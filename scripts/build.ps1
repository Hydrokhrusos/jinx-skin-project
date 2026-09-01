$ErrorActionPreference = 'Stop'
$env:PYTHONDONTWRITEBYTECODE = '1'

$projectRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$buildRoot = [IO.Path]::GetFullPath((Join-Path $projectRoot 'build\abyssal'))
$sourceRoot = Join-Path $buildRoot 'source\game'
$sourceTextRoot = Join-Path $buildRoot 'source\ritobin'
$generatedRoot = Join-Path $buildRoot 'generated'
$commonWad = Join-Path $generatedRoot 'common\Jinx.wad.client'
$reportRoot = Join-Path $projectRoot 'reports\generated'
$distRoot = Join-Path $projectRoot 'dist'
$baseRoot = Join-Path $projectRoot 'variants\base'
$baseContent = Join-Path $baseRoot 'content'
$baseConfig = Join-Path $baseRoot 'mod.config.json'
$projectConfig = Join-Path $projectRoot 'mod.config.json'

$blender = Join-Path $projectRoot '.tools\blender-4.5.13\blender-4.5.13-windows-x64\blender.exe'
$avRoot = Join-Path $projectRoot '.tools\Aventurine-3.1.5'
$ritobin = Join-Path $projectRoot '.tools\ritobin-2025-10-05\bin\ritobin_cli.exe'
$wadHashRoot = Join-Path $projectRoot '.tools\hashes'
$ritoHashRoot = Join-Path $projectRoot '.tools\ritobin-2025-10-05\bin\hashes'
$leagueMod = Join-Path $projectRoot '.tools\league-mod-modpkg-0.9.1\league-mod.exe'
$overlayBuilder = Join-Path $projectRoot '.tools\league-mod-modpkg-0.9.1\build_modpkg_overlay.exe'
$wadtools = Join-Path $projectRoot '.tools\wadtools-0.5.7\wadtools.exe'
$texconv = Join-Path $projectRoot '.tools\texconv-2026.5.8.exe'
$vgmstream = Join-Path $projectRoot '.tools\vgmstream-r2117\vgmstream-cli.exe'
$audioManifest = Join-Path $projectRoot 'source\audio\dark_witch\manifest.json'
$audioClips = Join-Path $projectRoot 'source\audio\dark_witch\clips'
$gameDir = 'C:\Riot Games\League of Legends\Game'
$gameWad = Join-Path $gameDir 'DATA\FINAL\Champions\Jinx.wad.client'
$versionMetadata = Join-Path $gameDir 'compat-version-metadata.json'

