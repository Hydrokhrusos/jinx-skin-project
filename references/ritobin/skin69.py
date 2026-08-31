#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Jinx/Jinx_Multi_Skins_Skin65_Skins_Skin66_Skins_Skin67_Skins_Skin68_Skins_Skin69_Skins_Skin70_Skins_Skin71_Skins_Skin72_Skins_Skin73.bin"
    "DATA/Characters/Jinx/Jinx_Multi_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin32_Skins_Skin33_Skins_Skin34_Skins_Skin35_Skins_Skin36_Skins_Skin37_Skins_Skin38_Skins_Skin39_Skins_Skin40_Skins_Skin41_Skins_Skin42_Skins_Skin43_Skins_Skin44_Skins_Skin45_Skins_Skin46_Skins_Skin47_Skins_Skin48_Skins_Skin49_Skins_Skin5_Skins_Skin51_Skins_Skin52_Skins_Skin53_Skins_Skin54_Skins_Skin55_Skins_Skin56_Skins_Skin57_Skins_Skin58_Skins_Skin59_Skins_Skin6_Skins_Skin62_Skins_Skin63_Skins_Skin64_Skins_Skin65_Skins_Skin66_Skins_Skin67_Skins_Skin68_Skins_Skin69_Skins_Skin7_Skins_Skin70_Skins_Skin71_Skins_Skin72_Skins_Skin73_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Characters/Jinx/Jinx.bin"
    "DATA/Characters/Jinx/Animations/Skin65.bin"
}
entries: map[hash,embed] = {
    0x56135d61 = 0x9b67e9f6 {
        0x87225880: u32 = 2
        0x2d78c328: string = "JinxSkin69"
        0x514b1c48: i32 = 65
        0x939e7b29: string = "faction:zaun,gender:female,race:human,skinline:oceansong"
        0xc3a944e7: pointer = 0xe7ee4f28 {
            0x7dd33afb: u32 = 18
        }
        0x97f7188d: embed = 0xd06263ff {
            0xb35135fa: file = 0x492abeec893c6b7c
        }
        0x8f7b194f: embed = 0x8f7b194f {
            0xd65bac4d: list[string] = {
                "Jinx"
                "JinxSkin65"
            }
            0xf8f29f92: list2[embed] = {
                0xa4416515 {
                    0x8d39bde6: string = "Jinx_Base_VO"
                    0x2a21ad00: list[string] = {
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Jinx/Skins/Base/Jinx_Base_VO_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Jinx/Skins/Base/Jinx_Base_VO_events.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Jinx/Skins/Base/Jinx_Base_VO_audio.wpk"
                    }
                    0x12d8e384: list[string] = {
                        "Play_vo_Jinx_Attack2DGeneral"
                        "Play_vo_Jinx_Death3D"
                        "Play_vo_Jinx_FirstEncounter3DCaitlyn"
                        "Play_vo_Jinx_FirstEncounter3DVi"
                        "Play_vo_Jinx_JinxE_cast3D"
                        "Play_vo_Jinx_JinxR_cast3D"
                        "Play_vo_Jinx_JinxW_cast3D"
                        "Play_vo_Jinx_Joke3DGeneral"
                        "Play_vo_Jinx_laugh3D_in"
                        "Play_vo_Jinx_laugh3D_loop"
                        "Play_vo_Jinx_Move2DStandard"
                        "Play_vo_Jinx_Recall3DGeneral"
                        "Play_vo_Jinx_Taunt3DGeneral"
                    }
                    0x3b13aa4b: bool = true
                }
                0xa4416515 {
                    0x8d39bde6: string = "Jinx_Skin65_SFX"
                    0x2a21ad00: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Jinx/Skins/Skin65/Jinx_Skin65_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Jinx/Skins/Skin65/Jinx_Skin65_SFX_events.bnk"
                    }
                    0x12d8e384: list[string] = {
                        "Play_sfx_JinxSkin65_Dance3D_buffactivate"
                        "Play_sfx_JinxSkin65_Dance3D_loop"
                        "Play_sfx_JinxSkin65_Death3D_cast"
                        "Play_sfx_JinxSkin65_JinxBasicAttack2_OnCast"
                        "Play_sfx_JinxSkin65_JinxBasicAttack2_OnHit"
                        "Play_sfx_JinxSkin65_JinxBasicAttack2_OnMissileCast"
                        "Play_sfx_JinxSkin65_JinxBasicAttack2_OnMissileLaunch"
                        "Play_sfx_JinxSkin65_JinxBasicAttack_OnCast"
                        "Play_sfx_JinxSkin65_JinxBasicAttack_OnHit"
                        "Play_sfx_JinxSkin65_JinxBasicAttack_OnMissileCast"
                        "Play_sfx_JinxSkin65_JinxBasicAttack_OnMissileLaunch"
                        "Play_sfx_JinxSkin65_JinxCritAttack_OnCast"
                        "Play_sfx_JinxSkin65_JinxCritAttack_OnHit"
                        "Play_sfx_JinxSkin65_JinxCritAttack_OnMissileCast"
                        "Play_sfx_JinxSkin65_JinxCritAttack_OnMissileLaunch"
                        "Play_sfx_JinxSkin65_JinxE_OnCast"
                        "Play_sfx_JinxSkin65_JinxEMine_OnBuffActivate"
                        "Play_sfx_JinxSkin65_JinxEMine_OnBuffDeactivate"
                        "Play_sfx_JinxSkin65_JinxEMineSnare_OnBuffActivate"
                        "Play_sfx_JinxSkin65_JinxPassiveKill_OnBuffActivate"
                        "Play_sfx_JinxSkin65_JinxQ_OnBuffActivate"
                        "Play_sfx_JinxSkin65_JinxQAttack2_OnCast"
                        "Play_sfx_JinxSkin65_JinxQAttack2_OnMissileCast"
                        "Play_sfx_JinxSkin65_JinxQAttack2_OnMissileLaunch"
                        "Play_sfx_JinxSkin65_JinxQAttack_hit"
                        "Play_sfx_JinxSkin65_JinxQAttack_OnCast"
                        "Play_sfx_JinxSkin65_JinxQAttack_OnMissileCast"
                        "Play_sfx_JinxSkin65_JinxQAttack_OnMissileLaunch"
                        "Play_sfx_JinxSkin65_JinxQCritAttack_OnCast"
                        "Play_sfx_JinxSkin65_JinxQCritAttack_OnMissileCast"
                        "Play_sfx_JinxSkin65_JinxQCritAttack_OnMissileLaunch"
                        "Play_sfx_JinxSkin65_JinxQIcon_OnBuffActivate"
                        "Play_sfx_JinxSkin65_JinxR_boosteractivate"
                        "Play_sfx_JinxSkin65_JinxR_boosterlaunch"
                        "Play_sfx_JinxSkin65_JinxR_hit"
                        "Play_sfx_JinxSkin65_JinxR_missilelaunch"
                        "Play_sfx_JinxSkin65_JinxR_OnCast"
                        "Play_sfx_JinxSkin65_JinxR_OnMissileCast"
                        "Play_sfx_JinxSkin65_JinxW_OnCast"
                        "Play_sfx_JinxSkin65_JinxWMissile_hit"
                        "Play_sfx_JinxSkin65_JinxWMissile_OnMissileCast"
                        "Play_sfx_JinxSkin65_JinxWMissile_OnMissileLaunch"
                        "Play_sfx_JinxSkin65_Joke3D_buffactivate"
                        "Play_sfx_JinxSkin65_Recall3D_buffactivate"
                        "Play_sfx_JinxSkin65_Respawn3D_buffactivate"
                        "Play_sfx_JinxSkin65_Taunt23D_buffactivate"
                        "Play_sfx_JinxSkin65_Taunt3D_buffactivate"
                        "Play_sfx_JinxSkin65_Winddown3D_buffactivate"
                        "Stop_sfx_JinxSkin65_Dance3D_buffactivate"
                        "Stop_sfx_JinxSkin65_Dance3D_loop"
                        "Stop_sfx_JinxSkin65_JinxBasicAttack_OnMissileLaunch"
                        "Stop_sfx_JinxSkin65_JinxCritAttack_OnMissileLaunch"
                        "Stop_sfx_JinxSkin65_JinxPassiveKill_OnBuffActivate"
                        "Stop_sfx_JinxSkin65_JinxQAttack2_OnMissileLaunch"
                        "Stop_sfx_JinxSkin65_JinxQAttack_OnMissileLaunch"
                        "Stop_sfx_JinxSkin65_JinxQCritAttack_OnMissileLaunch"
                        "Stop_sfx_JinxSkin65_JinxR_boosterlaunch"
                        "Stop_sfx_JinxSkin65_JinxR_missilelaunch"
                        "Stop_sfx_JinxSkin65_JinxWMissile_OnMissileLaunch"
                        "Stop_sfx_JinxSkin65_Respawn3D_buffactivate"
                    }
                }
            }
        }
        0x426d89a3: embed = 0x426d89a3 {
            0xf5fb07c7: link = 0x6e5ceb16
        }
        0x45ff5904: embed = 0x6111d8a4 {
            0xb14c976e: string = "ASSETS/Characters/Jinx/Skins/Skin65/Jinx_Skin65.skl"
            0xd6a00df6: string = "ASSETS/Characters/Jinx/Skins/Skin65/Jinx_Skin65.skn"
            0x3c6468f4: file = 0xbc3da5eaf2ee3a19
            0xa1f805da: f32 = 1.03
            0x252f6884: f32 = 0.7
            0xc91afa4d: f32 = 0.4
            0x5c7a0332: option[vec3] = {
                { 160, 228.1, 160 }
            }
            0xd2e4d060: link = 0x841b8034
            0x561f4fea: rgba = { 0, 0, 0, 255 }
            0x80b7f78f: string = "Recall"
            0xf4ba5c9e: string = "Recall"
            0x382825a9: string = "Recall"
            0x24725910: list[embed] = {
                0x8b7a4394 {
                    0xd2e4d060: link = 0x841b8034
                    0xaad7612c: string = "Weapon"
                }
                0x8b7a4394 {
                    0xd2e4d060: link = 0x0b65b451
                    0xaad7612c: string = "Body"
                }
                0x8b7a4394 {
                    0xd2e4d060: link = 0xd22ae377
                    0xaad7612c: string = "WeaponVFX"
                }
                0x8b7a4394 {
                    0x3c6468f4: file = 0xbc3da5eaf2ee3a19
                    0xaad7612c: string = "Hair"
                }
                0x8b7a4394 {
                    0xd2e4d060: link = 0xa8760645
                    0xaad7612c: string = "Skirt"
                }
                0x8b7a4394 {
                    0x3c6468f4: file = 0xe3508349ef6fd41c
                    0xaad7612c: string = "Recall"
                }
            }
            0xe9c98281: list[pointer] = {
                0xce0b9a93 {
                    0xc6a8e023: hash = 0x1997b0f5
                    0x96dbc896: hash = 0x1297a5f0
                    0x50271332: hash = 0xef7cfc3b
                    0x3288d6d8: f32 = 0
                }
                0xce0b9a93 {
                    0xc6a8e023: hash = 0xde970e9b
                    0x96dbc896: hash = 0xe397167a
                    0x50271332: hash = 0xef7cfc3b
                    0x3288d6d8: f32 = 0
                }
            }
        }
        0x2d0d1f1d: string = "Flesh"
        0x123393ed: list[string] = {
            "Rlauncher_To_Minigun"
        }
        0x84186f3c: list[embed] = {
            0x33068165 {
                0x9b0300f3: hash = 0xe562facd
                0x1ecb978c: string = "Buffbone_R_dress"
            }
            0x33068165 {
                0x9b0300f3: hash = 0x08a38d85
                0x1ecb978c: string = "Buffbone_L_dress"
            }
            0x33068165 {
                0x9b0300f3: hash = 0xa96c9a02
                0x1ecb978c: string = "Root"
            }
            0x33068165 {
                0x9b0300f3: hash = 0x30efbad8
                0x1ecb978c: string = "L_Hair1"
            }
            0x33068165 {
                0x9b0300f3: hash = 0x33efbf91
                0x1ecb978c: string = "R_Hair1"
            }
        }
        0x660c8b4e: list[string] = {
            "JinxMine"
        }
        0xd8f64a0d: link = 0xc1f683c5
        0xe67284f4: option[file] = {
            0xbfafbb160ef44938
        }
        0xac473fef: option[file] = {
            0x8519545a82fe8941
        }
        0x089aff69: file = 0x6703525659da4e06
        0x51c83af8: embed = 0x11b71b5e {
            0x3fcb5693: u8 = 12
        }
        0xb698fb27: list[embed] = {
            0x7ba9ed2e {
                0x5df7536e: link = 0x24aba2b0
            }
        }
        0x62286e7e: link = 0x7060b543
        0x87b1d303: list2[pointer] = {
            0x67ac9672 {
                0x43c8c7b1: pointer = 0x9233f657 {
                    0x7aceca0f: list[pointer] = {
                        0xd5a6ab25 {
                            0x85045366: pointer = 0x087188b5 {
                                0x30b2f4b2: list[hash] = {
                                    0x5a81bdb0
                                }
                            }
                        }
                    }
                }
                0x071f3c1d: list2[embed] = {
                    0x00fa43e4 {
                        0x1ecb978c: string = "Minigun"
                        0xda428935: string = "R_Shoulder"
                        0x9b0300f3: hash = 0x1720d661
                    }
                }
            }
        }
        0x55d3758e: string = "ASSETS/Characters/Jinx/Skins/Skin69/ChromaPreview.tex"
        0x1d369c29: hash = 0x56135d61
    }
    0x0b65b451 = 0xff9d3409 {
        0x8d39bde6: string = "Characters/Jinx/Skins/Skin69/Materials/Matcap_Iridescent_Holographic_Body_inst"
        0x0a6f0eb5: list2[embed] = {
            0x0904b150 {
                0xb311d4ef: string = "Dissolve_Gradient_Texture"
                0xf0a363e3: file = 0xb1070dff5a760d5c
            }
            0x0904b150 {
                0xb311d4ef: string = "Dissolve_Texture"
                0xf0a363e3: file = 0x529442b91a3a6c5e
            }
            0x0904b150 {
                0xb311d4ef: string = "Diffuse_Texture"
                0xf0a363e3: file = 0xbc3da5eaf2ee3a19
                0x111ec6d2: u32 = 1
                0x101ec53f: u32 = 1
                0x0f1ec3ac: u32 = 1
            }
            0x0904b150 {
                0xb311d4ef: string = "Mask_Texture"
                0xf0a363e3: file = 0x219c7582503c10c6
                0x111ec6d2: u32 = 1
                0x101ec53f: u32 = 1
                0x0f1ec3ac: u32 = 1
            }
            0x0904b150 {
                0xb311d4ef: string = "MatCap_Tex"
                0xf0a363e3: file = 0xf907fb5294a70dea
                0x111ec6d2: u32 = 1
                0x101ec53f: u32 = 1
                0x0f1ec3ac: u32 = 1
            }
            0x0904b150 {
                0xb311d4ef: string = "iridescentTex"
                0xf0a363e3: file = 0x879f01a634742bbe
                0x0f1ec3ac: u32 = 1
            }
            0x0904b150 {
                0xb311d4ef: string = "Noise_Texture"
                0xf0a363e3: file = 0x8b1cf0ca3b7e8f42
                0x0f1ec3ac: u32 = 1
            }
            0x0904b150 {
                0xb311d4ef: string = "Flowmap"
                0xf0a363e3: file = 0xb2f42548b598ff28
                0x111ec6d2: u32 = 1
                0x101ec53f: u32 = 1
                0x0f1ec3ac: u32 = 1
            }
        }
        0xd0ab46b8: list2[embed] = {
            0xde480eef {
                0x8d39bde6: string = "Rim_Light_Power"
                0x425ed3ca: vec4 = { 2, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Rim_Light_Intensity"
                0x425ed3ca: vec4 = { 2, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Rim_Light_Color"
                0x425ed3ca: vec4 = { 0.10966659, 0.9057603, 0.9001907, 1 }
            }
            0xde480eef {
                0x8d39bde6: string = "rimOffset"
                0x425ed3ca: vec4 = { 0.985, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "albedoNewMin"
                0x425ed3ca: vec4 = { 0.1, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "albedoNewMax"
                0x425ed3ca: vec4 = { 1, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "modelHeight"
                0x425ed3ca: vec4 = { 275, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Alpha_Sharpness"
                0x425ed3ca: vec4 = { 0.001, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Dissolve_SmoothStep"
                0x425ed3ca: vec4 = { 0, 1, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Gradient_Sharpness"
                0x425ed3ca: vec4 = { 4, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Dissolve_Bias"
            }
            0xde480eef {
                0x8d39bde6: string = "TintColor"
                0x425ed3ca: vec4 = { 1, 1, 1, 1 }
            }
            0xde480eef {
                0x8d39bde6: string = "MatCap_Strength"
                0x425ed3ca: vec4 = { 1, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "MatCapSpecularPower"
                0x425ed3ca: vec4 = { 1, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "MatCapSpecularTintColor"
                0x425ed3ca: vec4 = { 1, 1, 1, 1 }
            }
            0xde480eef {
                0x8d39bde6: string = "Iridescent_Strength"
                0x425ed3ca: vec4 = { 0.6, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Iridescent_Value"
                0x425ed3ca: vec4 = { 1, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Iridescent_Power"
                0x425ed3ca: vec4 = { 10, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Iridescent_Normal_Blend"
                0x425ed3ca: vec4 = { 1, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Holo_Strength"
                0x425ed3ca: vec4 = { 0.5, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Holo_Gradient_Contrast"
                0x425ed3ca: vec4 = { 5, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "BaseNoiseUVTile"
                0x425ed3ca: vec4 = { 0.1, 0.1, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "BaseNoiseScrollSpeed"
                0x425ed3ca: vec4 = { 0.04, 0.006, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "NoiseStrength"
                0x425ed3ca: vec4 = { 5, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Flowspeed"
            }
            0xde480eef {
                0x8d39bde6: string = "Bloom_Intensity"
                0x425ed3ca: vec4 = { 0.3, 0, 0, 0 }
            }
        }
        0xdd7ddb9d: list2[embed] = {
            0x0e2212a1 {
                0x8d39bde6: string = "ADD_FRESNEL_RIM"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "USE_ALBEDO_REMAP"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "USE_RIM"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "USE_DISSOLVE"
                0x61342fd0: bool = false
                0x5fb91e8c: string = "Dissolve"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "FRESNEL_MASK_HOLOGRAPHIC"
                0x5fb91e8c: string = "Holographic"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "MATCAP_ON"
                0x5fb91e8c: string = "Mat Cap"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "MATCAP_MASK_ON"
                0x5fb91e8c: string = "Mat Cap"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "IRIDESCENCE_ON"
                0x5fb91e8c: string = "Iridescent"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "IRIDESCENT_MASK_ON"
                0x5fb91e8c: string = "Iridescent"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "HOLOGRAPHIC_ON"
                0x5fb91e8c: string = "Holographic"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "HOLOGRAPHIC_MASK_ON"
                0x5fb91e8c: string = "Holographic"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "FLOWMAP_ON"
                0x61342fd0: bool = false
                0x5fb91e8c: string = "Holographic"
            }
        }
        0xe6d67ded: map[string,string] = {
            "NUM_BLEND_WEIGHTS" = "4"
        }
        0x844f384e: list[embed] = {
            0x060a4413 {
                0x8d39bde6: string = "normal"
                0x623cd25c: list[embed] = {
                    0x8537d0c2 {
                        0x355d5568: link = 0xbceb4368
                        0x23b75597: bool = true
                        0x22c0c7d0: u32 = 6
                        0xa0958d01: u32 = 6
                        0xbe0abbf5: u32 = 7
                        0x7385e534: u32 = 7
                    }
                }
            }
        }
        0x9330e6b6: list[embed] = {
            0x735b4c95 {
                0x8d39bde6: string = "transition"
                0xb696a5fe: string = "normal"
                0xe6d67ded: map[string,string] = {
                    "TRANSITION" = "1"
                }
            }
        }
    }
    0x841b8034 = 0xff9d3409 {
        0x8d39bde6: string = "Characters/Jinx/Skins/Skin69/Materials/Matcap_Iridescent_Holographic_inst"
        0x0a6f0eb5: list2[embed] = {
            0x0904b150 {
                0xb311d4ef: string = "Dissolve_Gradient_Texture"
                0xf0a363e3: file = 0xb1070dff5a760d5c
            }
            0x0904b150 {
                0xb311d4ef: string = "Dissolve_Texture"
                0xf0a363e3: file = 0x529442b91a3a6c5e
            }
            0x0904b150 {
                0xb311d4ef: string = "Diffuse_Texture"
                0xf0a363e3: file = 0x52442a16c2c54b6d
                0x111ec6d2: u32 = 1
                0x101ec53f: u32 = 1
                0x0f1ec3ac: u32 = 1
            }
            0x0904b150 {
                0xb311d4ef: string = "Mask_Texture"
                0xf0a363e3: file = 0x16845f9071df4542
                0x111ec6d2: u32 = 1
                0x101ec53f: u32 = 1
                0x0f1ec3ac: u32 = 1
            }
            0x0904b150 {
                0xb311d4ef: string = "MatCap_Tex"
                0xf0a363e3: file = 0xfdc3f48c05442cfc
                0x111ec6d2: u32 = 1
                0x101ec53f: u32 = 1
                0x0f1ec3ac: u32 = 1
            }
            0x0904b150 {
                0xb311d4ef: string = "iridescentTex"
                0xf0a363e3: file = 0x879f01a634742bbe
                0x0f1ec3ac: u32 = 1
            }
            0x0904b150 {
                0xb311d4ef: string = "Noise_Texture"
                0xf0a363e3: file = 0x8b1cf0ca3b7e8f42
                0x0f1ec3ac: u32 = 1
            }
            0x0904b150 {
                0xb311d4ef: string = "Flowmap"
                0xf0a363e3: file = 0xb2f42548b598ff28
                0x111ec6d2: u32 = 1
                0x101ec53f: u32 = 1
                0x0f1ec3ac: u32 = 1
            }
        }
        0xd0ab46b8: list2[embed] = {
            0xde480eef {
                0x8d39bde6: string = "Rim_Light_Power"
                0x425ed3ca: vec4 = { 2, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Rim_Light_Intensity"
                0x425ed3ca: vec4 = { 2, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Rim_Light_Color"
                0x425ed3ca: vec4 = { 0.10966659, 0.9057603, 0.9001907, 1 }
            }
            0xde480eef {
                0x8d39bde6: string = "rimOffset"
                0x425ed3ca: vec4 = { 0.985, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "albedoNewMin"
                0x425ed3ca: vec4 = { 0.1, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "albedoNewMax"
                0x425ed3ca: vec4 = { 1, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "modelHeight"
                0x425ed3ca: vec4 = { 275, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Alpha_Sharpness"
                0x425ed3ca: vec4 = { 0.001, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Dissolve_SmoothStep"
                0x425ed3ca: vec4 = { 0, 1, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Gradient_Sharpness"
                0x425ed3ca: vec4 = { 4, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Dissolve_Bias"
            }
            0xde480eef {
                0x8d39bde6: string = "TintColor"
                0x425ed3ca: vec4 = { 1, 1, 1, 1 }
            }
            0xde480eef {
                0x8d39bde6: string = "MatCap_Strength"
                0x425ed3ca: vec4 = { 0.5, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "MatCapSpecularPower"
                0x425ed3ca: vec4 = { 1, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "MatCapSpecularTintColor"
                0x425ed3ca: vec4 = { 1, 1, 1, 1 }
            }
            0xde480eef {
                0x8d39bde6: string = "Iridescent_Strength"
                0x425ed3ca: vec4 = { 0.5, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Iridescent_Value"
                0x425ed3ca: vec4 = { 1, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Iridescent_Power"
                0x425ed3ca: vec4 = { 10, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Iridescent_Normal_Blend"
                0x425ed3ca: vec4 = { 1, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Holo_Strength"
                0x425ed3ca: vec4 = { 0.5, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Holo_Gradient_Contrast"
                0x425ed3ca: vec4 = { 5, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "BaseNoiseUVTile"
                0x425ed3ca: vec4 = { 0.1, 0.1, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "BaseNoiseScrollSpeed"
                0x425ed3ca: vec4 = { 0.04, 0.006, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "NoiseStrength"
                0x425ed3ca: vec4 = { 5, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Flowspeed"
            }
            0xde480eef {
                0x8d39bde6: string = "Bloom_Intensity"
                0x425ed3ca: vec4 = { 0.3, 0, 0, 0 }
            }
        }
        0xdd7ddb9d: list2[embed] = {
            0x0e2212a1 {
                0x8d39bde6: string = "ADD_FRESNEL_RIM"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "USE_ALBEDO_REMAP"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "USE_RIM"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "USE_DISSOLVE"
                0x61342fd0: bool = false
                0x5fb91e8c: string = "Dissolve"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "FRESNEL_MASK_HOLOGRAPHIC"
                0x5fb91e8c: string = "Holographic"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "MATCAP_ON"
                0x5fb91e8c: string = "Mat Cap"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "MATCAP_MASK_ON"
                0x5fb91e8c: string = "Mat Cap"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "IRIDESCENCE_ON"
                0x5fb91e8c: string = "Iridescent"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "IRIDESCENT_MASK_ON"
                0x5fb91e8c: string = "Iridescent"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "HOLOGRAPHIC_ON"
                0x5fb91e8c: string = "Holographic"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "HOLOGRAPHIC_MASK_ON"
                0x5fb91e8c: string = "Holographic"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "FLOWMAP_ON"
                0x61342fd0: bool = false
                0x5fb91e8c: string = "Holographic"
            }
        }
        0xe6d67ded: map[string,string] = {
            "NUM_BLEND_WEIGHTS" = "4"
        }
        0x844f384e: list[embed] = {
            0x060a4413 {
                0x8d39bde6: string = "normal"
                0x623cd25c: list[embed] = {
                    0x8537d0c2 {
                        0x355d5568: link = 0xbceb4368
                        0x23b75597: bool = true
                        0x22c0c7d0: u32 = 6
                        0xa0958d01: u32 = 6
                        0xbe0abbf5: u32 = 7
                        0x7385e534: u32 = 7
                    }
                }
            }
        }
        0x9330e6b6: list[embed] = {
            0x735b4c95 {
                0x8d39bde6: string = "transition"
                0xb696a5fe: string = "normal"
                0xe6d67ded: map[string,string] = {
                    "TRANSITION" = "1"
                }
            }
        }
    }
    0xa8760645 = 0xff9d3409 {
        0x8d39bde6: string = "Characters/Jinx/Skins/Skin69/Materials/Skirt_inst"
        0x0a6f0eb5: list2[embed] = {
            0x0904b150 {
                0xb311d4ef: string = "Diffuse_Texture"
                0xf0a363e3: file = 0x38aa3010fdd52168
                0x0f1ec3ac: u32 = 1
            }
            0x0904b150 {
                0xb311d4ef: string = "Bottom_Texture"
                0xf0a363e3: file = 0x5a6966203b2dcead
                0x0f1ec3ac: u32 = 1
            }
            0x0904b150 {
                0xb311d4ef: string = "Top_Texture"
                0xf0a363e3: file = 0x73450aac16943977
                0x0f1ec3ac: u32 = 1
            }
            0x0904b150 {
                0xb311d4ef: string = "Alpha_Mask"
                0xf0a363e3: file = 0x830863549ce1c9ef
                0x0f1ec3ac: u32 = 1
            }
        }
        0xd0ab46b8: list2[embed] = {
            0xde480eef {
                0x8d39bde6: string = "modelHeight"
                0x425ed3ca: vec4 = { 275, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "rimOffset"
            }
            0xde480eef {
                0x8d39bde6: string = "albedoNewMax"
                0x425ed3ca: vec4 = { 1, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "albedoNewMin"
                0x425ed3ca: vec4 = { 0.1, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "VertAnim_UV_Dir2"
                0x425ed3ca: vec4 = { 1, 1, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Low_Quality_Bias"
                0x425ed3ca: vec4 = { 1, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Alpha_Bounds"
                0x425ed3ca: vec4 = { 0, 1, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Alpha_Bias"
            }
            0xde480eef {
                0x8d39bde6: string = "Bottom_ScrollSpeed"
                0x425ed3ca: vec4 = { 0, -0.05, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Top_ScrollSpeed"
                0x425ed3ca: vec4 = { 0, -0.153, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Alpha_Scale"
                0x425ed3ca: vec4 = { 1, 1, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Diffuse_AlphaIntensity"
                0x425ed3ca: vec4 = { 1, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Top_AlphaIntensity"
                0x425ed3ca: vec4 = { 0.6725, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Bottom_AlphaIntensity"
                0x425ed3ca: vec4 = { 0.5425, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Alpha_Rate"
                0x425ed3ca: vec4 = { 0.1, 0.2, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Top_UVScale"
                0x425ed3ca: vec4 = { 1, 1, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Bottom_UVScale"
                0x425ed3ca: vec4 = { 1.3, 1, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Diffuse_Tint"
                0x425ed3ca: vec4 = { 1, 1, 1, 1 }
            }
            0xde480eef {
                0x8d39bde6: string = "Bloom_Intensity"
                0x425ed3ca: vec4 = { 0.075, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "VertAnim_Intensity"
                0x425ed3ca: vec4 = { 0.4, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "VertAnim_Line_Thick"
                0x425ed3ca: vec4 = { 0.8, 16, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "VertAnim_UV_Speed"
                0x425ed3ca: vec4 = { 0.64, 1, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "VertAnim_UV_Tiling"
                0x425ed3ca: vec4 = { 8, 8, 0, 0 }
            }
        }
        0xdd7ddb9d: list2[embed] = {
            0x0e2212a1 {
                0x8d39bde6: string = "USE_RIM"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "USE_ALBEDO_REMAP"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "DIFFUSEHOLD_USING_BCHANNEL"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "BLOOM"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "VERTEX_WOBBLE_PANNING_LINE"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "VERTEX_COLOR_MASK"
                0x61342fd0: bool = false
            }
        }
        0xe6d67ded: map[string,string] = {
            "NUM_BLEND_WEIGHTS" = "4"
        }
        0x844f384e: list[embed] = {
            0x060a4413 {
                0x8d39bde6: string = "normal"
                0x623cd25c: list[embed] = {
                    0x8537d0c2 {
                        0x355d5568: link = 0xb3635c9d
                        0x23b75597: bool = true
                        0x22c0c7d0: u32 = 6
                        0xa0958d01: u32 = 6
                        0xbe0abbf5: u32 = 7
                        0x7385e534: u32 = 7
                    }
                }
            }
        }
        0x9330e6b6: list[embed] = {
            0x735b4c95 {
                0x8d39bde6: string = "transition"
                0xb696a5fe: string = "normal"
                0xe6d67ded: map[string,string] = {
                    "TRANSITION" = "1"
                }
            }
        }
        0x86875ff3: pointer = 0x2d6bf1a2 {}
    }
    0xd22ae377 = 0xff9d3409 {
        0x8d39bde6: string = "Characters/Jinx/Skins/Skin69/Materials/WeaponVFX"
        0x0a6f0eb5: list2[embed] = {
            0x0904b150 {
                0xb311d4ef: string = "Diffuse_Texture"
                0xf0a363e3: file = 0x52442a16c2c54b6d
                0x0f1ec3ac: u32 = 1
            }
            0x0904b150 {
                0xb311d4ef: string = "Bottom_Texture"
                0x0f1ec3ac: u32 = 1
            }
            0x0904b150 {
                0xb311d4ef: string = "Top_Texture"
                0xf0a363e3: file = 0xa6950e6fda96aa67
                0x0f1ec3ac: u32 = 1
            }
            0x0904b150 {
                0xb311d4ef: string = "Alpha_Mask"
                0xf0a363e3: file = 0x441946a7c63657f8
                0x0f1ec3ac: u32 = 1
            }
        }
        0xd0ab46b8: list2[embed] = {
            0xde480eef {
                0x8d39bde6: string = "modelHeight"
                0x425ed3ca: vec4 = { 275, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "rimOffset"
                0x425ed3ca: vec4 = { 0.3, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "albedoNewMax"
                0x425ed3ca: vec4 = { 1, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "albedoNewMin"
                0x425ed3ca: vec4 = { 0.1, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "VertAnim_UV_Dir2"
                0x425ed3ca: vec4 = { 1, 1, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Low_Quality_Bias"
                0x425ed3ca: vec4 = { 1, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Alpha_Bounds"
                0x425ed3ca: vec4 = { 0, 1, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Alpha_Bias"
            }
            0xde480eef {
                0x8d39bde6: string = "Bottom_ScrollSpeed"
                0x425ed3ca: vec4 = { 0, -0.1, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Top_ScrollSpeed"
                0x425ed3ca: vec4 = { -0.3, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Alpha_Scale"
                0x425ed3ca: vec4 = { 1, 1, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Diffuse_AlphaIntensity"
                0x425ed3ca: vec4 = { 0.805, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Top_AlphaIntensity"
                0x425ed3ca: vec4 = { 0.9875, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Bottom_AlphaIntensity"
            }
            0xde480eef {
                0x8d39bde6: string = "Alpha_Rate"
                0x425ed3ca: vec4 = { 0.1, 0.2, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Top_UVScale"
                0x425ed3ca: vec4 = { 1, 1, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Bottom_UVScale"
                0x425ed3ca: vec4 = { 1, 1, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "Diffuse_Tint"
                0x425ed3ca: vec4 = { 0.7375143, 0.7340963, 0.9963226, 1 }
            }
            0xde480eef {
                0x8d39bde6: string = "Bloom_Intensity"
                0x425ed3ca: vec4 = { 0.3, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "VertAnim_Intensity"
                0x425ed3ca: vec4 = { 2, 0, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "VertAnim_Line_Thick"
                0x425ed3ca: vec4 = { 0.618, 16, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "VertAnim_UV_Speed"
                0x425ed3ca: vec4 = { 0.64, 1, 0, 0 }
            }
            0xde480eef {
                0x8d39bde6: string = "VertAnim_UV_Tiling"
                0x425ed3ca: vec4 = { 16, 16, 0, 0 }
            }
        }
        0xdd7ddb9d: list2[embed] = {
            0x0e2212a1 {
                0x8d39bde6: string = "USE_RIM"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "USE_ALBEDO_REMAP"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "DIFFUSEHOLD_USING_BCHANNEL"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "BLOOM"
            }
            0x0e2212a1 {
                0x8d39bde6: string = "VERTEX_WOBBLE_PANNING_LINE"
                0x61342fd0: bool = false
            }
            0x0e2212a1 {
                0x8d39bde6: string = "VERTEX_COLOR_MASK"
                0x61342fd0: bool = false
            }
        }
        0xe6d67ded: map[string,string] = {
            "NUM_BLEND_WEIGHTS" = "4"
        }
        0x844f384e: list[embed] = {
            0x060a4413 {
                0x8d39bde6: string = "normal"
                0x623cd25c: list[embed] = {
                    0x8537d0c2 {
                        0x355d5568: link = 0xb3635c9d
                        0x23b75597: bool = true
                        0x22c0c7d0: u32 = 6
                        0xa0958d01: u32 = 6
                        0xbe0abbf5: u32 = 7
                        0x7385e534: u32 = 7
                    }
                }
            }
        }
        0x9330e6b6: list[embed] = {
            0x735b4c95 {
                0x8d39bde6: string = "transition"
                0xb696a5fe: string = "normal"
                0xe6d67ded: map[string,string] = {
                    "TRANSITION" = "1"
                }
            }
        }
        0x86875ff3: pointer = 0x2d6bf1a2 {}
    }
    0x1149b587 = 0x45cd899f {
        0x868eb76a: list[pointer] = {
            0x09cde442 {
                0x22e763bc: f32 = 0.1
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.15
                }
                0x5212abee: option[f32] = {
                    2
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Distort_Warp"
                0xb9516a6f: u8 = 3
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -100, 170 }
                }
                0xb56e8811: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin60_color-rampdown32.tex"
                0xfa784eab: u8 = 1
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.7
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 3000
                0xbc809cdb: pointer = 0x49d51b69 {
                    0xbc5efeaa: f32 = 0.01
                    0xe672d557: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin60_distort_soft_shockwave.tex"
                }
                0x67b5d729: vec2 = { -1, -25 }
                0x3c91cebd: bool = true
                0x6563bee8: u8 = 1
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 450, 200, 200 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.6250996, 0.2, 0.2 }
                            { 1, 1, 1 }
                            { 1.3, 1.3, 1.3 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Shared/Particles/DefaultColorOverlifetime.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 30
                    0xbc037de7: pointer = 0xfe064c88 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.3
                            0.5
                            1
                        }
                        0x34474c3b: list[f32] = {
                            60
                            30
                            3
                            0
                        }
                    }
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    0.7
                                    1.2
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            1
                        }
                    }
                }
                0x2431d42c: option[f32] = {
                    11
                }
                0x5212abee: option[f32] = {
                    50
                }
                0x3d25b8ce: string = "SparklesFast"
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 200, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.3
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 200, 0, 0 }
                        }
                    }
                }
                0x8275da98: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 5, 5, 5 }
                }
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -600, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -600, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    0x9c677a2c: u8 = 1
                    0x0dba4cb3: f32 = 35
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -150, 90 }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.9000076 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.6
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                            0.5
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0.9000076 }
                            { 0.192157, 1, 0.827451, 0.9000076 }
                            { 1, 0, 0.682353, 0.9000076 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.3
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.23921569, 0.8352941, 1, 1 }
                            { 0.24313726, 0.7607843, 1, 1 }
                            { 0.13725491, 0.30588236, 0.85490197, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 50
                0x2674b1b5: u8 = 3
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x1f661402: f32 = 30
                }
                0x3559e15b: flag = true
                0xe09d5ebb: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 90, 0, 0 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 10, 35, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 10, 35, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.2
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.2, 2, 0 }
                            { 0.8, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Zeri_Skin10_Q_Bubble01.tex"
                0x1e67b0f1: u16 = 4
                0x86a84509: vec2 = { 2, 2 }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 400
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.8
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.2
                                    1
                                    1.5
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            0.8
                        }
                    }
                }
                0x2431d42c: option[f32] = {
                    1
                }
                0x5212abee: option[f32] = {
                    5
                }
                0x3d25b8ce: string = "PSmoke"
                0xb9516a6f: u8 = 3
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -20, 0 }
                }
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -500, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -500, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    0x9c677a2c: u8 = 1
                    0x23a0d95c: vec3 = { 15, 100, 30 }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 30, 100 }
                }
                0xb56e8811: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin51_Flicker_04.tex"
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.66999316 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.2
                            0.3
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.5372549, 0.85490197, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.5137255, 0.7882353, 1, 1 }
                            { 0.14901961, 0.19215687, 1, 1 }
                            { 0.13333334, 0.19215687, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 997
                0x2674b1b5: u8 = 3
                0xcb13aff1: f32 = -80
                0x3559e15b: flag = true
                0xe09d5ebb: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                0x1d779e6a: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 80, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 80, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 25, 0.377, 0.377 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.2
                                    1
                                }
                            }
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.2
                                    1.1
                                }
                            }
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.2
                                    1.1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 25, 0.377, 0.377 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.2, 0.2, 0.2 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin62_EnergyMote.tex"
                0x1e67b0f1: u16 = 2
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 6
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.6
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.4
                                    0.75
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            0.6
                        }
                    }
                }
                0x2431d42c: option[f32] = {
                    1
                }
                0x5212abee: option[f32] = {
                    5
                }
                0x3d25b8ce: string = "PSmoke1"
                0xb9516a6f: u8 = 3
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -20, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -20, 0 }
                        }
                    }
                }
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    0x9c677a2c: u8 = 1
                    0x23a0d95c: vec3 = { 50, 150, 30 }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -100, -30 }
                }
                0xb56e8811: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Bokeh_Color.tex"
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.42000458 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0.42000458 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.13207547
                            0.3
                            0.43910807
                            0.77186966
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.84615386 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.8552036 }
                            { 1, 1, 1, 0.19004525 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 50
                0x2674b1b5: u8 = 3
                0x3559e15b: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                0x1d779e6a: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 80, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 80, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 30, 6, 6 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 30, 6, 6 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Dance_Sparks.tex"
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.1
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "FakeShadow2"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, -130, 0 }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0, -10 }
                }
                0x007b14f6: pointer = 0x4beb81fd {}
                0xb56e8811: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/color-hold_2.tex"
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.34117648, 0.28235295, 0.67058825, 1 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.001
                            0.015
                            0.02
                            0.5
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = -1
                0x19bdf4df: u8 = 0
                0xb99310f4: u8 = 0
                0x6563bee8: u8 = 1
                0x27d40903: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 80, 300, 700 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/W_Beam_EPassive_03_1_1_2.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Caitlyn_Skin51_AnimeShapes061.tex"
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = 90
                    }
                }
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.08
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.2
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Ground_light2"
                0xb9516a6f: u8 = 3
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -40, 100 }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.77999544 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.3
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.8627451, 0.36078432, 1, 0.3019608 }
                            { 0.48235294, 0.13725491, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 20
                0xb99310f4: u8 = 0
                0x6563bee8: u8 = 1
                0x3559e15b: flag = true
                0x27d40903: flag = true
                0xdddde180: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1, 0, 90 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 0, 90 }
                        }
                    }
                }
                0x1d779e6a: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 10, 0, 0 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 350, 350, 0 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.57768923, 0, 0 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 1.5 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Camille_Skin44_Q_Hex_Indicator_1_1_007.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Caitlyn_Skin51_BA_Color03.tex"
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = 1
                        0xbc037de7: pointer = 0xfe064c88 {
                            0xa7084719: list[pointer] = {
                                0x53a6c97e {
                                    0x40c351da: list[f32] = {
                                        0
                                        1
                                    }
                                    0xe44b7382: list[f32] = {
                                        -360
                                        1
                                    }
                                }
                            }
                            0x5d68eeb5: list[f32] = {
                                0
                            }
                            0x34474c3b: list[f32] = {
                                1
                            }
                        }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 12
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.4
                }
                0x2431d42c: option[f32] = {
                    0.1
                }
                0x5212abee: option[f32] = {
                    50
                }
                0x3d25b8ce: string = "WaterAdd"
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -100, 0 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Zeri_Skin10_R_Water.scb"
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.2399939, 0.7100023, 1, 0.2 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.01
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.2399939, 0.7100023, 1, 0 }
                            { 0.2399939, 0.7100023, 1, 0.2 }
                            { 0.2399939, 0.7100023, 1, 0.2 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.3
                            0.8
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = -2
                0xb99310f4: u8 = 0
                0x6563bee8: u8 = 1
                0x27d40903: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -270, 0, 0 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0.85, 0, 1.7 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.05
                            0.6
                            0.95
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 0.5, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 0, 1 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Zeri_Skin10_Wave_Foam_Stylized_01.tex"
                0x264afd39: u8 = 2
                0xcfb707de: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0, -0.2 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 0, -0.2 }
                        }
                    }
                }
                0xb9198a2a: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 1, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 0, 1 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 0, 1 }
                        }
                    }
                }
                0xeddebb48: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 1.3, 1.7 }
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_Water_Alpha01.tex"
                    0x5b249407: u8 = 2
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 100
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.65
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            1
                        }
                    }
                }
                0x2431d42c: option[f32] = {
                    1
                }
                0x3d25b8ce: string = "circleSPARKLES"
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -100, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -100, 0 }
                        }
                    }
                }
                0x8275da98: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 3, 5, 0 }
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    0x9c677a2c: u8 = 1
                    0x23a0d95c: vec3 = { 10, 10, 10 }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 135, 60, 0 }
                }
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.7499962 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.2
                            0.4
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.29411766, 0.6, 1, 1 }
                            { 0.17000076, 0.5300069, 1, 0.2 }
                            { 0.08999771, 0.40999466, 1, 0.2 }
                        }
                    }
                }
                0x7b7a7318: i16 = 6
                0x67b5d729: vec2 = { -1, -50 }
                0x3559e15b: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 16, 10, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.15
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 16, 10, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.3
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_R_BightSpark.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 100
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.65
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            1
                        }
                    }
                }
                0x2431d42c: option[f32] = {
                    1
                }
                0x3d25b8ce: string = "circleSPARKLES1"
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -100, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -100, 0 }
                        }
                    }
                }
                0x8275da98: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 3, 5, 0 }
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    0x9c677a2c: u8 = 1
                    0x23a0d95c: vec3 = { 10, 10, 10 }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -135, 60, 0 }
                }
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.7499962 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.2
                            0.4
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.29411766, 0.6, 1, 1 }
                            { 0.17000076, 0.5300069, 1, 0.2 }
                            { 0.08999771, 0.40999466, 1, 0.2 }
                        }
                    }
                }
                0x7b7a7318: i16 = 6
                0x67b5d729: vec2 = { -1, -50 }
                0x3559e15b: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 16, 10, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.15
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 16, 10, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.3
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_R_BightSpark.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 100
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.6
                }
                0x2431d42c: option[f32] = {
                    0.25
                }
                0x5212abee: option[f32] = {
                    50
                }
                0x3d25b8ce: string = "L_Edge2"
                0x8275da98: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 2, 0, 2 }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 150, 0, 0 }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 80, 0 }
                }
                0x007b14f6: pointer = 0x5705625a {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 700, 0, 0 }
                        }
                        0x0ea6d9c1: u8 = 1
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.2 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.001
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.2 }
                            { 1, 1, 1, 0.2 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.2
                            0.4
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.2 }
                            { 1, 1, 1, 1 }
                            { 0.2901961, 0.59607846, 1, 0.3019608 }
                            { 0.20784314, 0.28627452, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 1
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    0x2244caa3: f32 = 0.3
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_R_Water02.tex"
                }
                0x6563bee8: u8 = 1
                0x3559e15b: flag = true
                0x27d40903: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 50, 50, 0 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.3
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.2, 1, 1 }
                            { 1, 1, 1 }
                            { 0.2, 1, 1 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_R_Water02.tex"
                0xcfb707de: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0.3, 0 }
                }
                0xb9198a2a: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0.5, 0 }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.4
                }
                0x2431d42c: option[f32] = {
                    0.6
                }
                0x5212abee: option[f32] = {
                    50
                }
                0x50b7397d: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0.1, 0.1 }
                }
                0x3d25b8ce: string = "Trail_BG6"
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -35, 5, 100 }
                }
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 1500
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 500, 0, 0 }
                        }
                        0x0ea6d9c1: u8 = 1
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.5100023 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.02
                            0.9
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.5100023 }
                            { 1, 1, 1, 0.5100023 }
                            { 1, 1, 1, 0.40800184 }
                            { 1, 1, 1, 0.40800184 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.15
                            0.35
                            0.65
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.73333335, 0.3647059, 1, 0 }
                            { 0.7882353, 0.3647059, 1, 0.54901963 }
                            { 0.5254902, 0.2509804, 1, 0.67058825 }
                            { 0.050003815, 0.1600061, 0.7400015, 0.10000763 }
                            { 0.007843138, 0.12941177, 0.5647059, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 4
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xb4b427aa: f32 = 0
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    0x34bee0ea: f32 = 0.25
                    0x2244caa3: f32 = 0.25
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                0x6563bee8: u8 = 1
                0x3559e15b: flag = true
                0x27d40903: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 110, 1, 1 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.014
                            0.016
                            0.02
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 93.5, 0, 0 }
                            { 93.5, 1, 1 }
                            { 110, 0, 0 }
                            { 110, 0, 0 }
                            { 110, 0, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.8, 1, 1 }
                            { 1, 1, 1 }
                            { 0.4, 0.2, 0.2 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_09.tex"
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 0.05, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 0.05, 0 }
                        }
                    }
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/W_Mis_Water_1_01111.tex"
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = 90
                    }
                    0xcd124686: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 1, 60 }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.45
                }
                0x2431d42c: option[f32] = {
                    0.6
                }
                0x5212abee: option[f32] = {
                    50
                }
                0x3d25b8ce: string = "TrailBlend5"
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -60, 90 }
                }
                0x007b14f6: pointer = 0x5705625a {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 350, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.001
                            0.1
                            0.2
                            0.8
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0.8 }
                            { 1, 1, 1, 0.8 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.45
                            0.60182154
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.20392157, 0.654902, 1, 0 }
                            { 0.19215687, 0.654902, 0.9411765, 0.8392157 }
                            { 0.20999466, 0.34000152, 0.88000304, 0.46999314 }
                            { 0.2899977, 0.17000076, 0.59000534, 0.22000457 }
                            { 0.29411766, 0.050980393, 0.46666667, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 2
                0x6563bee8: u8 = 1
                0x3559e15b: flag = true
                0x27d40903: flag = true
                0x676949a1: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 70, 1, 1 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.05
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.6, 1, 1 }
                            { 0.6, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Q_Trail_fill.tex"
                0xcfb707de: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0.3, 0 }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.6
                }
                0x2431d42c: option[f32] = {
                    0.6
                }
                0x5212abee: option[f32] = {
                    50
                }
                0x3d25b8ce: string = "TrailBlend6"
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -300, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -300, 0 }
                        }
                    }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0, 85 }
                }
                0x007b14f6: pointer = 0x5705625a {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 700, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.85000384 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.01
                            0.015
                            0.9
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0.6800031 }
                            { 1, 1, 1, 0.6800031 }
                            { 1, 1, 1, 0.85000384 }
                            { 1, 1, 1, 0.85000384 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.40406722
                            0.5482442
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.08627451, 0.52156866, 0.75686276, 0 }
                            { 0.2899977, 0.37000075, 0.86999315, 0.7000076 }
                            { 0.3764706, 0.30980393, 0.8784314, 0.9098039 }
                            { 0.4399939, 0.2, 0.7000076, 0.5600061 }
                            { 0.15686275, 0.015686275, 0.29803923, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 1
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    0x34bee0ea: f32 = 0.25
                    0x2244caa3: f32 = 0.25
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                0x6563bee8: u8 = 1
                0x3559e15b: flag = true
                0x27d40903: flag = true
                0x676949a1: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 150, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.014
                            0.0165
                            0.02
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 120, 0, 0 }
                            { 120, 0, 0 }
                            { 150, 0, 0 }
                            { 135, 0, 0 }
                            { 135, 0, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.7, 1, 1 }
                            { 1.2, 1, 1 }
                            { 0.7, 1, 1 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Aurora_Skin20_Comet_Trail_01.tex"
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 0.3, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 0.3, 0 }
                        }
                    }
                }
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.1
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Conemesh_1"
                0x32741c32: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -70, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.0121
                            0.015
                            0.016
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -7, 0 }
                            { 0, -70, 0 }
                            { 0, -70, 0 }
                            { 0, -0, 0 }
                        }
                    }
                }
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -80, 100 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/fireball.SCB"
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.5254902, 0.8980392, 1, 1 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.3137255, 0.5764706, 1, 1 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.014
                            0.016
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.3137255, 0.5764706, 1, 1 }
                            { 0.3137255, 0.5764706, 1, 1 }
                            { 0.3137255, 0.5764706, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 322
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x6b89d541: f32 = 20
                    0x1f661402: f32 = 10
                }
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xb4b427aa: f32 = 0
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Shyvana_Base_E_ErosionLoweRes.tex"
                    0xb0794a80: embed = 0x074f91dd {
                        0xb4b427aa: vec4 = { 1, 0, 0, 0 }
                    }
                    0x2b32227b: u8 = 0
                }
                0x6563bee8: u8 = 1
                0x37ddb774: flag = true
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -90, 0, 0 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 5, 5, 11 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 2, 2, 2 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.012
                            0.016
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 2, 2, 2 }
                            { 2, 2, 2 }
                            { 2.4, 2.4, 2.6 }
                            { 2.4, 2.4, 2.6 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Shared/Particles/3026_Items_Streaks.tex"
                0xcfb707de: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0, 0.55 }
                }
                0xb9198a2a: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { -0.25, 0.5 }
                }
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 0.5, 2 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            0.5
                        }
                        0x34474c3b: list[vec2] = {
                            { 0.5, 4 }
                            { 0.5, 4 }
                            { 0.5, 1 }
                        }
                    }
                }
                0xeddebb48: embed = 0x69dc3449 {
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.5
                            1
                        }
                        0x34474c3b: list[vec2] = {
                            { 1, 2 }
                            { 1, 0.5 }
                            { 1, 1 }
                        }
                    }
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Morg_Base_E_MeshMult.tex"
                    0x5b249407: u8 = 2
                    0xcd124686: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 1, 1.35 }
                    }
                    0x740ca9c0: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 0, -0.25 }
                    }
                }
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.1
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0xa03664c8: pointer = 0xb520045a {
                    0x663f55e6: list[embed] = {
                        0x969aee94 {
                            0x9b0300f3: hash = 0x9da4674d
                        }
                    }
                }
                0x3d25b8ce: string = "FakeShadow3"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, -50, 100 }
                }
                0x007b14f6: pointer = 0x4beb81fd {}
                0xb56e8811: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/color-hold_2.tex"
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.020004578, 0.020004578, 0.050003815, 0 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0 }
                }
                0x7b7a7318: i16 = 103
                0x19bdf4df: u8 = 0
                0xb99310f4: u8 = 0
                0x6563bee8: u8 = 1
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -120, 0 }
                }
                0x712b01bd: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -15, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.002
                            0.01
                            0.012
                            0.018
                            0.019
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -7.5, 0 }
                            { 0, -0, 0 }
                            { 0, -0, 0 }
                            { 0, -0, 0 }
                            { 0, -60, 0 }
                            { 0, -8.25, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 110, 200, 700 }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Projected21"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 30, 102 }
                }
                0x007b14f6: pointer = 0x4beb81fd {}
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.4 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.014
                            0.018
                            0.025
                            0.1
                            0.7
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 5
                0x19bdf4df: u8 = 0
                0xb99310f4: u8 = 0
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0, 90 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 100, 80, 700 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0.08
                            0.018
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_splash_ring_Mask_1_1_011_3.tex"
                0x968279e0: embed = 0x04300058 {
                    0xb4b427aa: f32 = 180
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Trail_01_7.tex"
                    0x5b249407: u8 = 2
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = 180
                    }
                    0xcd124686: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 1, 1.1 }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.55
                }
                0x2431d42c: option[f32] = {
                    0.6
                }
                0x5212abee: option[f32] = {
                    50
                }
                0x50b7397d: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0.1, 0.1 }
                }
                0x3d25b8ce: string = "Trail_BG7"
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -100, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -100, 0 }
                        }
                    }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 25, 35, 100 }
                }
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 1500
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 850, 0, 0 }
                        }
                        0x0ea6d9c1: u8 = 1
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.5100023, 0.7100023, 1, 0.42999923 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.9
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.5100023, 0.7100023, 1, 0 }
                            { 0.5100023, 0.7100023, 1, 0.42999923 }
                            { 0.5100023, 0.7100023, 1, 0.42999923 }
                            { 0.5100023, 0.7100023, 1, 0.42999923 }
                            { 0.5100023, 0.7100023, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.15
                            0.25
                            0.4
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.26999313 }
                            { 1, 1, 1, 0.65882355 }
                            { 1, 1, 1, 0.42000458 }
                            { 1, 1, 1, 0.2399939 }
                            { 0.5647059, 0.5647059, 0.5647059, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 3
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    0x34bee0ea: f32 = 0.25
                    0x2244caa3: f32 = 0.25
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                0x6563bee8: u8 = 1
                0x3559e15b: flag = true
                0x27d40903: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 120, 1, 1 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.014
                            0.016
                            0.02
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 102, 0, 0 }
                            { 102, 1, 1 }
                            { 120, 0, 0 }
                            { 120, 0, 0 }
                            { 120, 0, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 0.5 }
                            { 0.3, 0.5, 0.5 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_08.tex"
                0x52010b69: vec2 = { 0.15, 0 }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Caitlyn_Skin51_AnimeShapes061.tex"
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.4
                }
                0x2431d42c: option[f32] = {
                    0.6
                }
                0x5212abee: option[f32] = {
                    50
                }
                0x50b7397d: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0.1, 0.1 }
                }
                0x3d25b8ce: string = "Trail_BG8"
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -35, 5, 100 }
                }
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 1500
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 500, 0, 0 }
                        }
                        0x0ea6d9c1: u8 = 1
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.85000384, 0.4599985, 1, 0.4 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.9
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.85000384, 0.4599985, 1, 0 }
                            { 0.85000384, 0.4599985, 1, 0.4 }
                            { 0.85000384, 0.4599985, 1, 0.4 }
                            { 0.85000384, 0.4599985, 1, 0.4 }
                            { 0.85000384, 0.4599985, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.7499962 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.15
                            0.35
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.38999572 }
                            { 1, 1, 1, 0.5024923 }
                            { 1, 1, 1, 0.08250129 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 3
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xb4b427aa: f32 = 0
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    0x34bee0ea: f32 = 0.25
                    0x2244caa3: f32 = 0.25
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                0x6563bee8: u8 = 1
                0x3559e15b: flag = true
                0x27d40903: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 110, 1, 1 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.014
                            0.016
                            0.02
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 93.5, 0, 0 }
                            { 93.5, 1, 1 }
                            { 110, 0, 0 }
                            { 110, 0, 0 }
                            { 110, 0, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.8, 1, 1 }
                            { 1, 1, 1 }
                            { 0.4, 0.2, 0.2 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_09.tex"
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 0.05, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 0.05, 0 }
                        }
                    }
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_mis_Mask_Color_6_1.tex"
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Missle12"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, -50, 100 }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -2, 0, 0 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_Splash_1_004.scb"
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.73333335, 0, 0, 1 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.014
                            0.018
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 800
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x6b89d541: f32 = 20
                    0x1f661402: f32 = 10
                }
                0x67b5d729: vec2 = { -1, -100 }
                0x6563bee8: u8 = 1
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -95, 180, 0 }
                }
                0x712b01bd: embed = 0x6ccc7f03 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.002
                            0.01
                            0.014
                            0.018
                            0.019
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 4, 4, 4 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.004
                            0.012
                            0.014
                            0.016
                            0.02
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.0053098, 1.0053098, 1.0053098 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 0.2 }
                            { 0.5, 0.5, 1.25 }
                            { 1.2, 1.2, 1.2 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_mis_Mask_Color_6_011.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Missle13"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, -50, 100 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0x8c41a32e: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skn"
                        0x90595a15: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skl"
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 0.06999313, 0.06999313, 0.6 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.012
                            0.015
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 104
                0x67b5d729: vec2 = { -1, -100 }
                0xb5158067: flag = true
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -95, 180, 0 }
                }
                0x712b01bd: embed = 0x6ccc7f03 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.002
                            0.01
                            0.014
                            0.018
                            0.019
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 4, 4, 4 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.004
                            0.012
                            0.014
                            0.016
                            0.02
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.0053098, 1.0053098, 1.0053098 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 0.2 }
                            { 0.5, 0.5, 1.25 }
                            { 1.2, 1.2, 1.2 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Pufferfish_1_01.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Missle15"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, -50, 100 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0x8c41a32e: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skn"
                        0x90595a15: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skl"
                    }
                }
                0xfa784eab: u8 = 4
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 0.42745098, 0.25490198, 1 }
                }
                0x7b7a7318: i16 = 103
                0x67b5d729: vec2 = { -1, -100 }
                0xb5158067: flag = true
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -95, 180, 0 }
                }
                0x712b01bd: embed = 0x6ccc7f03 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.002
                            0.01
                            0.014
                            0.018
                            0.019
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 4, 4, 4 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.004
                            0.012
                            0.014
                            0.016
                            0.02
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.0053098, 1.0053098, 1.0053098 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 0.2 }
                            { 0.5, 0.5, 1.25 }
                            { 1.2, 1.2, 1.2 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_mis_globefish_Mask_1.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    5
                }
                0x42bd7f6b: flag = true
                0x3bc59eb6: option[f32] = {
                    0.3
                }
                0x3d25b8ce: string = "head_"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {}
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -210, 95 }
                }
                0x007b14f6: pointer = 0x4beb81fd {}
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.78431374, 0.78431374, 0.78431374, 0.4 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.014
                            0.02
                            0.1
                            0.7
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 2
                0x19bdf4df: u8 = 0
                0xb99310f4: u8 = 0
                0x6563bee8: u8 = 1
                0x8d2e2474: flag = true
                0x27d40903: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 180, 0, 90 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 160, 100, 100 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 2, 1, 1 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lux_Skin70_Idle_Glow051_4.tex"
                0xeddebb48: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { -1, 1 }
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_Mask_1_1_01.tex"
                }
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.1
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    3
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Temp_GroundGlow2"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, -345, 0 }
                }
                0x007b14f6: pointer = 0x4beb81fd {}
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 0.7921569, 0.30588236, 0.6 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.6 }
                }
                0x7b7a7318: i16 = 1
                0xb99310f4: u8 = 0
                0x6563bee8: u8 = 1
                0x27d40903: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0, 90 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 700, 430, 180 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0.85, 0.8, 0.85 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Mis_Beam_1_01.tex"
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.1
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    3
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Temp_GroundGlow6"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, -350, 0 }
                }
                0x007b14f6: pointer = 0x4beb81fd {}
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.7400015, 0.7400015, 0.7400015, 0.68999773 }
                }
                0x7b7a7318: i16 = -3
                0xb99310f4: u8 = 0
                0x6563bee8: u8 = 1
                0x27d40903: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0, 90 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 700, 430, 180 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0.85, 0.8, 0.85 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_07.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_06.tex"
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = 180
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Projected23"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -15, 102 }
                }
                0x007b14f6: pointer = 0x4beb81fd {}
                0xfa784eab: u8 = 4
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 0.8901961, 0.5019608, 1 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 0.8901961, 0.5019608, 0 }
                            { 1, 0.8901961, 0.5019608, 1 }
                            { 1, 0.8901961, 0.5019608, 1 }
                            { 1, 0.8901961, 0.5019608, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 4
                0x19bdf4df: u8 = 0
                0xb99310f4: u8 = 0
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0, 90 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 90, 90, 50 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.4
                            0.6
                            0.75
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.2, 1, 0.2 }
                            { 1, 1, 1 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_splash_ring_Mask_1_1_011_3.tex"
                0x968279e0: embed = 0x04300058 {
                    0xb4b427aa: f32 = 180
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Trail_01_7.tex"
                    0x5b249407: u8 = 2
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = 180
                    }
                    0xcd124686: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 1, 1.1 }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Projected24"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 30, 102 }
                }
                0x007b14f6: pointer = 0x4beb81fd {}
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.5000076 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.7000076 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.014
                            0.018
                            0.025
                            0.1
                            0.7
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0.7000076 }
                        }
                    }
                }
                0x7b7a7318: i16 = 4
                0x19bdf4df: u8 = 0
                0xb99310f4: u8 = 0
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0, 90 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 100, 100, 700 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0.08
                            0.018
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_splash_ring_Mask_1_1_011_3.tex"
                0x968279e0: embed = 0x04300058 {
                    0xb4b427aa: f32 = 180
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_splash_ring_Mask_2_01.tex"
                    0x5b249407: u8 = 2
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = 180
                    }
                    0xcd124686: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 1, 1.1 }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.55
                }
                0x2431d42c: option[f32] = {
                    0.6
                }
                0x5212abee: option[f32] = {
                    50
                }
                0x50b7397d: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0.1, 0.1 }
                }
                0x3d25b8ce: string = "Trail_BG9"
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -100, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -100, 0 }
                        }
                    }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 25, 35, 100 }
                }
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 1500
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 850, 0, 0 }
                        }
                        0x0ea6d9c1: u8 = 1
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.4 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.02
                            0.9
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0.32 }
                            { 1, 1, 1, 0.32 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.15
                            0.25
                            0.4
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.30980393, 0.9647059, 1, 0 }
                            { 0.2399939, 0.7600061, 1, 0.37999544 }
                            { 0.2901961, 0.57254905, 1, 0.6784314 }
                            { 0.33000687, 0.37000075, 1, 0.4500038 }
                            { 0.2500038, 0.30000764, 1, 0.22000457 }
                            { 0.101960786, 0.101960786, 0.36862746, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 4
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    0x34bee0ea: f32 = 0.25
                    0x2244caa3: f32 = 0.25
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                0x6563bee8: u8 = 1
                0x3559e15b: flag = true
                0x27d40903: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 120, 1, 1 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.014
                            0.016
                            0.02
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 102, 0, 0 }
                            { 102, 1, 1 }
                            { 120, 0, 0 }
                            { 120, 0, 0 }
                            { 120, 0, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 0.5 }
                            { 0.4, 0.5, 0.5 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_08.tex"
                0x52010b69: vec2 = { 0.15, 0 }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/W_Mis_Water_1_01111.tex"
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = 90
                    }
                    0xcd124686: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 1, 80 }
                    }
                }
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.1
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Conemesh_5"
                0x32741c32: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -70, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.0121
                            0.015
                            0.016
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -7, 0 }
                            { 0, -70, 0 }
                            { 0, -70, 0 }
                            { 0, -0, 0 }
                        }
                    }
                }
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -155, 100 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin62_Q_dash_half_sphere.scb"
                    }
                }
                0xfa784eab: u8 = 4
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 0.60784316, 0.12941177, 1 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.013
                            0.015
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 0.48389083, 0.041614763, 0 }
                            { 1, 0.60784316, 0.12941177, 1 }
                            { 1, 0.60784316, 0.12941177, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 100
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x6b89d541: f32 = 20
                    0x1f661402: f32 = 10
                }
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xb4b427aa: f32 = 0
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Shyvana_Base_E_ErosionLoweRes.tex"
                    0xb0794a80: embed = 0x074f91dd {
                        0xb4b427aa: vec4 = { 1, 0, 0, 0 }
                    }
                    0x2b32227b: u8 = 0
                }
                0x6563bee8: u8 = 1
                0x37ddb774: flag = true
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 90, 0 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1.7, 5, 1.7 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.012
                            0.015
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1.2, 1.2, 1.3 }
                            { 1.2, 1.2, 1.3 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/3026_Items_color01.tex"
                0xb9198a2a: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { -0.25, 0.5 }
                }
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 0, -3 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 0, -3 }
                        }
                    }
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Gradient03_02.tex"
                    0xcd124686: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 2, 1 }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Missle16"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, -50, 100 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0x8c41a32e: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skn"
                        0x90595a15: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skl"
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.49411765, 0.03529412, 0.03529412, 1 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.012
                            0.015
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 105
                0x67b5d729: vec2 = { -1, -100 }
                0xb5158067: flag = true
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -95, 180, 0 }
                }
                0x712b01bd: embed = 0x6ccc7f03 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.002
                            0.01
                            0.014
                            0.018
                            0.019
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 4, 4, 4 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.004
                            0.012
                            0.014
                            0.016
                            0.02
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.0053098, 1.0053098, 1.0053098 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 0.2 }
                            { 0.5, 0.5, 1.25 }
                            { 1.2, 1.2, 1.2 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Mask_Pufferfish_3_01.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Missle17"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, -50, 100 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0x8c41a32e: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skn"
                        0x90595a15: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skl"
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 0.078431375, 0.078431375, 1 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.012
                            0.015
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 106
                0x67b5d729: vec2 = { -1, -100 }
                0xb5158067: flag = true
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -95, 180, 0 }
                }
                0x712b01bd: embed = 0x6ccc7f03 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.002
                            0.01
                            0.014
                            0.018
                            0.019
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 4, 4, 4 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.004
                            0.012
                            0.014
                            0.016
                            0.02
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.0053098, 1.0053098, 1.0053098 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 0.2 }
                            { 0.5, 0.5, 1.25 }
                            { 1.2, 1.2, 1.2 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Mask_Pufferfish_3_01.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Shared/Particles/Augment_Mercy_WispMult.tex"
                    0x32356474: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 0, 0.5 }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 100
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.6
                }
                0x2431d42c: option[f32] = {
                    0.25
                }
                0x5212abee: option[f32] = {
                    50
                }
                0x3d25b8ce: string = "L_Edge4"
                0x8275da98: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 2, 0, 2 }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { -150, 0, 0 }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 80, 0 }
                }
                0x007b14f6: pointer = 0x5705625a {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 700, 0, 0 }
                        }
                        0x0ea6d9c1: u8 = 1
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.2 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.001
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.2 }
                            { 1, 1, 1, 0.2 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.2
                            0.4
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.2 }
                            { 1, 1, 1, 1 }
                            { 0.2901961, 0.59607846, 1, 0.3019608 }
                            { 0.20784314, 0.28627452, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 1
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    0x2244caa3: f32 = 0.3
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_R_Water03.tex"
                }
                0x6563bee8: u8 = 1
                0x3559e15b: flag = true
                0x27d40903: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 50, 50, 0 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.3
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.2, 1, 1 }
                            { 1, 1, 1 }
                            { 0.2, 1, 1 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_R_Water03.tex"
                0xcfb707de: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0.3, 0 }
                }
                0xb9198a2a: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0.5, 0 }
                }
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.08
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Projected25"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -30, 100 }
                }
                0x007b14f6: pointer = 0x4beb81fd {}
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.6 }
                }
                0x7b7a7318: i16 = -2
                0x19bdf4df: u8 = 0
                0xb99310f4: u8 = 0
                0x3559e15b: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0, 90 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 420, 700, 700 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            5e-04
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Glow.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_mis_Mask_Color_6_8.tex"
                    0x5b249407: u8 = 2
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = 180
                    }
                    0xcd124686: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 1, 0.8 }
                    }
                }
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.1
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Conemesh_8"
                0x32741c32: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -70, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.0121
                            0.015
                            0.016
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -7, 0 }
                            { 0, -70, 0 }
                            { 0, -70, 0 }
                            { 0, -0, 0 }
                        }
                    }
                }
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -155, 100 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin62_Q_dash_half_sphere.scb"
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 0.7411765, 0.22352941, 1 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.013
                            0.015
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 0.79607844, 0.32156864, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 322
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x6b89d541: f32 = 20
                    0x1f661402: f32 = 10
                }
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xb4b427aa: f32 = 0
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Shyvana_Base_E_ErosionLoweRes.tex"
                    0xb0794a80: embed = 0x074f91dd {
                        0xb4b427aa: vec4 = { 1, 0, 0, 0 }
                    }
                    0x2b32227b: u8 = 0
                }
                0x6563bee8: u8 = 1
                0x37ddb774: flag = true
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 90, 0 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1.7, 5, 1.7 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.012
                            0.015
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1.2, 1.2, 1.3 }
                            { 1.2, 1.2, 1.3 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Shared/Particles/3026_Items_Streaks.tex"
                0xcfb707de: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0, 0.55 }
                }
                0xb9198a2a: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { -0.25, 0.5 }
                }
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 0.25, 3 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            0.5
                        }
                        0x34474c3b: list[vec2] = {
                            { 0.25, 6 }
                            { 0.25, 6 }
                            { 0.25, 6 }
                        }
                    }
                }
                0xeddebb48: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 1, -1.5 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.5
                            1
                        }
                        0x34474c3b: list[vec2] = {
                            { 1, -1.5 }
                            { 1, -0.75 }
                            { 1, -1.5 }
                        }
                    }
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Yone_Skin26_Air_Swoosh.tex"
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = 180
                    }
                    0xcd124686: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 3, 1 }
                    }
                    0x32356474: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 0, 5 }
                    }
                }
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.1
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Conemesh_10"
                0x32741c32: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -70, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.0121
                            0.015
                            0.016
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -7, 0 }
                            { 0, -70, 0 }
                            { 0, -70, 0 }
                            { 0, -0, 0 }
                        }
                    }
                }
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -155, 100 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin62_Q_dash_half_sphere.scb"
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 0.83137256, 0.40392157, 0.61960787 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.013
                            0.015
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 0.79607844, 0.32156864, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 322
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x6b89d541: f32 = 20
                    0x1f661402: f32 = 10
                }
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xb4b427aa: f32 = 0
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Shyvana_Base_E_ErosionLoweRes.tex"
                    0xb0794a80: embed = 0x074f91dd {
                        0xb4b427aa: vec4 = { 1, 0, 0, 0 }
                    }
                    0x2b32227b: u8 = 0
                }
                0x6563bee8: u8 = 1
                0x37ddb774: flag = true
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 90, 0 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1.7, 5, 1.7 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.012
                            0.015
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1.2, 1.2, 1.3 }
                            { 1.2, 1.2, 1.3 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Shared/Particles/3026_Items_Streaks.tex"
                0xcfb707de: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0, 0.55 }
                }
                0xb9198a2a: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { -0.25, 0.5 }
                }
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 0, 3 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            0.5
                        }
                        0x34474c3b: list[vec2] = {
                            { 0, 6 }
                            { 0, 6 }
                            { 0, 6 }
                        }
                    }
                }
                0xeddebb48: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 1, -1.5 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.5
                            1
                        }
                        0x34474c3b: list[vec2] = {
                            { 1, -1.5 }
                            { 1, -0.75 }
                            { 1, -1.5 }
                        }
                    }
                }
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.05
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1.2
                }
                0x2431d42c: option[f32] = {
                    2
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "shockwaves_out5"
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -1700, 0 }
                }
                0x8275da98: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 10, 0 }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0, 100 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_Splash_1_002.scb"
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.7000076 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.6431373, 0.827451, 0.9529412, 1 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.09374067
                            0.22703832
                            0.69844985
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.6431373, 0.827451, 0.9529412, 0 }
                            { 0.6431373, 0.827451, 0.9529412, 0.78547853 }
                            { 0.6431373, 0.827451, 0.9529412, 0.3257918 }
                            { 0.6431373, 0.827451, 0.9529412, 0.09722295 }
                            { 0.6431373, 0.827451, 0.9529412, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 900
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x1f661402: f32 = 80
                }
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                0.1388889
                                0.5148148
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0.1
                                0.18187252
                                0.70956177
                                2
                            }
                        }
                    }
                    0x2244caa3: f32 = 0.15
                    0x7c7970d8: f32 = 1
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_6655_Items_stack_3.tex"
                    0xb0794a80: embed = 0x074f91dd {
                        0xb4b427aa: vec4 = { 1, 0, 0, 0 }
                    }
                }
                0x3c91cebd: bool = true
                0x6563bee8: u8 = 1
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 1, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0
                                    360
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                0x712b01bd: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -3, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.35
                            0.5
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -3, 0 }
                            { 0, -0.3, 0 }
                            { 0, -0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 100, 60, 100 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.34444445
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 1.1, 1.1, 1.1 }
                            { 1.4, 2, 1.4 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_T2_dea_55.tex"
                0x86a84509: vec2 = { 0.5, 1 }
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { -2, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.30370373
                            0.5
                        }
                        0x34474c3b: list[vec2] = {
                            { -4, 0 }
                            { -0.79402393, 0 }
                            { -0, 0 }
                        }
                    }
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_splash_ring_1_01_1.tex"
                    0xcd124686: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 1, -1.5 }
                    }
                    0x32356474: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { -1, 0.3 }
                        0xbc037de7: pointer = 0x2e0ea245 {
                            0x5d68eeb5: list[f32] = {
                                0
                                0.2
                                1
                            }
                            0x34474c3b: list[vec2] = {
                                { -1, 0.3 }
                                { -1, 0 }
                                { -1, 0 }
                            }
                        }
                    }
                }
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.05
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.85
                }
                0x2431d42c: option[f32] = {
                    2
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "shockwaves_out6"
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -700, 0 }
                }
                0x8275da98: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 10, 0 }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 100, 100 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_Splash_1_002.scb"
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.6 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.6431373, 0.827451, 0.9529412, 1 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.09374067
                            0.22703832
                            0.69844985
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.6431373, 0.827451, 0.9529412, 0 }
                            { 0.6431373, 0.827451, 0.9529412, 1 }
                            { 0.6431373, 0.827451, 0.9529412, 0.3257918 }
                            { 0.6431373, 0.827451, 0.9529412, 0.09722295 }
                            { 0.6431373, 0.827451, 0.9529412, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 900
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x1f661402: f32 = 80
                }
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                0.1388889
                                0.5148148
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0.1
                                0.18187252
                                0.70956177
                                2
                            }
                        }
                    }
                    0x2244caa3: f32 = 0.15
                    0x7c7970d8: f32 = 1
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Irelia_Skin18_Q_Erode.tex"
                    0xb0794a80: embed = 0x074f91dd {
                        0xb4b427aa: vec4 = { 1, 0, 0, 0 }
                    }
                }
                0x3c91cebd: bool = true
                0x6563bee8: u8 = 1
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 1, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0
                                    360
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                0x712b01bd: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, 0.5, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.35
                            0.5
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0.5, 0 }
                            { 0, 0.05, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 65, 60, 65 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.34444445
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 1.02, 1.1, 1.02 }
                            { 1.4, 2, 1.4 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_T2_dea_55.tex"
                0x86a84509: vec2 = { 0.5, 1 }
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { -2, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.30370373
                            0.5
                        }
                        0x34474c3b: list[vec2] = {
                            { -4, 0 }
                            { -0.79402393, 0 }
                            { -0, 0 }
                        }
                    }
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_splash_ring_1_01_1.tex"
                    0xcd124686: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 1, -1.5 }
                    }
                    0x32356474: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { -1, 0.2 }
                        0xbc037de7: pointer = 0x2e0ea245 {
                            0x5d68eeb5: list[f32] = {
                                0
                                0.2
                                1
                            }
                            0x34474c3b: list[vec2] = {
                                { -1, 0.2 }
                                { -1, 0 }
                                { -1, 0 }
                            }
                        }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Missle18"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, -50, 100 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0x8c41a32e: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skn"
                        0x90595a15: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skl"
                    }
                }
                0xfa784eab: u8 = 1
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.012
                            0.015
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 102
                0x67b5d729: vec2 = { -1, -100 }
                0xb5158067: flag = true
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -95, 180, 0 }
                }
                0x712b01bd: embed = 0x6ccc7f03 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.002
                            0.01
                            0.014
                            0.018
                            0.019
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 4, 4, 4 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.004
                            0.012
                            0.014
                            0.016
                            0.02
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.0053098, 1.0053098, 1.0053098 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 0.2 }
                            { 0.5, 0.5, 1.25 }
                            { 1.2, 1.2, 1.2 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_R_mis_globefish.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Missle19"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, -50, 100 }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -2, 0, 0 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_Splash_1_004.scb"
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 0, 0, 1 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.014
                            0.018
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 801
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x6b89d541: f32 = 20
                    0x1f661402: f32 = 10
                }
                0x67b5d729: vec2 = { -1, -100 }
                0x6563bee8: u8 = 1
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -95, 180, 0 }
                }
                0x712b01bd: embed = 0x6ccc7f03 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.002
                            0.01
                            0.014
                            0.018
                            0.019
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 4, 4, 4 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.004
                            0.012
                            0.014
                            0.016
                            0.02
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.0053098, 1.0053098, 1.0053098 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 0.2 }
                            { 0.5, 0.5, 1.25 }
                            { 1.2, 1.2, 1.2 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_mis_Mask_Color_6_011.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Shared/Particles/3026_Items_Noise_02.tex"
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Missle20"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, -50, 100 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0x8c41a32e: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skn"
                        0x90595a15: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skl"
                    }
                }
                0xfa784eab: u8 = 1
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.012
                            0.015
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 102
                0x67b5d729: vec2 = { -1, -100 }
                0xb5158067: flag = true
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -95, 180, 0 }
                }
                0x712b01bd: embed = 0x6ccc7f03 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.002
                            0.01
                            0.014
                            0.018
                            0.019
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 4, 4, 4 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.004
                            0.012
                            0.014
                            0.016
                            0.02
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.0053098, 1.0053098, 1.0053098 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 0.2 }
                            { 0.5, 0.5, 1.25 }
                            { 1.2, 1.2, 1.2 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_R_mis_globefish_3_1.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 50
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Missle22"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, -50, 100 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0x8c41a32e: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skn"
                        0x90595a15: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skl"
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.6862745, 0.6862745, 0.6862745, 1 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.012
                            0.015
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 103
                0x67b5d729: vec2 = { -1, -100 }
                0xb5158067: flag = true
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -95, 180, 0 }
                }
                0x712b01bd: embed = 0x6ccc7f03 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.002
                            0.01
                            0.014
                            0.018
                            0.019
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 4, 4, 4 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.004
                            0.012
                            0.014
                            0.016
                            0.02
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.0053098, 1.0053098, 1.0053098 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 0.2 }
                            { 0.5, 0.5, 1.25 }
                            { 1.2, 1.2, 1.2 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_R_mis_globefish_3_1.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_Mask_3_12.tex"
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.55
                }
                0x2431d42c: option[f32] = {
                    0.6
                }
                0x5212abee: option[f32] = {
                    50
                }
                0x50b7397d: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0.1, 0.1 }
                }
                0x3d25b8ce: string = "Trail_BG10"
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -100, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -100, 0 }
                        }
                    }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 25, 50, 100 }
                }
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 1500
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 800, 0, 0 }
                        }
                        0x0ea6d9c1: u8 = 1
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.4 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.9
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.15
                            0.25
                            0.4
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.23529412, 0.9882353, 1, 0 }
                            { 0.28000304, 0.77000076, 1, 0 }
                            { 0.30588236, 0.49019608, 1, 0 }
                            { 0.29411766, 0.48235294, 1, 0 }
                            { 0.2399939, 0.34000152, 1, 0 }
                            { 0.11764706, 0.1254902, 0.5647059, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 3
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    0x34bee0ea: f32 = 0.25
                    0x2244caa3: f32 = 0.25
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                0x6563bee8: u8 = 1
                0x3559e15b: flag = true
                0x27d40903: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 120, 1, 1 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.014
                            0.016
                            0.02
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 102, 0, 0 }
                            { 102, 1, 1 }
                            { 120, 0, 0 }
                            { 120, 0, 0 }
                            { 120, 0, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 0.5 }
                            { 0.3, 0.5, 0.5 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_08.tex"
                0x52010b69: vec2 = { 0.15, 0 }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.4
                }
                0x2431d42c: option[f32] = {
                    0.6
                }
                0x5212abee: option[f32] = {
                    50
                }
                0x50b7397d: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0.1, 0.1 }
                }
                0x3d25b8ce: string = "Trail_BG11"
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -30, 20, 100 }
                }
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 1500
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 450, 0, 0 }
                        }
                        0x0ea6d9c1: u8 = 1
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.4 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.9
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.15
                            0.35
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 0.30980393, 0.49411765, 0 }
                            { 0.8235294, 0.28627452, 1, 0 }
                            { 0.5803922, 0.2784314, 1, 0 }
                            { 0.37000075, 0.3100023, 1, 0 }
                            { 0.023529412, 0.23529412, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 3
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xb4b427aa: f32 = 0
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    0x34bee0ea: f32 = 0.25
                    0x2244caa3: f32 = 0.25
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                0x6563bee8: u8 = 1
                0x3559e15b: flag = true
                0x27d40903: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 105, 1, 1 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.014
                            0.016
                            0.02
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 89.25, 0, 0 }
                            { 89.25, 1, 1 }
                            { 105, 0, 0 }
                            { 105, 0, 0 }
                            { 105, 0, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.8, 1, 1 }
                            { 1, 1, 1 }
                            { 0.4, 0.2, 0.2 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_09.tex"
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 0.05, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 0.05, 0 }
                        }
                    }
                }
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.05
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 16
                    0xbc037de7: pointer = 0xfe064c88 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.018
                            0.025
                        }
                        0x34474c3b: list[f32] = {
                            8
                            16
                            16
                        }
                    }
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.55
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.2
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            0.55
                        }
                    }
                }
                0x5212abee: option[f32] = {
                    50
                }
                0x3d25b8ce: string = "Swirls"
                0xb9516a6f: u8 = 3
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -350, 0 }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, 0, 100 }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -90, 0 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin13_R_CometSwirlMesh.scb"
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.14901961, 0.92941177, 1, 1 }
                            { 0.16470589, 0.5411765, 1, 1 }
                            { 0.023529412, 0.05490196, 0.36862746, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 40
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                0.5
                            }
                        }
                    }
                    0x5da05f9b: string = "ASSETS/Shared/Particles/Base_SmokeErosionT.tex"
                    0xb0794a80: embed = 0x074f91dd {
                        0xb4b427aa: vec4 = { 0, 1, 0, 0 }
                    }
                }
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 90, 1, 0 }
                }
                0x1d779e6a: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 50, 0 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1.4, 1.4, 1.3 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 1.4, 1.4, 1.3 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1.8, 1.8, 1.8 }
                            { 2.8, 2.8, 2.8 }
                            { 4, 4, 4 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_mis_Mask_Color_6_01.tex"
                0xb9198a2a: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 1, 1 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -0.5
                                    0.5
                                }
                            }
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -0.5
                                    0.5
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
            }
        }
        0xfd01a9d3: f32 = 1e+05
        0xecf1c6bc: string = "Jinx_Skin69_R_Mis"
        0xe7638138: string = "Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_R_Mis"
        0x5a6a73e2: string = "Play_sfx_Jinx_JinxR_missilelaunch"
        0x9c677a2c: u16 = 213
        0x1d369c29: hash = 0x1149b587
    }
    0x3675053a = 0x45cd899f {
        0x868eb76a: list[pointer] = {
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 24
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.6
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            24
                        }
                    }
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.8
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            0.8
                        }
                    }
                }
                0x3d25b8ce: string = "Basic"
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -5, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -5, 0 }
                        }
                    }
                }
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    0x9c677a2c: u8 = 1
                    0x23a0d95c: vec3 = { 10, 20, 15 }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -4, 0, 5 }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.7019608, 0.9098039, 1, 1 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.7019608, 0.9098039, 1, 1 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.3095499
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 901
                0xb99310f4: u8 = 0
                0xcb13aff1: f32 = -2
                0x37ddb774: flag = true
                0x3559e15b: flag = true
                0xdddde180: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    360
                                    0
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                0x2ae335b2: flag = false
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 15, 10, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.2
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 15, 10, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.44716242
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.49839142, 0, 0 }
                            { 0.6608579, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Nidalee_Skin29_egoprestige_speark.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_rainbow.tex"
                    0x32356474: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 0, 1.5 }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 60
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.5
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            0.5
                        }
                    }
                }
                0x3d25b8ce: string = "Basic1"
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -20, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -20, 0 }
                        }
                    }
                }
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    0x9c677a2c: u8 = 1
                    0x23a0d95c: vec3 = { 5, 20, 15 }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -8, -5, 5 }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.27041095
                            0.5
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.15294118, 0.16862746, 1, 0 }
                            { 0.13333334, 0.1764706, 1, 1 }
                            { 0.29411766, 0.90588236, 1, 1 }
                            { 0.1254902, 0.35686275, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 901
                0xb99310f4: u8 = 0
                0xcb13aff1: f32 = -2
                0x37ddb774: flag = true
                0x3559e15b: flag = true
                0xdddde180: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    360
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                0x2ae335b2: flag = false
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 4, 10, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.3
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 4, 10, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.44716242
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.49839142, 0, 0 }
                            { 0.6608579, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Dance_Sparks.tex"
            }
        }
        0xecf1c6bc: string = "Jinx_Skin69_Idle_Flicker"
        0xe7638138: string = "Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Idle_Flicker"
        0xf55e1472: bool = true
        0x1d369c29: hash = 0x3675053a
    }
    0x3cdb5416 = 0x45cd899f {
        0x868eb76a: list[pointer] = {
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.4
                }
                0x2431d42c: option[f32] = {
                    0.5
                }
                0x5212abee: option[f32] = {
                    2
                }
                0x3d25b8ce: string = "TrailBlend2"
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 20, 0 }
                }
                0x007b14f6: pointer = 0x5705625a {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 300, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.5000076 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.05
                            0.8
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.5000076 }
                            { 1, 1, 1, 0.5000076 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.86999315 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.2
                            0.3
                            0.60182154
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.27450982, 0.78431374, 1, 0 }
                            { 0.28000304, 0.6, 1, 0.34799725 }
                            { 0.25882354, 0.45490196, 1, 0.7232884 }
                            { 0.27450982, 0.38039216, 0.9882353, 0.573172 }
                            { 0.27450982, 0.23529412, 0.84313726, 0.2968212 }
                            { 0.29411766, 0.18039216, 0.6313726, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = -2
                0x3559e15b: flag = true
                0x676949a1: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 35, 1, 1 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.6, 1, 1 }
                            { 0.2, 1, 1 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Q_Trail_fill.tex"
                0xcfb707de: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0.3, 0 }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.2
                }
                0x2431d42c: option[f32] = {}
                0x5212abee: option[f32] = {
                    2
                }
                0x3d25b8ce: string = "TrailAdd1"
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 320, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.05
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.15
                            0.35
                            0.5
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.2784314, 0.8784314, 1, 0 }
                            { 0.2784314, 0.78431374, 1, 1 }
                            { 0.2509804, 0.4862745, 1, 1 }
                            { 0.26999313, 0.37000075, 1, 0.5000076 }
                            { 0.4, 0.2, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 2
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x1f661402: f32 = 50
                }
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 23, 50, 50 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 1.5 }
                            { 0.1, 1.8, 1.8 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_BA_03.tex"
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 1, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.03
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "DarkBG"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -45, 0 }
                }
                0x007b14f6: pointer = 0x4beb81fd {}
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.09803922, 0.5647059, 1, 0.7019608 }
                }
                0xb99310f4: u8 = 0
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0, 90 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 90, 80, 0 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/MissFortune_Skin69_MisLead_Mask.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/MissFortune_Skin69_E_Screen_Flames_Soft.tex"
                    0xcd124686: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 2, 1 }
                    }
                    0x32356474: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 0, -3 }
                    }
                }
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.03
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 5
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "bullets3"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {}
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Mis_Hand_grenade.scb"
                    }
                    0xd49fb9fe: bool = true
                    0xc535c0ef: bool = true
                }
                0xfa784eab: u8 = 3
                0x7b7a7318: i16 = 80
                0x3559e15b: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 180, 90 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 3.2, 2, 2.2 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Q_Mis_Thorn_2.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.2
                }
                0x2431d42c: option[f32] = {}
                0x5212abee: option[f32] = {
                    2
                }
                0x3d25b8ce: string = "TrailAdd7"
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 320, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.05
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.15
                            0.35
                            0.5
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.2784314, 0.8784314, 1, 0 }
                            { 0.25882354, 0.6431373, 1, 0.8509804 }
                            { 0.20392157, 0.54901963, 1, 0.67058825 }
                            { 0.22999924, 0.26999313, 1, 0.42999923 }
                            { 0.2, 0.14509805, 0.6117647, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 1
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x1f661402: f32 = 50
                }
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 23, 50, 50 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.1, 1.8, 1.8 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_BA_03.tex"
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 1, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.4
                }
                0x2431d42c: option[f32] = {
                    0.5
                }
                0x5212abee: option[f32] = {
                    2
                }
                0x3d25b8ce: string = "TrailBlend4"
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -200, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -200, 0 }
                        }
                    }
                }
                0x007b14f6: pointer = 0x5705625a {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 500, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.7000076 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.05
                            0.8
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.12
                            0.55
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.21568628, 0.4509804, 1, 0 }
                            { 0.34000152, 0.40999466, 1, 0.85999846 }
                            { 0.3100023, 0.2899977, 0.8200046, 0.6200046 }
                            { 0.3137255, 0.13725491, 0.5647059, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = -4
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0.2
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    0x34bee0ea: f32 = 0.25
                    0x2244caa3: f32 = 0.25
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                0x3559e15b: flag = true
                0x676949a1: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 65, 1, 1 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.4
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.7, 0.7, 0.7 }
                            { 1, 1, 1 }
                            { 1.3, 1, 1 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Aurora_Skin20_Comet_Trail_01.tex"
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 0.3, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 0.3, 0 }
                        }
                    }
                }
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.03
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1.5
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "FlameGlow2"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 25, 0 }
                }
                0x007b14f6: pointer = 0x4beb81fd {}
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.5000076 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.7000076 }
                }
                0x7b7a7318: i16 = 150
                0xb99310f4: u8 = 0
                0x6563bee8: u8 = 1
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 100, 90, 0 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin62_Alpha_Backdrop.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_splash_ring_Mask_2_01.tex"
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = -90
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.3
                }
                0x2431d42c: option[f32] = {
                    0.2
                }
                0x5212abee: option[f32] = {
                    2
                }
                0x3d25b8ce: string = "TrailAdd8"
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 400, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.919997 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.8
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.919997 }
                            { 1, 1, 1, 0.919997 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.35
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.85882354, 0.5254902, 1, 0.4 }
                            { 0.28235295, 0.02745098, 0.40784314, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 50
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x1f661402: f32 = 50
                }
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 80, 50, 50 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.5
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.6, 1, 1 }
                            { 0.3, 1, 1 }
                            { 0.15, 1, 1 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_E_Trail_01.tex"
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 0.5, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 0.5, 0 }
                        }
                    }
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Radialring_01_04113.tex"
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x5212abee: option[f32] = {
                    1.85
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "feather1"
                0xb9516a6f: u8 = 3
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0.01, 0 }
                }
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -30, 0 }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.4 }
                }
                0x7b7a7318: i16 = -50
                0xb99310f4: u8 = 0
                0xddfca826: flag = true
                0x3559e15b: flag = true
                0xe09d5ebb: flag = true
                0x8d2e2474: flag = true
                0x7ad984a5: f32 = 0.001
                0xebd44083: f32 = 1.5
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 100, 25, 1.26 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Soraka_ball32_02.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_mis_Mask_Color_6_8.tex"
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = 180
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 28
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            28
                        }
                    }
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.5
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.35
                                    1.5
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            0.5
                        }
                    }
                }
                0x2431d42c: option[f32] = {
                    0.7
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x3d25b8ce: string = "STARS_BACKGROUND"
                0xb9516a6f: u8 = 3
                0x51433ef4: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 1, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 1, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 50, -10, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -0.2
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 50, -10, 0 }
                        }
                    }
                }
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    0x9c677a2c: u8 = 1
                    0x0dba4cb3: f32 = 10
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -50, -10 }
                }
                0xb56e8811: string = "ASSETS/Shared/Particles/15.tex"
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x2674b1b5: u8 = 3
                0x67b5d729: vec2 = { -1, -18 }
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 40, 65, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    0.9
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.3
                                    1
                                    2
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 40, 65, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin51_W_BightSpark.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 16
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1.2
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    0.7
                                    1.2
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            1.2
                        }
                    }
                }
                0x2431d42c: option[f32] = {
                    1
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x3d25b8ce: string = "SparklesFast1"
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 200, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.3
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 200, 0, 0 }
                        }
                    }
                }
                0x8275da98: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 5, 5, 5 }
                }
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -600, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -600, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    0x9c677a2c: u8 = 1
                    0x0dba4cb3: f32 = 10
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -10, -5 }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.9000076 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.6
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                            0.5
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0.9000076 }
                            { 0.192157, 1, 0.827451, 0.9000076 }
                            { 1, 0, 0.682353, 0.9000076 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.3
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.23921569, 0.8352941, 1, 1 }
                            { 0.24313726, 0.7607843, 1, 1 }
                            { 0.13725491, 0.30588236, 0.85490197, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = -10
                0x2674b1b5: u8 = 3
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x1f661402: f32 = 30
                }
                0x3559e15b: flag = true
                0xe09d5ebb: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 90, 0, 0 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 10, 35, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 10, 35, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.2
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.2, 2, 0 }
                            { 0.8, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Zeri_Skin10_Q_Bubble01.tex"
                0x1e67b0f1: u16 = 4
                0x86a84509: vec2 = { 2, 2 }
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.03
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 5
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "bullets8"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {}
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Mis_Hand_grenade.scb"
                    }
                    0xd49fb9fe: bool = true
                    0xc535c0ef: bool = true
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.2 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.7000076 }
                }
                0x7b7a7318: i16 = 81
                0x3559e15b: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 180, 90 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 3.2, 2, 2.2 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Q_Mis_Thorn_2.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 2
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Projected"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, -50, 0 }
                }
                0x007b14f6: pointer = 0x4beb81fd {}
                0xb56e8811: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/color-holdhalf.tex"
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 0.68000305, 0.22000457, 0.5000076 }
                }
                0x19bdf4df: u8 = 0
                0x3559e15b: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -90, 0, 0 }
                }
                0x2ae335b2: flag = false
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 305, 450, 450 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Glow.tex"
            }
        }
        0xecf1c6bc: string = "Jinx_Skin69_Q_RocketMis"
        0xe7638138: string = "Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Q_RocketMis"
        0x1d369c29: hash = 0x3cdb5416
    }
    0x4bf38663 = 0x45cd899f {
        0x868eb76a: list[pointer] = {
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 32
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            32
                        }
                    }
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.75
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            0.75
                        }
                    }
                }
                0x3d25b8ce: string = "Basic1"
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -10, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -10, 0 }
                        }
                    }
                }
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    0x9c677a2c: u8 = 1
                    0x23a0d95c: vec3 = { 8, 8, 15 }
                }
                0xfa784eab: u8 = 4
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.27041095
                            0.5
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.15294118, 0.16862746, 1, 0 }
                            { 0.13333334, 0.1764706, 1, 1 }
                            { 0.29411766, 0.90588236, 1, 1 }
                            { 0.1254902, 0.35686275, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 901
                0xb99310f4: u8 = 0
                0xcb13aff1: f32 = -2
                0x3559e15b: flag = true
                0x8d2e2474: flag = true
                0xdddde180: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    360
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 4, 10, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.3
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 4, 10, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.44716242
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.49839142, 0, 0 }
                            { 0.6608579, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Dance_Sparks.tex"
            }
        }
        0xecf1c6bc: string = "Jinx_Skin69_Idle_Header"
        0xe7638138: string = "Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Idle_Header"
        0xf55e1472: bool = true
        0x1d369c29: hash = 0x4bf38663
    }
    0x4d2e580e = 0x45cd899f {
        0x868eb76a: list[pointer] = {
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.35
                }
                0x2431d42c: option[f32] = {
                    0.2
                }
                0x5212abee: option[f32] = {
                    2
                }
                0x3d25b8ce: string = "TrailAdd"
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 400, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.8
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.4
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 0.4899977, 0.88000304, 0.4 }
                            { 0.28235295, 0.02745098, 0.40784314, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 50
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x1f661402: f32 = 50
                }
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 85, 50, 50 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.5
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.6, 1, 1 }
                            { 0.3, 1, 1 }
                            { 0.15, 1, 1 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_E_Trail_01.tex"
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 0.5, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 0.5, 0 }
                        }
                    }
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Radialring_01_04113.tex"
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 16
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1.2
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    0.7
                                    1.2
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            1.2
                        }
                    }
                }
                0x2431d42c: option[f32] = {
                    1
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x3d25b8ce: string = "SparklesFast"
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 200, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.3
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 200, 0, 0 }
                        }
                    }
                }
                0x8275da98: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 5, 5, 5 }
                }
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -600, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -600, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    0x9c677a2c: u8 = 1
                    0x0dba4cb3: f32 = 10
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -10, -5 }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.9000076 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.6
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                            0.5
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0.9000076 }
                            { 0.192157, 1, 0.827451, 0.9000076 }
                            { 1, 0, 0.682353, 0.9000076 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.3
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.23921569, 0.8352941, 1, 1 }
                            { 0.24313726, 0.7607843, 1, 1 }
                            { 0.13725491, 0.30588236, 0.85490197, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = -10
                0x2674b1b5: u8 = 3
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x1f661402: f32 = 30
                }
                0x3559e15b: flag = true
                0xe09d5ebb: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 90, 0, 0 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 10, 35, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 10, 35, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.2
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.2, 2, 0 }
                            { 0.8, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Zeri_Skin10_Q_Bubble01.tex"
                0x1e67b0f1: u16 = 4
                0x86a84509: vec2 = { 2, 2 }
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.03
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1.5
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "FlameGlow"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 30, 0 }
                }
                0x007b14f6: pointer = 0x4beb81fd {}
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.4 }
                }
                0x7b7a7318: i16 = 150
                0xb99310f4: u8 = 0
                0x6563bee8: u8 = 1
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 80, 100, 0 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin62_Alpha_Backdrop.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_splash_ring_Mask_2_01.tex"
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = -90
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x5212abee: option[f32] = {
                    1.85
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "feather"
                0xb9516a6f: u8 = 3
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0.01, 0 }
                }
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -30, 0 }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.4 }
                }
                0x7b7a7318: i16 = -50
                0xb99310f4: u8 = 0
                0xddfca826: flag = true
                0x3559e15b: flag = true
                0xe09d5ebb: flag = true
                0x8d2e2474: flag = true
                0x7ad984a5: f32 = 0.001
                0xebd44083: f32 = 1.5
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 100, 25, 1.26 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Soraka_ball32_02.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_mis_Mask_Color_6_8.tex"
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = 180
                    }
                }
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.03
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 2
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "FrontWaveBLUE"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 60, 0 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/MissFortune_Skin21_RQ_Mesh_Core.scb"
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 0.7600061, 0.34999618, 0.6 }
                }
                0x7b7a7318: i16 = 15
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 360, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 360, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1, 2.3, 1 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/MissFortune_Skin21_BA_9571.tex"
                0xb9198a2a: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0, 0.1 }
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/MissFortune_Skin21_Dance_Einstein_01_mult.tex"
                    0xcd124686: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 2, 1 }
                    }
                    0x22c3cf3e: embed = 0x6bcc7d70 {
                        0xb4b427aa: vec2 = { 0, -3 }
                        0xbc037de7: pointer = 0x2e0ea245 {
                            0x5d68eeb5: list[f32] = {
                                0
                            }
                            0x34474c3b: list[vec2] = {
                                { 0, -3 }
                            }
                        }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.4
                }
                0x2431d42c: option[f32] = {
                    0.1
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x50b7397d: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0.1, 0.1 }
                }
                0x3d25b8ce: string = "Trail_BG"
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -200, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -200, 0 }
                        }
                    }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -5, -20, 0 }
                }
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 1500
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 780, 0, 0 }
                        }
                        0x0ea6d9c1: u8 = 1
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.5000076 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.9
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.5000076 }
                            { 1, 1, 1, 0.5000076 }
                            { 1, 1, 1, 0.5000076 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.15
                            0.3
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.21568628, 0.7254902, 1, 0 }
                            { 0.13333334, 0.46666667, 1, 0.6117647 }
                            { 0.5400015, 0.17000076, 1, 0.34000152 }
                            { 0.77999544, 0.11000229, 1, 0.2 }
                            { 0.64705884, 0.24313726, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 7
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    0x34bee0ea: f32 = 0.25
                    0x2244caa3: f32 = 0.25
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 70, 1, 1 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.85, 1, 0.5 }
                            { 0.9, 1, 1 }
                            { 0.4, 0.5, 0.5 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Mis_music_1_01_13.tex"
                0x52010b69: vec2 = { -0.2, 0 }
                0xeddebb48: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { -1, 1 }
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/W_Mis_Water_1_01111.tex"
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = 90
                    }
                    0xcd124686: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 1, 100 }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.4
                }
                0x2431d42c: option[f32] = {
                    0.1
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x50b7397d: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0.1, 0.1 }
                }
                0x3d25b8ce: string = "Trail_BG1"
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -200, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -200, 0 }
                        }
                    }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -5, -20, 0 }
                }
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 1500
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 780, 0, 0 }
                        }
                        0x0ea6d9c1: u8 = 1
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.8899977, 0.46999314, 1, 0.3100023 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.9
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.8899977, 0.46999314, 1, 0 }
                            { 0.8899977, 0.46999314, 1, 0.3100023 }
                            { 0.8899977, 0.46999314, 1, 0.3100023 }
                            { 0.8899977, 0.46999314, 1, 0.3100023 }
                            { 0.8899977, 0.46999314, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.7000076 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.15
                            0.3
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.12627588 }
                            { 1, 1, 1, 0.4611815 }
                            { 0.5100023, 0.2, 0.8899977, 0.08399878 }
                            { 0.34509805, 0.105882354, 0.6156863, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 6
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    0x34bee0ea: f32 = 0.25
                    0x2244caa3: f32 = 0.25
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 90, 1, 1 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.85, 1, 0.5 }
                            { 0.9, 1, 1 }
                            { 0.4, 0.5, 0.5 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Mis_music_1_01_13.tex"
                0x52010b69: vec2 = { -0.2, 0 }
                0xeddebb48: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { -1, 1 }
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Caitlyn_Skin51_AnimeShapes061.tex"
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.25
                }
                0x2431d42c: option[f32] = {
                    0.1
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x50b7397d: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0.1, 0.1 }
                }
                0x3d25b8ce: string = "Trail_BG2"
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -50, 0, 0 }
                }
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 1500
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 450, 0, 0 }
                        }
                        0x0ea6d9c1: u8 = 1
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.4 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.9
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.15
                            0.3
                            0.65
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.73333335, 0.3647059, 1, 0 }
                            { 0.6200046, 0.14999619, 1, 0.30000764 }
                            { 0.39000535, 0.20999466, 1, 0.59000534 }
                            { 0.2, 0.30000764, 0.8399939, 0.22999924 }
                            { 0.05882353, 0.21960784, 0.5647059, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 7
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xb4b427aa: f32 = 0
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    0x34bee0ea: f32 = 0.25
                    0x2244caa3: f32 = 0.25
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -100, 1, 1 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.9, 1, 1 }
                            { 1, 1, 1 }
                            { 0.4, 0.2, 0.2 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Mis_music_1_01_14.tex"
                0x52010b69: vec2 = { 0.25, 0 }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/W_Mis_Water_1_01111.tex"
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = 90
                    }
                    0xcd124686: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 1, 70 }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.25
                }
                0x2431d42c: option[f32] = {
                    0.1
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x50b7397d: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0.1, 0.1 }
                }
                0x3d25b8ce: string = "Trail_BG3"
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -50, 0, 0 }
                }
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 1500
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 450, 0, 0 }
                        }
                        0x0ea6d9c1: u8 = 1
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.6431373, 0.46666667, 1, 0.5019608 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.9
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.6431373, 0.46666667, 1, 0 }
                            { 0.6431373, 0.46666667, 1, 0.5019608 }
                            { 0.6431373, 0.46666667, 1, 0.5019608 }
                            { 0.6431373, 0.46666667, 1, 0.5019608 }
                            { 0.6431373, 0.46666667, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.7000076 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.15
                            0.3
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.16196255 }
                            { 1, 1, 1, 0.40627894 }
                            { 1, 1, 1, 0.08509897 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 6
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xb4b427aa: f32 = 0
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    0x34bee0ea: f32 = 0.25
                    0x2244caa3: f32 = 0.25
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -100, 1, 1 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.9, 1, 1 }
                            { 1, 1, 1 }
                            { 0.4, 0.2, 0.2 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Mis_music_1_01_14.tex"
                0x52010b69: vec2 = { 0.25, 0 }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_Mask_1_1_01.tex"
                }
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.03
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "DarkBG"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -45, 0 }
                }
                0x007b14f6: pointer = 0x4beb81fd {}
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.09803922, 0.5647059, 1, 0.7019608 }
                }
                0xb99310f4: u8 = 0
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0, 90 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 90, 80, 0 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/MissFortune_Skin69_MisLead_Mask.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/MissFortune_Skin69_E_Screen_Flames_Soft.tex"
                    0xcd124686: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 2, 1 }
                    }
                    0x32356474: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 0, -3 }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "SoftHead"
                0x0b6fe52f: vec3 = { 0, 0, 90 }
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -70, 0, 0 }
                }
                0x007b14f6: pointer = 0x4beb81fd {}
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.4627451, 0.32156864, 0.8862745, 1 }
                }
                0x7b7a7318: i16 = -10
                0xb99310f4: u8 = 0
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0, -90 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 30, 80, 0 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1.3, 1.3, 1 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/W_Beam_EPassive_03_1_1_2.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.4
                }
                0x2431d42c: option[f32] = {
                    0.5
                }
                0x5212abee: option[f32] = {
                    2
                }
                0x3d25b8ce: string = "TrailBlend2"
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 20, 0 }
                }
                0x007b14f6: pointer = 0x5705625a {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 300, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.7000076 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.05
                            0.8
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.2
                            0.3
                            0.60182154
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.27450982, 0.78431374, 1, 0 }
                            { 0.28000304, 0.6, 1, 0.4 }
                            { 0.25882354, 0.45490196, 1, 0.83137256 }
                            { 0.27450982, 0.38039216, 0.9882353, 0.65882355 }
                            { 0.34117648, 0.21568628, 0.84313726, 0.34117648 }
                            { 0.34117648, 0.105882354, 0.6313726, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = -2
                0x3559e15b: flag = true
                0x676949a1: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 32, 1, 1 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.6, 1, 1 }
                            { 0.2, 1, 1 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Q_Trail_fill.tex"
                0xcfb707de: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0.3, 0 }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.45
                }
                0x2431d42c: option[f32] = {
                    0.5
                }
                0x5212abee: option[f32] = {
                    2
                }
                0x3d25b8ce: string = "TrailBlend3"
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -200, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -200, 0 }
                        }
                    }
                }
                0x007b14f6: pointer = 0x5705625a {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 500, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.8899977 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.05
                            0.8
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.8899977 }
                            { 1, 1, 1, 0.8899977 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.12
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.21568628, 0.4509804, 1, 0 }
                            { 0.22745098, 0.49803922, 1, 0.85882354 }
                            { 0.28000304, 0.20999466, 0.8200046, 0.5499962 }
                            { 0.3137255, 0.13725491, 0.5647059, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = -4
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0.2
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    0x34bee0ea: f32 = 0.25
                    0x2244caa3: f32 = 0.25
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                0x3559e15b: flag = true
                0x676949a1: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 65, 1, 1 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.4
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.8, 0.7, 0.7 }
                            { 1, 1, 1 }
                            { 1.3, 1, 1 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Aurora_Skin20_Comet_Trail_01.tex"
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 0.3, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 0.3, 0 }
                        }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.2
                }
                0x2431d42c: option[f32] = {}
                0x5212abee: option[f32] = {
                    2
                }
                0x3d25b8ce: string = "TrailAdd6"
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 320, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.05
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.15
                            0.35
                            0.5
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.2784314, 0.8784314, 1, 0 }
                            { 0.2784314, 0.78431374, 1, 1 }
                            { 0.25490198, 0.47843137, 1, 1 }
                            { 0.26999313, 0.37000075, 1, 0.5000076 }
                            { 0.4, 0.2, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 2
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x1f661402: f32 = 50
                }
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 24, 50, 50 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 1.5 }
                            { 0.1, 1.8, 1.8 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_BA_03.tex"
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 1, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.2
                }
                0x2431d42c: option[f32] = {}
                0x5212abee: option[f32] = {
                    2
                }
                0x3d25b8ce: string = "TrailAdd7"
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 320, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.05
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.15
                            0.35
                            0.5
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.2784314, 0.8784314, 1, 0 }
                            { 0.25882354, 0.6431373, 1, 0.8509804 }
                            { 0.17999542, 0.33000687, 1, 0.66999316 }
                            { 0.22999924, 0.26999313, 1, 0.42999923 }
                            { 0.2, 0.14509805, 0.6117647, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 1
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x1f661402: f32 = 50
                }
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 24, 50, 50 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.1, 1.8, 1.8 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_BA_03.tex"
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 1, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 40
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.5
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.35
                                    1.5
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            0.5
                        }
                    }
                }
                0x2431d42c: option[f32] = {
                    1
                }
                0x5212abee: option[f32] = {
                    50
                }
                0x3d25b8ce: string = "STARS_BACKGROUND1"
                0xb9516a6f: u8 = 3
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 30, -50, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.1
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 30, -50, 0 }
                        }
                    }
                }
                0x32741c32: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0, 1 }
                }
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -100, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -100, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    0x9c677a2c: u8 = 1
                    0x0dba4cb3: f32 = 20
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 20, 0 }
                }
                0xb56e8811: string = "ASSETS/Shared/Particles/15.tex"
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.4
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 50
                0x2674b1b5: u8 = 3
                0x67b5d729: vec2 = { -1, -18 }
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 30, 30, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.1
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 30, 30, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.4
                            0.5
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.6, 1, 1 }
                            { 2, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Star01.tex"
                0x264afd39: u8 = 2
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.03
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 5
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "bullets2"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {}
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Mis_Hand_grenade.scb"
                    }
                    0xd49fb9fe: bool = true
                    0xc535c0ef: bool = true
                }
                0xfa784eab: u8 = 3
                0x7b7a7318: i16 = 80
                0x3559e15b: flag = true
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 180, 90 }
                }
                0x2ae335b2: flag = false
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 3.2, 2, 2.2 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Q_Mis_Thorn_2.tex"
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.03
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 5
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "bullets3"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {}
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Mis_Hand_grenade.scb"
                    }
                    0xd49fb9fe: bool = true
                    0xc535c0ef: bool = true
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.4 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.6 }
                }
                0x7b7a7318: i16 = 81
                0x3559e15b: flag = true
                0x8d2e2474: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 180, 90 }
                }
                0x2ae335b2: flag = false
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 3.2, 2, 2.2 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Q_Mis_Thorn_2.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 2
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Projected"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, -50, 0 }
                }
                0x007b14f6: pointer = 0x4beb81fd {}
                0xb56e8811: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/color-holdhalf.tex"
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 0.68000305, 0.22000457, 0.5000076 }
                }
                0x19bdf4df: u8 = 0
                0x3559e15b: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -90, 0, 0 }
                }
                0x2ae335b2: flag = false
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 350, 450, 450 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Glow.tex"
            }
        }
        0xecf1c6bc: string = "Jinx_Skin69_Q_RocketCritMis"
        0xe7638138: string = "Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Q_RocketCritMis"
        0x1d369c29: hash = 0x4d2e580e
    }
    0x6036fa79 = 0x45cd899f {
        0x868eb76a: list[pointer] = {
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.4
                }
                0x2431d42c: option[f32] = {
                    0.5
                }
                0x5212abee: option[f32] = {
                    2
                }
                0x3d25b8ce: string = "TrailBlend"
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 20, 0 }
                }
                0x007b14f6: pointer = 0x5705625a {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 300, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.5000076 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.05
                            0.8
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.5000076 }
                            { 1, 1, 1, 0.5000076 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.2
                            0.3
                            0.60182154
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.27450982, 0.78431374, 1, 0 }
                            { 0.28000304, 0.6, 1, 0.4 }
                            { 0.25882354, 0.45490196, 1, 0.83137256 }
                            { 0.27450982, 0.38039216, 0.9882353, 0.65882355 }
                            { 0.27450982, 0.23529412, 0.84313726, 0.34117648 }
                            { 0.29411766, 0.18039216, 0.6313726, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = -2
                0x3559e15b: flag = true
                0x676949a1: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 35, 1, 1 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.6, 1, 1 }
                            { 0.2, 1, 1 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Q_Trail_fill.tex"
                0xcfb707de: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0.3, 0 }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.4
                }
                0x2431d42c: option[f32] = {
                    0.5
                }
                0x5212abee: option[f32] = {
                    2
                }
                0x3d25b8ce: string = "TrailBlend1"
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -200, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -200, 0 }
                        }
                    }
                }
                0x007b14f6: pointer = 0x5705625a {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 500, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.7000076 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.05
                            0.8
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.12
                            0.55
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.21568628, 0.4509804, 1, 0 }
                            { 0.34000152, 0.40999466, 1, 0.85999846 }
                            { 0.3100023, 0.2899977, 0.8200046, 0.6200046 }
                            { 0.3137255, 0.13725491, 0.5647059, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = -4
                0xc4663005: pointer = 0x5e842b9b {
                    0xc6fbacd5: embed = 0x04300058 {
                        0xbc037de7: pointer = 0xfe064c88 {
                            0x5d68eeb5: list[f32] = {
                                0.2
                                1
                            }
                            0x34474c3b: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    0x34bee0ea: f32 = 0.25
                    0x2244caa3: f32 = 0.25
                    0x5da05f9b: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                0x3559e15b: flag = true
                0x676949a1: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 65, 1, 1 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.4
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.7, 0.7, 0.7 }
                            { 1, 1, 1 }
                            { 1.3, 1, 1 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Aurora_Skin20_Comet_Trail_01.tex"
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 0.3, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 0.3, 0 }
                        }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.2
                }
                0x2431d42c: option[f32] = {}
                0x5212abee: option[f32] = {
                    2
                }
                0x3d25b8ce: string = "TrailAdd1"
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 320, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.05
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.15
                            0.35
                            0.5
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.2784314, 0.8784314, 1, 0 }
                            { 0.2784314, 0.78431374, 1, 1 }
                            { 0.25490198, 0.47843137, 1, 1 }
                            { 0.26999313, 0.37000075, 1, 0.5000076 }
                            { 0.4, 0.2, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 2
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x1f661402: f32 = 50
                }
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 23, 50, 50 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 1.5 }
                            { 0.1, 1.8, 1.8 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_BA_03.tex"
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 1, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.2
                }
                0x2431d42c: option[f32] = {}
                0x5212abee: option[f32] = {
                    2
                }
                0x3d25b8ce: string = "TrailAdd2"
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 320, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.05
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.15
                            0.35
                            0.5
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.2784314, 0.8784314, 1, 0 }
                            { 0.25882354, 0.6431373, 1, 0.8509804 }
                            { 0.17999542, 0.33000687, 1, 0.66999316 }
                            { 0.22999924, 0.26999313, 1, 0.42999923 }
                            { 0.2, 0.14509805, 0.6117647, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 1
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x1f661402: f32 = 50
                }
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 23, 50, 50 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.1, 1.8, 1.8 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_BA_03.tex"
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { 1, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 28
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            28
                        }
                    }
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.5
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.35
                                    1.5
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            0.5
                        }
                    }
                }
                0x2431d42c: option[f32] = {
                    0.7
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x3d25b8ce: string = "STARS_BACKGROUND"
                0xb9516a6f: u8 = 3
                0x51433ef4: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 1, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 1, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 50, -10, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -0.2
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 50, -10, 0 }
                        }
                    }
                }
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    0x9c677a2c: u8 = 1
                    0x0dba4cb3: f32 = 10
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -50, -10 }
                }
                0xb56e8811: string = "ASSETS/Shared/Particles/15.tex"
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x2674b1b5: u8 = 3
                0x67b5d729: vec2 = { -1, -18 }
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 40, 65, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    0.9
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.3
                                    1
                                    2
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 40, 65, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin51_W_BightSpark.tex"
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.03
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1.5
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "FlameGlow"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 25, 0 }
                }
                0x007b14f6: pointer = 0x4beb81fd {}
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.5000076 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.7000076 }
                }
                0x7b7a7318: i16 = 150
                0xb99310f4: u8 = 0
                0x6563bee8: u8 = 1
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 100, 90, 0 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin62_Alpha_Backdrop.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_splash_ring_Mask_2_01.tex"
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = -90
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x5212abee: option[f32] = {
                    1.85
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "feather"
                0xb9516a6f: u8 = 3
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0.01, 0 }
                }
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -30, 0 }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.4 }
                }
                0x7b7a7318: i16 = -50
                0xb99310f4: u8 = 0
                0xddfca826: flag = true
                0x3559e15b: flag = true
                0xe09d5ebb: flag = true
                0x8d2e2474: flag = true
                0x7ad984a5: f32 = 0.001
                0xebd44083: f32 = 1.5
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 100, 25, 1.26 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Soraka_ball32_02.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_mis_Mask_Color_6_8.tex"
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = 180
                    }
                }
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.03
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 5
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "bullets"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {}
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Mis_Hand_grenade.scb"
                    }
                    0xd49fb9fe: bool = true
                    0xc535c0ef: bool = true
                }
                0xfa784eab: u8 = 3
                0x7b7a7318: i16 = 80
                0x3559e15b: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 180, 90 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 3.2, 2, 2.2 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Q_Mis_Thorn_2.tex"
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.03
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 5
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "bullets1"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {}
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Mis_Hand_grenade.scb"
                    }
                    0xd49fb9fe: bool = true
                    0xc535c0ef: bool = true
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.2 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.7000076 }
                }
                0x7b7a7318: i16 = 81
                0x3559e15b: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 180, 90 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 3.2, 2, 2.2 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Q_Mis_Thorn_2.tex"
            }
            0x09cde442 {
                0x22e763bc: f32 = 0.03
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "DarkBG"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -45, 0 }
                }
                0x007b14f6: pointer = 0x4beb81fd {}
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.09803922, 0.5647059, 1, 0.7019608 }
                }
                0xb99310f4: u8 = 0
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0, 90 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 90, 80, 0 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/MissFortune_Skin69_MisLead_Mask.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/MissFortune_Skin69_E_Screen_Flames_Soft.tex"
                    0xcd124686: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 2, 1 }
                    }
                    0x32356474: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 0, -3 }
                    }
                }
            }
        }
        0xecf1c6bc: string = "Jinx_Skin69_Q_RocketHurricaneMis"
        0xe7638138: string = "Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Q_RocketHurricaneMis"
        0x1d369c29: hash = 0x6036fa79
    }
    0x6f0938d5 = 0x45cd899f {
        0x868eb76a: list[pointer] = {
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 2
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3d25b8ce: string = "Flash3"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, 10, 15 }
                }
                0xb56e8811: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/color-rampdown.tex"
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.43529412, 0.2627451, 1, 1 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.5
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.43529412, 0.2627451, 1, 0 }
                            { 0.43529412, 0.2627451, 1, 1 }
                            { 0.43529412, 0.2627451, 1, 0 }
                        }
                    }
                }
                0x19bdf4df: u8 = 0
                0x67b5d729: vec2 = { -1, -16 }
                0x37ddb774: flag = true
                0x3559e15b: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    1
                                    360
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 15, 105, 105 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Glow.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 2
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3d25b8ce: string = "Flash4"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, 10, -10 }
                }
                0xb56e8811: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/color-rampdown.tex"
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.43529412, 0.2627451, 1, 1 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.5
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.43529412, 0.2627451, 1, 0 }
                            { 0.43529412, 0.2627451, 1, 1 }
                            { 0.43529412, 0.2627451, 1, 0 }
                        }
                    }
                }
                0x19bdf4df: u8 = 0
                0x67b5d729: vec2 = { -1, -16 }
                0x37ddb774: flag = true
                0x3559e15b: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    1
                                    360
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 15, 105, 105 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Glow.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = -1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "chain_beam6"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x007b14f6: pointer = 0x68753673 {
                    0xd45614c7: embed = 0x1fb8df09 {
                        0xfa870fed: vec3 = { 0, 7, -10 }
                        0xce1e03e5: vec3 = { -5, 0, -5 }
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { -1, 120, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.5000076 }
                }
                0x7b7a7318: i16 = 1
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 15, 0, 0 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_02.tex"
                0xcfb707de: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { -0.2, 0 }
                }
                0xb9198a2a: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 1, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0
                                    1
                                }
                            }
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Idle_Beam_Mult_1_01.tex"
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = -1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "chain_beam7"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x007b14f6: pointer = 0x68753673 {
                    0xd45614c7: embed = 0x1fb8df09 {
                        0xfa870fed: vec3 = { 0, 7, 15 }
                        0xce1e03e5: vec3 = { -5, 0, 20 }
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { -1, 120, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.5000076 }
                }
                0x7b7a7318: i16 = 1
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 15, 0, 0 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_02.tex"
                0xcfb707de: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { -0.2, 0 }
                }
                0xb9198a2a: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 1, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0
                                    1
                                }
                            }
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Idle_Beam_Mult_1_01.tex"
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = -1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "chain_beam11"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x007b14f6: pointer = 0x68753673 {
                    0xd45614c7: embed = 0x1fb8df09 {
                        0xfa870fed: vec3 = { 0, 7, 15 }
                        0xce1e03e5: vec3 = { -5, 0, 20 }
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { -1, 100, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.5000076 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 5, 0, 0 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin60_W_Glow_Trail.tex"
                0x968279e0: embed = 0x04300058 {
                    0xb4b427aa: f32 = 90
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Idle_Beam_Mult_1_01.tex"
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = -1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "chain_beam12"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x007b14f6: pointer = 0x68753673 {
                    0xd45614c7: embed = 0x1fb8df09 {
                        0xfa870fed: vec3 = { 0, 7, -10 }
                        0xce1e03e5: vec3 = { -5, 0, -5 }
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { -1, 100, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.5000076 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 5, 0, 0 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin60_W_Glow_Trail.tex"
                0x968279e0: embed = 0x04300058 {
                    0xb4b427aa: f32 = 90
                }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Idle_Beam_Mult_1_01.tex"
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 16
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.5
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.4
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            0.5
                        }
                    }
                }
                0x3d25b8ce: string = "Flash6"
                0xb9516a6f: u8 = 3
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 3, 3, 3 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -3
                                    1
                                }
                            }
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 3, 3, 3 }
                        }
                    }
                }
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    0x9c677a2c: u8 = 1
                    0x23a0d95c: vec3 = { 5, 15, 36 }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, -5, -10 }
                }
                0xb56e8811: string = "ASSETS/Characters/Jinx/Skins/Skin69/Particles/Seraphine_Skin69_Q_RainbowMult.tex"
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.5
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x19bdf4df: u8 = 0
                0xb99310f4: u8 = 0
                0x67b5d729: vec2 = { -1, -16 }
                0xcb13aff1: f32 = -2
                0x37ddb774: flag = true
                0x3559e15b: flag = true
                0xed87335c: flag = true
                0x8d2e2474: flag = true
                0xdddde180: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 26, 6, 6 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 26, 6, 6 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.3
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Star01.tex"
            }
        }
        0xecf1c6bc: string = "Jinx_Skin69_Idle_01Hover"
        0xe7638138: string = "Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Idle_01Hover"
        0xf55e1472: bool = true
        0x1d369c29: hash = 0x6f0938d5
    }
    0x73b3172a = 0x45cd899f {
        0x868eb76a: list[pointer] = {
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x3d25b8ce: string = "Grenade1"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0, -20 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_E_texmesh01.scb"
                    }
                }
                0xfa784eab: u8 = 3
                0x7b7a7318: i16 = 1000
                0x3f7567cd: pointer = 0x4112ea83 {
                    0x9137d3b8: f32 = 0
                }
                0x3559e15b: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -90, 0, -180 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1.2, 30, 30 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_E_texmesh01.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Grenade2"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.8509804, 0.30588236, 1, 0.3019608 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.60999465 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            0.8
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.60999465 }
                            { 1, 1, 1, 0.60999465 }
                            { 0.6509804, 0.6509804, 0.6509804, 0 }
                        }
                    }
                }
                0x19bdf4df: u8 = 0
                0xb99310f4: u8 = 0
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x1f661402: f32 = 30
                }
                0x3559e15b: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 45, 0, 0 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 120, 30, 30 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/3026_Items_ball32_02.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 10
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1
                                    1.5
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            1
                        }
                    }
                }
                0x2431d42c: option[f32] = {
                    1
                }
                0x5212abee: option[f32] = {
                    5
                }
                0x3d25b8ce: string = "PSmoke1"
                0xb9516a6f: u8 = 3
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 50, 0 }
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    0x9c677a2c: u8 = 1
                    0x23a0d95c: vec3 = { 54, 120, 57 }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 30, 0 }
                }
                0xb56e8811: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_E_BokehColor.tex"
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.5600061, 0.7600061, 1, 0.6 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.5600061, 0.7600061, 1, 0.6 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.93000686 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.3
                            0.5
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.93000686 }
                            { 1, 1, 1, 0.15810187 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 900
                0x2674b1b5: u8 = 3
                0x3559e15b: flag = true
                0xe09d5ebb: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                0x1d779e6a: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 90, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 90, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 70, 0.377, 0.377 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    0.9
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.2
                                    1
                                    1.5
                                }
                            }
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.2
                                    1.1
                                }
                            }
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.2
                                    1.1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 70, 0.377, 0.377 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0.7, 1, 1 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.7, 1, 1 }
                            { 0.7, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin69_LensGlow01.tex"
                0x1e67b0f1: u16 = 4
                0x86a84509: vec2 = { 2, 2 }
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin69_Rainbow01.tex"
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 12
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            12
                        }
                    }
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.8
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1.2
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            0.8
                        }
                    }
                }
                0x2431d42c: option[f32] = {
                    1
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x3d25b8ce: string = "SparklesFast"
                0xb9516a6f: u8 = 3
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 50, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 50, 0, 0 }
                        }
                    }
                }
                0x8275da98: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 5, 5, 5 }
                }
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -400, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.65
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -400, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    0x9c677a2c: u8 = 1
                    0x0dba4cb3: f32 = 10
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 50, -10 }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.7300069 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.3
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.3529412, 0.85882354, 1, 1 }
                            { 0.38431373, 0.7019608, 1, 1 }
                            { 0.19215687, 0.20392157, 1, 1 }
                        }
                    }
                }
                0x3559e15b: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 90, 0, 0 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 10, 35, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    1
                                    2
                                }
                            }
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 10, 35, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.2
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 2, 0 }
                            { 0.8, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/TahmKench_Skin30_BasicAttack_Bubble01.tex"
                0x9b111ae4: f32 = 5
                0x1e67b0f1: u16 = 4
                0x86a84509: vec2 = { 2, 2 }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.25
                }
                0x2431d42c: option[f32] = {
                    1
                }
                0x5212abee: option[f32] = {
                    0.5
                }
                0x3d25b8ce: string = "TrailBlend1"
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, 30, 0 }
                }
                0x007b14f6: pointer = 0x5705625a {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 400, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.8039216, 0.8509804, 1, 0.5019608 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            0.8
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.8039216, 0.8509804, 1, 0 }
                            { 0.8039216, 0.8509804, 1, 0.5019608 }
                            { 0.8039216, 0.8509804, 1, 0.5019608 }
                            { 0.8039216, 0.8509804, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.2
                            0.38907105
                            0.60182154
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.38431373, 0.9490196, 1, 0 }
                            { 0.34117648, 0.7490196, 1, 0.5921569 }
                            { 0.34117648, 0.48235294, 0.9372549, 1 }
                            { 0.30000764, 0.34999618, 0.8200046, 0.6599985 }
                            { 0.37254903, 0.21960784, 0.7607843, 0.3019608 }
                            { 0.22745098, 0.101960786, 0.49411765, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = -2
                0x3559e15b: flag = true
                0x676949a1: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 40, 1, 1 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.3, 0.2, 0.2 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Q_Trail_fill.tex"
                0xcfb707de: embed = 0x69dc3449 {
                    0xb4b427aa: vec2 = { 0.3, 0 }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.22
                }
                0x2431d42c: option[f32] = {
                    1
                }
                0x5212abee: option[f32] = {
                    0.5
                }
                0x3d25b8ce: string = "TrailAdd"
                0x3bf0b4ed: pointer = 0xee39916f {
                    0xe5f268dd: vec3 = { 0, 30, 0 }
                }
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 400, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.919997 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            0.8
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.919997 }
                            { 1, 1, 1, 0.919997 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.3
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.38039216, 0.85490197, 1, 0 }
                            { 0.020004578, 0.4599985, 1, 0.37999544 }
                            { 0.1882353, 0.2, 1, 0.56078434 }
                            { 0.25882354, 0.09803922, 0.6, 0.92156863 }
                            { 0.1764706, 0.023529412, 0.40784314, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = -2
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x1f661402: f32 = 50
                }
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 100, 50, 50 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            0.5
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.6, 0.6, 0.6 }
                            { 0.6, 1, 1 }
                            { 0.3, 1, 1 }
                            { 0.1, 1, 1 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_E_Trail_01.tex"
                0x52010b69: vec2 = { -1, 0 }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.15
                }
                0x2431d42c: option[f32] = {
                    1
                }
                0x5212abee: option[f32] = {
                    0.5
                }
                0x3d25b8ce: string = "TrailAdd1"
                0x3bf0b4ed: pointer = 0xee39916f {}
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 23, 0 }
                }
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 360, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.7000076 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.8
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.05
                            0.15
                            0.4
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 0.48235294, 0.13725491, 0 }
                            { 1, 0.7411765, 0.22745098, 1 }
                            { 0.17999542, 0.80999464, 1, 0.77000076 }
                            { 0.21960784, 0.53333336, 1, 0.4509804 }
                            { 0.2627451, 0.23921569, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 2
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x1f661402: f32 = 50
                }
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 20, 50, 50 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1.2, 11, 1.5 }
                            { 1, 1.8, 1.8 }
                            { 0.2, 1.8, 1.8 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_BA_03.tex"
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { -1, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { -1, 0 }
                        }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 16
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            16
                        }
                    }
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.7
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            0.7
                        }
                    }
                }
                0x2431d42c: option[f32] = {
                    0.6
                }
                0x5212abee: option[f32] = {
                    5
                }
                0x3d25b8ce: string = "PSmoke3"
                0xb9516a6f: u8 = 3
                0xfa41ab8d: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 10, 20, 10 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 10, 20, 10 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    0x9c677a2c: u8 = 1
                    0x0dba4cb3: f32 = 10
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 50.1, 0 }
                }
                0xb56e8811: string = "ASSETS/Shared/Particles/15.tex"
                0xfa784eab: u8 = 4
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.55
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 11
                0x6563bee8: u8 = 1
                0x3559e15b: flag = true
                0x27d40903: flag = true
                0xdddde180: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 20, 30, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.3
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 20, 30, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.4
                            0.6
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.6, 1, 1 }
                            { 2, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin62_EnergyMote.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Grenade4"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0, -20 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_E_texmesh01.scb"
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.6500038 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 1001
                0x3f7567cd: pointer = 0x4112ea83 {
                    0x9137d3b8: f32 = 0
                }
                0x3559e15b: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -90, 0, -180 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1.2, 30, 30 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_E_ShellMis0101.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Shared/Particles/Augment_Mercy_ChromaticGlaze_A.tex"
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 2
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2431d42c: option[f32] = {
                    0.4
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x3d25b8ce: string = "shineRing"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 20, 0 }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.75
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 962
                0xb99310f4: u8 = 0
                0x67b5d729: vec2 = { 1, 20 }
                0x6563bee8: u8 = 1
                0x3559e15b: flag = true
                0x27d40903: flag = true
                0xdddde180: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 360, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 120, 1, 1 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 120, 1, 1 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.257754
                            0.5080214
                            0.7497326
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.74817073, 0.74817073, 0.74817073 }
                            { 0.92317075, 0.9162045, 0.9162045 }
                            { 1, 1, 1 }
                            { 0.9060976, 0.91890246, 0.91890246 }
                            { 0.80792683, 0.80792683, 0.80792683 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Assets_1_369.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Caitlyn_Skin51_BA_Color03.tex"
                    0xedbcaa56: embed = 0x04300058 {
                        0xb4b427aa: f32 = 200
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 2
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2431d42c: option[f32] = {
                    0.4
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x3d25b8ce: string = "shineRing1"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 20, 0 }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 0.7137255, 0.25490198, 1 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.75
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 0.7137255, 0.25490198, 1 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 964
                0xb99310f4: u8 = 0
                0x67b5d729: vec2 = { 1, 20 }
                0x6563bee8: u8 = 1
                0x3559e15b: flag = true
                0x27d40903: flag = true
                0xdddde180: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 360, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 80, 1, 1 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.257754
                            0.5080214
                            0.7497326
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.74817073, 0.74817073, 0.74817073 }
                            { 0.92317075, 0.9162045, 0.9162045 }
                            { 1, 1, 1 }
                            { 0.9060976, 0.91890246, 0.91890246 }
                            { 0.80792683, 0.80792683, 0.80792683 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/BA_Hex_Indicator_1_01.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Caitlyn_Skin51_BA_Color03.tex"
                    0xedbcaa56: embed = 0x04300058 {
                        0xb4b427aa: f32 = 200
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Grenade6"
                0xb9516a6f: u8 = 3
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 0, -20 }
                }
                0x007b14f6: pointer = 0x8594e839 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xd467e8c0: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_E_texmesh01.scb"
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 0.77999544, 0.2500038, 0.9499962 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.65
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 0.77999544, 0.2500038, 0.9499962 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 1001
                0x3f7567cd: pointer = 0x4112ea83 {
                    0x9137d3b8: f32 = 0
                }
                0x3559e15b: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -90, 0, -180 }
                }
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1.2, 30, 30 }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_E_ShellMis03.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Shared/Particles/3026_Items_Noise_02.tex"
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = 45
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 200
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.15
                }
                0x2431d42c: option[f32] = {
                    1
                }
                0x5212abee: option[f32] = {
                    0.5
                }
                0x3d25b8ce: string = "TrailAdd3"
                0x3bf0b4ed: pointer = 0xee39916f {}
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 0, 23, 0 }
                }
                0x007b14f6: pointer = 0x287851b9 {
                    0x5e661fd4: embed = 0x00c2a390 {
                        0xac59cf4b: u8 = 1
                        0xee88201d: f32 = 2000
                        0x8c784fc7: embed = 0x68dc32b6 {
                            0xb4b427aa: vec3 = { 360, 0, 0 }
                        }
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0.6 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.1
                            0.8
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.6 }
                            { 1, 1, 1, 0.6 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0.05
                            0.15
                            0.4
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 0.40784314, 0.22745098, 0 }
                            { 1, 0.80784315, 0.23529412, 1 }
                            { 0.17999542, 0.80999464, 1, 0.7600061 }
                            { 0.22000457, 0.5300069, 1, 0.4 }
                            { 0.2627451, 0.23921569, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 1
                0xbfb0efdd: pointer = 0x1daa3fb0 {
                    0x1f661402: f32 = 50
                }
                0x3559e15b: flag = true
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 20, 50, 50 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 1.2, 1, 1.5 }
                            { 1, 1.8, 1.8 }
                            { 0.2, 1.8, 1.8 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_BA_03.tex"
                0x645e1b8b: embed = 0x6bcc7d70 {
                    0xb4b427aa: vec2 = { -1, 0 }
                    0xbc037de7: pointer = 0x2e0ea245 {
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec2] = {
                            { -1, 0 }
                        }
                    }
                }
            }
        }
        0xecf1c6bc: string = "Jinx_Skin69_E_Mis"
        0xe7638138: string = "Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_E_Mis"
        0x1d369c29: hash = 0x73b3172a
    }
    0xb9a5a107 = 0x45cd899f {
        0x868eb76a: list[pointer] = {
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = -1
                }
                0x2431d42c: option[f32] = {
                    0.15
                }
                0x42bd7f6b: flag = true
                0xa03664c8: pointer = 0xb520045a {
                    0x663f55e6: list[embed] = {
                        0x969aee94 {
                            0x9b0300f3: hash = 0x62333d7e
                        }
                    }
                }
                0x3d25b8ce: string = "Flash"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 15, 5, 5 }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.3
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 0.7100023, 0.13000686, 0.6 }
                            { 1, 1, 1, 1 }
                            { 0.8627451, 0.36078432, 1, 0.3019608 }
                            { 0.48235294, 0.13725491, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 150
                0xb99310f4: u8 = 0
                0x6563bee8: u8 = 1
                0x37ddb774: flag = true
                0x3559e15b: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 90, 90, 0 }
                }
                0x2ae335b2: flag = false
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1, 350, 350 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.42629483, 0, 0 }
                            { 1.5, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Camille_Skin44_Q_Hex_Indicator_1_1_007.tex"
            }
        }
        0xecf1c6bc: string = "Jinx_Skin69_Idle_Header_01"
        0xe7638138: string = "Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Idle_Header_01"
        0xf55e1472: bool = true
        0x1d369c29: hash = 0xb9a5a107
    }
    0xbaa5a29a = 0x45cd899f {
        0x868eb76a: list[pointer] = {
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = -1
                }
                0x2431d42c: option[f32] = {
                    0.15
                }
                0x42bd7f6b: flag = true
                0xa03664c8: pointer = 0xb520045a {
                    0x663f55e6: list[embed] = {
                        0x969aee94 {
                            0x9b0300f3: hash = 0x62333d7e
                        }
                    }
                }
                0x3d25b8ce: string = "Flash"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { -15, -5, -10 }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 1, 1, 0 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.3
                            0.6
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 0.7100023, 0.13000686, 0.6 }
                            { 1, 1, 1, 1 }
                            { 0.8627451, 0.36078432, 1, 0.3019608 }
                            { 0.48235294, 0.13725491, 1, 0 }
                        }
                    }
                }
                0x7b7a7318: i16 = 150
                0xb99310f4: u8 = 0
                0x6563bee8: u8 = 1
                0x37ddb774: flag = true
                0x3559e15b: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 125, 0, 0 }
                }
                0x2ae335b2: flag = false
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1, 350, 350 }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.2
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.42629483, 0, 0 }
                            { 1.5, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Camille_Skin44_Q_Hex_Indicator_1_1_007.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Caitlyn_Skin51_BA_Color03.tex"
                    0x33b8543e: embed = 0x04300058 {
                        0xb4b427aa: f32 = 1
                        0xbc037de7: pointer = 0xfe064c88 {
                            0xa7084719: list[pointer] = {
                                0x53a6c97e {
                                    0x40c351da: list[f32] = {
                                        0
                                        1
                                    }
                                    0xe44b7382: list[f32] = {
                                        -360
                                        1
                                    }
                                }
                            }
                            0x5d68eeb5: list[f32] = {
                                0
                            }
                            0x34474c3b: list[f32] = {
                                1
                            }
                        }
                    }
                }
            }
        }
        0xecf1c6bc: string = "Jinx_Skin69_Idle_Header_02"
        0xe7638138: string = "Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Idle_Header_02"
        0xf55e1472: bool = true
        0x1d369c29: hash = 0xbaa5a29a
    }
    0xf25b0b4a = 0x45cd899f {
        0x868eb76a: list[pointer] = {
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 24
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.6
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            24
                        }
                    }
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.8
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            0.8
                        }
                    }
                }
                0x3d25b8ce: string = "Basic7"
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -5, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -5, 0 }
                        }
                    }
                }
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    0x9c677a2c: u8 = 1
                    0x23a0d95c: vec3 = { 10, 20, 15 }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 4, 0, 0 }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.7019608, 0.9098039, 1, 1 }
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.7019608, 0.9098039, 1, 1 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.3095499
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 901
                0xb99310f4: u8 = 0
                0xcb13aff1: f32 = -2
                0x37ddb774: flag = true
                0x3559e15b: flag = true
                0xdddde180: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    360
                                    0
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                0x2ae335b2: flag = false
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 15, 10, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.2
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 15, 10, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.44716242
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.49839142, 0, 0 }
                            { 0.6608579, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Nidalee_Skin29_egoprestige_speark.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_rainbow.tex"
                    0x32356474: embed = 0x69dc3449 {
                        0xb4b427aa: vec2 = { 0, 1.5 }
                    }
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 60
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 0.5
                    0xbc037de7: pointer = 0xfe064c88 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[f32] = {
                            0.5
                        }
                    }
                }
                0x3d25b8ce: string = "Basic8"
                0xeb9a4e0f: embed = 0x6ccc7f03 {
                    0xb4b427aa: vec3 = { 0, -20, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 0, -20, 0 }
                        }
                    }
                }
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    0x9c677a2c: u8 = 1
                    0x23a0d95c: vec3 = { 5, 20, 15 }
                }
                0x563d4a22: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 8, -5, 0 }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {}
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.27041095
                            0.5
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 0.15294118, 0.16862746, 1, 0 }
                            { 0.13333334, 0.1764706, 1, 1 }
                            { 0.29411766, 0.90588236, 1, 1 }
                            { 0.1254902, 0.35686275, 1, 1 }
                        }
                    }
                }
                0x7b7a7318: i16 = 901
                0xb99310f4: u8 = 0
                0xcb13aff1: f32 = -2
                0x37ddb774: flag = true
                0x3559e15b: flag = true
                0xdddde180: flag = true
                0x5932ff9c: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 1, 0, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    360
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                0x2ae335b2: flag = false
                0xf0eb7084: embed = 0x68dc32b6 {
                    0xb4b427aa: vec3 = { 4, 10, 0 }
                    0xbc037de7: pointer = 0xacd81180 {
                        0xa7084719: list[pointer] = {
                            0x53a6c97e {
                                0x40c351da: list[f32] = {
                                    0
                                    1
                                }
                                0xe44b7382: list[f32] = {
                                    0.3
                                    1
                                }
                            }
                            0x53a6c97e {}
                            0x53a6c97e {}
                        }
                        0x5d68eeb5: list[f32] = {
                            0
                        }
                        0x34474c3b: list[vec3] = {
                            { 4, 10, 0 }
                        }
                    }
                }
                0xd4e17a53: embed = 0x68dc32b6 {
                    0xbc037de7: pointer = 0xacd81180 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.44716242
                            1
                        }
                        0x34474c3b: list[vec3] = {
                            { 0.49839142, 0, 0 }
                            { 0.6608579, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Dance_Sparks.tex"
            }
        }
        0xecf1c6bc: string = "Jinx_Skin69_Idle_Flicker_1"
        0xe7638138: string = "Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Idle_Flicker_1"
        0xf55e1472: bool = true
        0x1d369c29: hash = 0xf25b0b4a
    }
    0xfe2a7af7 = 0x45cd899f {
        0x868eb76a: list[pointer] = {
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = -1
                }
                0x5212abee: option[f32] = {
                    1
                }
                0x42bd7f6b: flag = true
                0x3d25b8ce: string = "Dark_Activate2"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x007b14f6: pointer = 0xa4aea2a5 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xdb63db58: list[hash] = {
                            0xed500a70
                        }
                        0xb1a2e185: list[hash] = {
                            0xed500a70
                        }
                    }
                }
                0xfa784eab: u8 = 1
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.81960785, 0.81960785, 0.81960785, 1 }
                }
                0x67b5d729: vec2 = { -1, -1 }
                0x3559e15b: flag = true
                0x2ae335b2: flag = false
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin69/Jinx_Skin69_Weapon_TX_CM.tex"
                0x2f2e99f2: pointer = 0xb097c1bd {
                    0x2f2e99f2: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Mask_1_3_02.tex"
                }
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3d25b8ce: string = "Dark_Activate3"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x007b14f6: pointer = 0xa4aea2a5 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xdb63db58: list[hash] = {
                            0xed500a70
                        }
                        0xb1a2e185: list[hash] = {
                            0xed500a70
                        }
                        0xe79da182: bool = true
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 1, 0.70980394, 0.24313726, 0.5294118 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.45
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0.30000764 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.30000764 }
                        }
                    }
                }
                0x7b7a7318: i16 = 14
                0x67b5d729: vec2 = { -1, -1 }
                0xcb13aff1: f32 = -1
                0x3559e15b: flag = true
                0x2ae335b2: flag = false
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Mask_1_3_03.tex"
            }
            0x09cde442 {
                0xae839c67: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x2a552694: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x3d25b8ce: string = "Dark_Activate5"
                0xca406316: embed = 0x04300058 {
                    0xb4b427aa: f32 = 1
                }
                0x007b14f6: pointer = 0xa4aea2a5 {
                    0x0d89732d: embed = 0x6a88780b {
                        0xdb63db58: list[hash] = {
                            0xed500a70
                        }
                        0xb1a2e185: list[hash] = {
                            0xed500a70
                        }
                        0xe79da182: bool = true
                    }
                }
                0xfa784eab: u8 = 4
                0x83cdeaa1: embed = 0x074f91dd {
                    0xb4b427aa: vec4 = { 0.33000687, 0.7100023, 1, 0.86999315 }
                }
                0x3d7e6258: embed = 0x074f91dd {
                    0xbc037de7: pointer = 0x4349c5f5 {
                        0x5d68eeb5: list[f32] = {
                            0
                            0.5
                            1
                        }
                        0x34474c3b: list[vec4] = {
                            { 1, 1, 1, 0.30000764 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.30000764 }
                        }
                    }
                }
                0x7b7a7318: i16 = 14
                0x67b5d729: vec2 = { -1, -1 }
                0xcb13aff1: f32 = -1
                0x3559e15b: flag = true
                0x2ae335b2: flag = false
                0x3c6468f4: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Mask_1_3_02.tex"
            }
        }
        0xecf1c6bc: string = "Jinx_Skin69_Idle_glow"
        0xe7638138: string = "Characters/Jinx/Skins/Skin69/Particles/Jinx_Skin69_Idle_glow"
        0x1d369c29: hash = 0xfe2a7af7
    }
    0x7060b543 = 0xef3a0f33 {
        0xd2f58721: map[hash,link] = {
            0x31552184 = 0x03ed066b
            0x26bbe6f1 = 0x93ffdb2d
            0xdd783950 = 0x01bc0a2c
            0x2982c019 = 0x0247fcf5
            0x3b20197a = 0x835fb806
            0xddc8ec0c = 0x4069ffeb
            0xfb94a30e = 0x8d7fc122
            0x329416df = 0x16c49de3
            0x80d881ef = 0xf9c1af4a
            0xd4108c3f = 0x1d704d4a
            0x1f90b4d8 = 0xc4b19dc3
            0xc373e477 = 0x3d783153
            0x5c96cb2b = 0xd73b2e57
            0x1d63ffbc = 0xb50a457b
            0xb0bb6258 = 0xec17545a
            0x7b838c08 = 0x82b414ea
            0x33ef2d7b = 0x1db613c4
            0x2aa5050b = 0xfc69f7b0
            0xaf4a6103 = 0xa66c1dff
            0xf5238fee = 0x73b3172a
            0x1bf664d2 = 0x65a2e7be
            0xd8685c04 = 0x032e2695
            0x3335629c = 0x0b5ec060
            0x6f19804f = 0xcf14bf15
            0x622544c7 = 0x9ce3b977
            0x3b4c05ba = 0x3681d014
            0xd9178839 = 0xa44c679f
            0xb05adec9 = 0x9be5a22b
            0xdf805ae1 = 0xb8057a97
            0x18809ef9 = 0x31160558
            0xc531b3ea = 0x19102673
            0x2cd3ea6c = 0x4fdc0d5f
            0xcb232a2a = 0xeb3cca21
            0x552f8456 = 0xde7b7085
            0x95883f21 = 0xa9c79040
            0xb61e2bfc = 0x4d2e580e
            0x2b67554b = 0x6036fa79
            0xd561416b = 0x3cdb5416
            0xc8a17acf = 0x88de24ca
            0x7e986a7e = 0xa76ec48c
            0x0a9f806c = 0xcc6c6637
            0xb20facf0 = 0xc96155b4
            0x1dc9cba7 = 0x7c6e6418
            0xa1e95d04 = 0xf87300ec
            0xefc5b1ee = 0x4935985d
            0x083842f0 = 0xda78fa74
            0x37a07059 = 0x8c0b598d
            0x9da4674d = 0x6720951a
            0xaa249563 = 0x1149b587
            0x8d344767 = 0x488d9523
            0x4b73542c = 0x9d93dd5a
            0x785a85cd = 0xfe9e4e37
            0x618b1f9c = 0x1081f482
            0xb4a61f18 = 0x8aa786b4
            0x228c331d = 0x39c2d3c1
            0x703192a1 = 0xd6ebdbc5
            0x2b20fcaa = 0x4ce657de
            0x9ed6347e = 0xc5c9ffda
            0x6a6b9040 = 0x37aec124
            0xa783200c = 0xc1e3bdc0
            0xea4f59c0 = 0x4935985d
            0x617f2a95 = 0x48ae2523
            0x20da2a44 = 0xba392b92
            0xd71a3e41 = 0xf29ef386
            0xa8c7afb4 = 0x39c2d3c1
            0xc200f858 = 0xd6ebdbc5
            0xf04a4703 = 0x2da001f6
            0xd1255a36 = 0xc010c817
            0x075bb707 = 0x72ec4c15
            0xef375a42 = 0x8ae27717
            0x919043e8 = 0xb0ef2c94
            0x5191a154 = 0x00000000
            0xce411392 = 0x00000000
            0x31d96392 = 0x97970998
            0x96d42b7e = 0x2bb810fc
            0xe2526e21 = 0x03816de5
            0x7c0f9a8e = 0xc717d85a
            0xa5a785c2 = 0xdd6d3a17
            0xc52c1b04 = 0xfdb5fa38
            0x48457d96 = 0xfddb780b
            0x1720d661 = 0x6f0938d5
            0xf1f9e076 = 0x982a45d2
            0xe6629014 = 0xc5179c20
            0x5d77ce60 = 0x93f1a059
            0x6077d319 = 0x90f19ba0
            0x1b69edab = 0xb8191788
            0x1c69ef3e = 0xbb191c41
            0x3f612770 = 0x58707cc6
            0x5f77d186 = 0x91f19d33
            0x2f0de378 = 0xcf75c1f0
            0x6277d63f = 0x96f1a512
            0x35f82e85 = 0x2f51dbfe
            0x34f82cf2 = 0x3051dd91
            0x2ff82513 = 0x3151df24
            0x2ef82380 = 0x3251e0b7
            0x31f82839 = 0x3351e24a
            0x30f826a6 = 0x3451e3dd
            0xcb760d49 = 0x204e2b9c
            0x562fa9bb = 0x54fb9e2d
            0xc8760890 = 0x234e3055
            0xc9760a23 = 0x224e2ec2
            0x3bf837f7 = 0x2551cc40
            0x3af83664 = 0x2651cdd3
            0x691e95c6 = 0xedcaaf2e
            0x7c5485db = 0xb633cbb1
            0x42612c29 = 0x57707b33
            0x6177d4ac = 0x97f1a6a5
            0x1d69f0d1 = 0xba191aae
            0x1e69f264 = 0xbd191f67
            0x05fa5f81 = 0x9cf4ed11
            0x1f69f3f7 = 0xbc191dd4
            0x2069f58a = 0xbf19228d
            0xbb1d1ab9 = 0xc7826e9e
            0x08a38d85 = 0x3675053a
            0xe562facd = 0xf25b0b4a
            0x0fd6fa46 = 0xe8ec412c
            0xeeafbf04 = 0xd32bf67a
            0xa96c9a02 = 0xfe2a7af7
            0x62333d7e = 0x4bf38663
            0x30efbad8 = 0xb9a5a107
            0x33efbf91 = 0xbaa5a29a
            0xf0ebf724 = 0x910404c8
        }
    }
}