function Assert-ChildPath {
    param(
        [Parameter(Mandatory = $true)][string]$Child,
        [Parameter(Mandatory = $true)][string]$Parent
    )
    $resolvedChild = [IO.Path]::GetFullPath($Child)
    $resolvedParent = [IO.Path]::GetFullPath($Parent).TrimEnd('\') + '\'
    if (-not $resolvedChild.StartsWith($resolvedParent, [StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing generated-file operation outside $resolvedParent`: $resolvedChild"
    }
}

function Clear-GeneratedPath {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][string]$Parent
    )
    Assert-ChildPath -Child $Path -Parent $Parent
    if (Test-Path -LiteralPath $Path) {
        Remove-Item -LiteralPath $Path -Recurse -Force
    }
}

function Get-Sha256 {
    param([Parameter(Mandatory = $true)][string]$Path)
    $stream = [IO.File]::OpenRead($Path)
    $algorithm = [Security.Cryptography.SHA256]::Create()
    try {
        return [BitConverter]::ToString($algorithm.ComputeHash($stream)).Replace('-', '').ToLowerInvariant()
    }
    finally {
        $algorithm.Dispose()
        $stream.Dispose()
    }
}

foreach ($required in @(
    $blender,
    $avRoot,
    $ritobin,
    $wadHashRoot,
    $ritoHashRoot,
    $leagueMod,
    $overlayBuilder,
    $wadtools,
    $texconv,
    $vgmstream,
    $audioManifest,
    $audioClips,
    $gameWad,
    $versionMetadata,
    $baseConfig,
    $projectConfig
)) {
    if (-not (Test-Path -LiteralPath $required)) {
        throw "Required build input is missing: $required"
    }
}

$projectMetadata = Get-Content -LiteralPath $projectConfig -Raw | ConvertFrom-Json
$baseMetadata = Get-Content -LiteralPath $baseConfig -Raw | ConvertFrom-Json
$projectVersion = $projectMetadata.version
if ($projectVersion -notmatch '^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$') {
    throw "Project version is not semantic: $projectVersion"
}
if ($baseMetadata.version -ne $projectVersion) {
    throw "Project and base versions differ: $projectVersion / $($baseMetadata.version)"
}
if ($baseMetadata.name -ne $projectMetadata.name) {
    throw "Project and base package names differ: $($projectMetadata.name) / $($baseMetadata.name)"
}
$package = Join-Path $distRoot "$($projectMetadata.name)_$projectVersion.modpkg"

Clear-GeneratedPath -Path $buildRoot -Parent (Join-Path $projectRoot 'build')
Clear-GeneratedPath -Path $baseContent -Parent $baseRoot
New-Item -ItemType Directory -Force $sourceRoot, $sourceTextRoot, $commonWad, $reportRoot, $distRoot | Out-Null

$superseded = @($package)
foreach ($version in @('1.0.0', '1.0.1', '1.0.2', '1.0.3', '2.0.0', '3.0.0')) {
    $superseded += Join-Path $distRoot "abyssal-siren-jinx_$version.modpkg"
    $superseded += Join-Path $distRoot "abyssal-siren-jinx-encore_$version.modpkg"
}
foreach ($oldPackage in $superseded) {
    Assert-ChildPath -Child $oldPackage -Parent $distRoot
    if (Test-Path -LiteralPath $oldPackage) {
        Remove-Item -LiteralPath $oldPackage -Force
    }
}

$multiBinRelative = 'data\characters\jinx\jinx_multi_skins_skin65_skins_skin66_skins_skin67_skins_skin68_skins_skin69_skins_skin70_skins_skin71_skins_skin72_skins_skin73.bin'
$sourcePattern = '^(data/characters/jinx/(skins/skin65|jinx_multi_skins_skin65_skins_skin66_skins_skin67_skins_skin68_skins_skin69_skins_skin70_skins_skin71_skins_skin72_skins_skin73)\.bin|data/characters/jinxmine/skins/skin65\.bin|assets/characters/jinx/skins/base/animations/jinx_(minigun|rlauncher)_idle1\.anm|assets/characters/jinx/skins/skin51/(jinx_skin51\.sk[ln]|jinx_skin51_main_tx_cm\.tex)|assets/characters/jinx/skins/skin62/(jinx_skin62\.sk[ln]|jinx_skin62_(tx_cm|weapon_tx_cm|recall_tx_cm)\.tex)|assets/characters/jinx/skins/skin65/(animations/(spell2|recall)\.anm|jinx_skin65\.sk[ln]|jinx_skin65.*\.tex|particles/.*)|assets/characters/jinxmine/skins/skin62/(jinxmine_skin62\.sk[ln]|jinxmine_skin62_tx_cm\.tex)|assets/characters/jinxmine/skins/skin65/(jinxmine_skin65\.sk[ln]|jinxmine_skin65_tx_cm\.tex)|assets/shared/particles/.*|assets/sounds/wwise2016/sfx/characters/jinx/skins/skin65/jinx_skin65_sfx_(audio|events)\.bnk)$'

Push-Location $projectRoot
try {
    & $wadtools --hashtable-dir $wadHashRoot --progress=false -L error extract `
        -i $gameWad `
        -o $sourceRoot `
        -x $sourcePattern `
        --overwrite `
        --stats=false
    if ($LASTEXITCODE -ne 0) { throw "Authoritative source extraction failed with exit code $LASTEXITCODE" }

    $sourceJinxBin = Join-Path $sourceRoot 'data\characters\jinx\skins\skin65.bin'
    $sourceMineBin = Join-Path $sourceRoot 'data\characters\jinxmine\skins\skin65.bin'
    $sourceMultiBin = Join-Path $sourceRoot $multiBinRelative
    $sourceJinxText = Join-Path $sourceTextRoot 'jinx_skin65.py'
    $sourceMineText = Join-Path $sourceTextRoot 'jinxmine_skin65.py'
    $sourceMultiText = Join-Path $sourceTextRoot 'jinx_multi_skin65.py'
    & $ritobin $sourceJinxBin $sourceJinxText -i bin -o text -d $ritoHashRoot
    if ($LASTEXITCODE -ne 0) { throw "Jinx skin65 BIN decompilation failed with exit code $LASTEXITCODE" }
    & $ritobin $sourceMineBin $sourceMineText -i bin -o text -d $ritoHashRoot
    if ($LASTEXITCODE -ne 0) { throw "JinxMine skin65 BIN decompilation failed with exit code $LASTEXITCODE" }
    & $ritobin $sourceMultiBin $sourceMultiText -i bin -o text -d $ritoHashRoot
    if ($LASTEXITCODE -ne 0) { throw "Linked Ocean Song VFX BIN decompilation failed with exit code $LASTEXITCODE" }

    & $blender --background --factory-startup --python-exit-code 1 --python scripts\build_sea_witch_models.py -- `
        --target-skn (Join-Path $sourceRoot 'assets\characters\jinx\skins\skin65\jinx_skin65.skn') `
        --target-skl (Join-Path $sourceRoot 'assets\characters\jinx\skins\skin65\jinx_skin65.skl') `
        --body-donor-skn (Join-Path $sourceRoot 'assets\characters\jinx\skins\skin51\jinx_skin51.skn') `
        --body-donor-skl (Join-Path $sourceRoot 'assets\characters\jinx\skins\skin51\jinx_skin51.skl') `
        --weapon-donor-skn (Join-Path $sourceRoot 'assets\characters\jinx\skins\skin62\jinx_skin62.skn') `
        --weapon-donor-skl (Join-Path $sourceRoot 'assets\characters\jinx\skins\skin62\jinx_skin62.skl') `
        --target-mine-skn (Join-Path $sourceRoot 'assets\characters\jinxmine\skins\skin65\jinxmine_skin65.skn') `
        --target-mine-skl (Join-Path $sourceRoot 'assets\characters\jinxmine\skins\skin65\jinxmine_skin65.skl') `
        --mine-donor-skn (Join-Path $sourceRoot 'assets\characters\jinxmine\skins\skin62\jinxmine_skin62.skn') `
        --mine-donor-skl (Join-Path $sourceRoot 'assets\characters\jinxmine\skins\skin62\jinxmine_skin62.skl') `
        --target-missile-skn (Join-Path $sourceRoot 'assets\characters\jinx\skins\skin65\particles\jinx_skin65_r_mis_globefish_01_1.skn') `
        --addon-root $avRoot `
        --out-root $commonWad `
        --missile-relative 'assets/characters/jinx/skins/skin65/particles/jinx_skin65_r_mis_globefish_01_1.skn' `
        --report (Join-Path $reportRoot 'abyssal_models.json')
    if ($LASTEXITCODE -ne 0) { throw "Sea-witch model build failed with exit code $LASTEXITCODE" }

    & $blender --background --factory-startup --python-exit-code 1 --python scripts\build_sea_witch_textures.py -- `
        --source-root $sourceRoot `
        --out-root $commonWad `
        --addon-root $avRoot `
        --texconv $texconv `
        --preview-dir (Join-Path $buildRoot 'qa\textures') `
        --report (Join-Path $reportRoot 'abyssal_textures.json')
    if ($LASTEXITCODE -ne 0) { throw "Sea-witch texture build failed with exit code $LASTEXITCODE" }

    $vfxMap = Join-Path $buildRoot 'compiled\vfx_asset_map.json'
    & $blender --background --factory-startup --python-exit-code 1 --python scripts\build_abyssal_vfx_assets.py -- `
        --bin $sourceJinxText `
        --bin $sourceMultiText `
        --source-root $sourceRoot `
        --generated-root $commonWad `
        --out-root $commonWad `
        --addon-root $avRoot `
        --texconv $texconv `
        --map-out $vfxMap `
        --report (Join-Path $reportRoot 'abyssal_vfx_assets.json') `
        --preview-dir (Join-Path $buildRoot 'qa')
    if ($LASTEXITCODE -ne 0) { throw "Abyssal VFX dependency build failed with exit code $LASTEXITCODE" }

    $patchedJinxText = Join-Path $buildRoot 'compiled\jinx_skin65.py'
    $patchedMineText = Join-Path $buildRoot 'compiled\jinxmine_skin65.py'
    $patchedMultiText = Join-Path $buildRoot 'compiled\jinx_multi_skin65.py'
    & python scripts\patch_abyssal_bins.py `
        --jinx $sourceJinxText `
        --mine $sourceMineText `
        --multi $sourceMultiText `
        --vfx-map $vfxMap `
        --out-jinx $patchedJinxText `
        --out-mine $patchedMineText `
        --out-multi $patchedMultiText `
        --report (Join-Path $reportRoot 'abyssal_bins.json')
    if ($LASTEXITCODE -ne 0) { throw "Abyssal BIN patch failed with exit code $LASTEXITCODE" }

    $outJinxBin = Join-Path $commonWad 'data\characters\jinx\skins\skin65.bin'
    $outMineBin = Join-Path $commonWad 'data\characters\jinxmine\skins\skin65.bin'
    $outMultiBin = Join-Path $commonWad $multiBinRelative
    New-Item -ItemType Directory -Force (Split-Path $outJinxBin), (Split-Path $outMineBin), (Split-Path $outMultiBin) | Out-Null
    & $ritobin $patchedJinxText $outJinxBin -i text -o bin -d $ritoHashRoot
    if ($LASTEXITCODE -ne 0) { throw "Patched Jinx BIN compilation failed with exit code $LASTEXITCODE" }
    & $ritobin $patchedMineText $outMineBin -i text -o bin -d $ritoHashRoot
    if ($LASTEXITCODE -ne 0) { throw "Patched JinxMine BIN compilation failed with exit code $LASTEXITCODE" }
    & $ritobin $patchedMultiText $outMultiBin -i text -o bin -d $ritoHashRoot
    if ($LASTEXITCODE -ne 0) { throw "Patched linked Ocean Song VFX BIN compilation failed with exit code $LASTEXITCODE" }

    $sourceBankDirectory = Join-Path $sourceRoot 'assets\sounds\wwise2016\sfx\characters\jinx\skins\skin65'
    $outputBankDirectory = Join-Path $commonWad 'assets\sounds\wwise2016\sfx\characters\jinx\skins\skin65'
    & python -B scripts\build_dark_witch_audio.py build `
        --target-audio (Join-Path $sourceBankDirectory 'jinx_skin65_sfx_audio.bnk') `
        --target-events (Join-Path $sourceBankDirectory 'jinx_skin65_sfx_events.bnk') `
        --manifest $audioManifest `
        --clips-dir $audioClips `
        --vgmstream $vgmstream `
        --decoded-dir (Join-Path $buildRoot 'audio\decoded') `
        --out-audio (Join-Path $outputBankDirectory 'jinx_skin65_sfx_audio.bnk') `
        --out-events (Join-Path $outputBankDirectory 'jinx_skin65_sfx_events.bnk') `
        --report (Join-Path $reportRoot 'dark_witch_audio.json')
    if ($LASTEXITCODE -ne 0) { throw "Dark-witch SFX bank build failed with exit code $LASTEXITCODE" }

    $layerRoot = Join-Path $baseContent 'base'
    New-Item -ItemType Directory -Force $layerRoot | Out-Null
    Copy-Item -LiteralPath $commonWad -Destination (Join-Path $layerRoot 'Jinx.wad.client') -Recurse -Force

    & $leagueMod pack --config-path $baseConfig --output-dir $distRoot
    if ($LASTEXITCODE -ne 0) { throw "Visual-only modpkg packing failed with exit code $LASTEXITCODE" }
    if (-not (Test-Path -LiteralPath $package)) { throw "Expected package was not created: $package" }

    $validationRoot = Join-Path $buildRoot 'validation'
    $packageExtract = Join-Path $validationRoot 'package'
    $validationProfile = Join-Path $validationRoot 'profile'
    $overlayExtract = Join-Path $validationRoot 'overlay'
    foreach ($path in @($packageExtract, $validationProfile, $overlayExtract)) {
        New-Item -ItemType Directory -Force $path | Out-Null
    }
    & $leagueMod extract $package --output-dir $packageExtract
    if ($LASTEXITCODE -ne 0) { throw "Package extraction failed with exit code $LASTEXITCODE" }

    $overlayLog = & $overlayBuilder $package $gameDir $validationProfile 2>&1
    if ($LASTEXITCODE -ne 0) { throw "LTK overlay build failed with exit code $LASTEXITCODE" }
    $overlayLog | Set-Content -LiteralPath (Join-Path $reportRoot 'abyssal_base_overlay.txt') -Encoding UTF8
    $overlayWad = Join-Path $validationProfile 'overlay\DATA\FINAL\Champions\Jinx.wad.client'
    $contentPattern = '^(assets/characters/jinx/skins/skin65/.*|assets/characters/jinxmine/skins/skin65/.*|assets/sounds/wwise2016/sfx/characters/jinx/skins/skin65/jinx_skin65_sfx_(audio|events)\.bnk|data/characters/jinx/(skins/skin65|jinx_multi_skins_skin65_skins_skin66_skins_skin67_skins_skin68_skins_skin69_skins_skin70_skins_skin71_skins_skin72_skins_skin73)\.bin|data/characters/jinxmine/skins/skin65\.bin)$'
    & $wadtools --hashtable-dir $wadHashRoot --progress=false -L error extract `
        -i $overlayWad -o $overlayExtract -x $contentPattern --overwrite --stats=false
    if ($LASTEXITCODE -ne 0) { throw "Overlay extraction failed with exit code $LASTEXITCODE" }

    & python -B scripts\extract_overlay_paths.py `
        --wadtools $wadtools `
        --hash-root $wadHashRoot `
        --wad $overlayWad `
        --out-root $overlayExtract `
        --vfx-map $vfxMap `
        --path 'assets/characters/jinx/skins/skin65/jinx_skin65_seawitch_body_tx_cm.tex' `
        --path 'assets/characters/jinx/skins/skin65/jinx_skin65_seawitch_armor_tx_cm.tex' `
        --path 'assets/characters/jinx/skins/skin65/jinx_skin65_seawitch_weapon_tx_cm.tex' `
        --path 'assets/characters/jinx/skins/skin65/jinx_skin65_seawitch_recall_tx_cm.tex' `
        --report (Join-Path $reportRoot 'abyssal_overlay_hash_paths.json')
    if ($LASTEXITCODE -ne 0) { throw "Unresolved overlay path extraction failed with exit code $LASTEXITCODE" }

    & $blender --background --factory-startup --python-exit-code 1 --python scripts\render_sea_witch_qa.py -- `
        --skn (Join-Path $overlayExtract 'assets\characters\jinx\skins\skin65\jinx_skin65.skn') `
        --skl (Join-Path $overlayExtract 'assets\characters\jinx\skins\skin65\jinx_skin65.skl') `
        --body-texture (Join-Path $overlayExtract 'assets\characters\jinx\skins\skin65\jinx_skin65_seawitch_body_tx_cm.tex') `
        --armor-texture (Join-Path $overlayExtract 'assets\characters\jinx\skins\skin65\jinx_skin65_seawitch_armor_tx_cm.tex') `
        --weapon-texture (Join-Path $overlayExtract 'assets\characters\jinx\skins\skin65\jinx_skin65_seawitch_weapon_tx_cm.tex') `
        --recall-texture (Join-Path $overlayExtract 'assets\characters\jinx\skins\skin65\jinx_skin65_seawitch_recall_tx_cm.tex') `
        --mine-skn (Join-Path $overlayExtract 'assets\characters\jinxmine\skins\skin65\jinxmine_skin65.skn') `
        --mine-skl (Join-Path $overlayExtract 'assets\characters\jinxmine\skins\skin65\jinxmine_skin65.skl') `
        --mine-texture (Join-Path $overlayExtract 'assets\characters\jinxmine\skins\skin65\jinxmine_skin65_tx_cm.tex') `
        --missile-skn (Join-Path $overlayExtract 'assets\characters\jinx\skins\skin65\particles\jinx_skin65_r_mis_globefish_01_1.skn') `
        --missile-skl (Join-Path $overlayExtract 'assets\characters\jinx\skins\skin65\particles\jinx_skin65_r_mis_globefish_01_1.skl') `
        --missile-texture (Join-Path $overlayExtract 'assets\characters\jinx\skins\skin65\particles\jinx_skin65_r_mis_globefish.tex') `
        --minigun-animation (Join-Path $sourceRoot 'assets\characters\jinx\skins\base\animations\jinx_minigun_idle1.anm') `
        --rocket-animation (Join-Path $sourceRoot 'assets\characters\jinx\skins\base\animations\jinx_rlauncher_idle1.anm') `
        --zapper-animation (Join-Path $sourceRoot 'assets\characters\jinx\skins\skin65\animations\spell2.anm') `
        --recall-animation (Join-Path $sourceRoot 'assets\characters\jinx\skins\skin65\animations\recall.anm') `
        --addon-root $avRoot `
        --out-dir (Join-Path $buildRoot 'qa\model') `
        --report (Join-Path $reportRoot 'abyssal_visual_qa.json')
    if ($LASTEXITCODE -ne 0) { throw "Final overlay visual QA render failed with exit code $LASTEXITCODE" }

    & python scripts\validate_abyssal.py `
        --project-root $projectRoot `
        --package $package `
        --package-extract $packageExtract `
        --overlay $overlayExtract `
        --stock-wad $gameWad `
        --overlay-wad $overlayWad `
        --out (Join-Path $reportRoot 'abyssal_validation.json')
    if ($LASTEXITCODE -ne 0) { throw "Final package validation failed with exit code $LASTEXITCODE" }

    $gameVersion = (Get-Content -LiteralPath $versionMetadata -Raw | ConvertFrom-Json).version
    $toolchain = [ordered]@{
        status = 'PASSED'
        project_version = $projectVersion
        target = 'Ocean Song Jinx skin 65'
        scope = 'model, opaque textures, VFX, and complete skin SFX replacement; stock animations and voice-over retained'
        target_game_build = $gameVersion
        generated_at_utc = [DateTime]::UtcNow.ToString('o')
        tools = [ordered]@{
            blender = [ordered]@{ version = '4.5.13 LTS'; sha256 = (Get-Sha256 -Path $blender) }
            aventurine = [ordered]@{ version = '3.1.5' }
            ritobin = [ordered]@{ version = '2025-10-05'; sha256 = (Get-Sha256 -Path $ritobin) }
            wadtools = [ordered]@{ version = '0.5.7'; sha256 = (Get-Sha256 -Path $wadtools) }
            texconv = [ordered]@{ version = 'DirectXTex 2026.5.8'; sha256 = (Get-Sha256 -Path $texconv) }
            vgmstream = [ordered]@{ version = 'r2117'; sha256 = (Get-Sha256 -Path $vgmstream) }
            league_mod = [ordered]@{ version = '0.2.1 with ltk_modpkg 0.9.1'; sha256 = (Get-Sha256 -Path $leagueMod) }
        }
        packages = @(
            [ordered]@{ path = $package; sha256 = (Get-Sha256 -Path $package) }
        )
    }
    $toolchain | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $reportRoot 'abyssal_toolchain.json') -Encoding UTF8
    Write-Host "ABYSSAL_BUILD=PASSED PACKAGE=$package"
}
finally {
    Pop-Location
}
