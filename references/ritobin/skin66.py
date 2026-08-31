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
    0x4f13525c = SkinCharacterDataProperties {
        SkinClassification: u32 = 2
        ChampionSkinName: string = "JinxSkin66"
        SkinParent: i32 = 65
        MetaDataTags: string = "faction:zaun,gender:female,race:human,skinline:oceansong"
        0xc3a944e7: pointer = 0xe7ee4f28 {
            0x7dd33afb: u32 = 14
            0xa2cb8e03: map[string,u32] = {
                "riot" = 1
            }
            0xc19c58be: map[string,string] = {
                "riot" = "chroma_description_222066"
            }
        }
        Loadscreen: embed = CensoredImage {
            Image: file = 0x492abeec893c6b7c
        }
        SkinAudioProperties: embed = SkinAudioProperties {
            TagEventList: list[string] = {
                "Jinx"
                "JinxSkin65"
            }
            BankUnits: list2[embed] = {
                BankUnit {
                    Name: string = "Jinx_Base_VO"
                    BankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Jinx/Skins/Base/Jinx_Base_VO_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Jinx/Skins/Base/Jinx_Base_VO_events.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Jinx/Skins/Base/Jinx_Base_VO_audio.wpk"
                    }
                    Events: list[string] = {
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
                    VoiceOver: bool = true
                }
                BankUnit {
                    Name: string = "Jinx_Skin65_SFX"
                    BankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Jinx/Skins/Skin65/Jinx_Skin65_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Jinx/Skins/Skin65/Jinx_Skin65_SFX_events.bnk"
                    }
                    Events: list[string] = {
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
        SkinAnimationProperties: embed = SkinAnimationProperties {
            AnimationGraphData: link = 0x6e5ceb16
        }
        SkinMeshProperties: embed = SkinMeshDataProperties {
            Skeleton: string = "ASSETS/Characters/Jinx/Skins/Skin65/Jinx_Skin65.skl"
            SimpleSkin: string = "ASSETS/Characters/Jinx/Skins/Skin65/Jinx_Skin65.skn"
            Texture: file = 0xa4c9f5ddcdc88715
            SkinScale: f32 = 1.03
            SelfIllumination: f32 = 0.7
            BrushAlphaOverride: f32 = 0.4
            OverrideBoundingBox: option[vec3] = {
                { 160, 228.1, 160 }
            }
            Material: link = 0x6c7042af
            ReflectionFresnelColor: rgba = { 0, 0, 0, 255 }
            InitialSubmeshToHide: string = "Recall"
            InitialSubmeshShadowsToHide: string = "Recall"
            InitialSubmeshMouseOversToHide: string = "Recall"
            MaterialOverride: list[embed] = {
                SkinMeshDataProperties_MaterialOverride {
                    Material: link = 0x6c7042af
                    Submesh: string = "Weapon"
                }
                SkinMeshDataProperties_MaterialOverride {
                    Material: link = 0xcd989594
                    Submesh: string = "Body"
                }
                SkinMeshDataProperties_MaterialOverride {
                    Material: link = 0xdd817686
                    Submesh: string = "WeaponVFX"
                }
                SkinMeshDataProperties_MaterialOverride {
                    Texture: file = 0xa4c9f5ddcdc88715
                    Submesh: string = "Hair"
                }
                SkinMeshDataProperties_MaterialOverride {
                    Material: link = 0x82dd64d2
                    Submesh: string = "Skirt"
                }
                SkinMeshDataProperties_MaterialOverride {
                    Texture: file = 0xe3508349ef6fd41c
                    Submesh: string = "Recall"
                }
            }
            RigPoseModifierData: list[pointer] = {
                ConformToPathRigPoseModifierData {
                    mStartingJointName: hash = 0x1997b0f5
                    mEndingJointName: hash = 0x1297a5f0
                    mDefaultMaskName: hash = 0xef7cfc3b
                    mVelMultiplier: f32 = 0
                }
                ConformToPathRigPoseModifierData {
                    mStartingJointName: hash = 0xde970e9b
                    mEndingJointName: hash = 0xe397167a
                    mDefaultMaskName: hash = 0xef7cfc3b
                    mVelMultiplier: f32 = 0
                }
            }
        }
        ArmorMaterial: string = "Flesh"
        DefaultAnimations: list[string] = {
            "Rlauncher_To_Minigun"
        }
        IdleParticlesEffects: list[embed] = {
            SkinCharacterDataProperties_CharacterIdleEffect {
                EffectKey: hash = 0xe562facd
                BoneName: string = "Buffbone_R_dress"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                EffectKey: hash = 0x08a38d85
                BoneName: string = "Buffbone_L_dress"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                EffectKey: hash = 0xa96c9a02
                BoneName: string = "Root"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                EffectKey: hash = 0x30efbad8
                BoneName: string = "L_Hair1"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                EffectKey: hash = 0x33efbf91
                BoneName: string = "R_Hair1"
            }
        }
        ExtraCharacterPreloads: list[string] = {
            "JinxMine"
        }
        mContextualActionData: link = "Characters/Jinx/CAC/Jinx_Base"
        IconCircle: option[file] = {
            0xbfafbb160ef44938
        }
        IconSquare: option[file] = {
            0x8519545a82fe8941
        }
        IconAvatar: file = 0x6703525659da4e06
        HealthBarData: embed = CharacterHealthBarDataRecord {
            UnitHealthBarStyle: u8 = 12
        }
        mEmblems: list[embed] = {
            SkinEmblem {
                mEmblemData: link = 0x24aba2b0
            }
        }
        mResourceResolver: link = 0x624fed9e
        PersistentEffectConditions: list2[pointer] = {
            PersistentEffectConditionData {
                OwnerCondition: pointer = AllTrueMaterialDriver {
                    mDrivers: list[pointer] = {
                        NotMaterialDriver {
                            mDriver: pointer = IsAnimationPlayingDynamicMaterialBoolDriver {
                                mAnimationNames: list[hash] = {
                                    "Recall"
                                }
                            }
                        }
                    }
                }
                PersistentVfxs: list2[embed] = {
                    PersistentVfxData {
                        BoneName: string = "Minigun"
                        TargetBoneName: string = "R_Shoulder"
                        EffectKey: hash = 0x1720d661
                    }
                }
            }
        }
        0x55d3758e: string = "ASSETS/Characters/Jinx/Skins/Skin66/ChromaPreview.tex"
        ObjectPath: hash = 0x4f13525c
    }
    0x12687e66 = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Lifetime: option[f32] = {
                    1
                }
                EmitterName: string = "Grenade1"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, -20 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_E_texmesh01.scb"
                    }
                }
                BlendMode: u8 = 3
                Pass: i16 = 1000
                ReflectionDefinition: pointer = VfxReflectionDefinitionData {
                    Fresnel: f32 = 0
                }
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -90, 0, -180 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1.2, 30, 30 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_E_texmesh01.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Grenade2"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.8509804, 0.30588236, 1, 0.3019608 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.60999465 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            0.8
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.60999465 }
                            { 1, 1, 1, 0.60999465 }
                            { 0.6509804, 0.6509804, 0.6509804, 0 }
                        }
                    }
                }
                MeshRenderFlags: u8 = 0
                AlphaRef: u8 = 0
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 30
                }
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 45, 0, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 120, 30, 30 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/3026_Items_ball32_02.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 10
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                    1.5
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            1
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    1
                }
                Lifetime: option[f32] = {
                    5
                }
                EmitterName: string = "PSmoke1"
                Importance: u8 = 3
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 50, 0 }
                }
                SpawnShape: pointer = VfxShapeBox {
                    Flags: u8 = 1
                    Size: vec3 = { 54, 120, 57 }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 30, 0 }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_E_BokehColor.tex"
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.5600061, 0.7600061, 1, 0.6 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec4] = {
                            { 0.5600061, 0.7600061, 1, 0.6 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.93000686 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.3
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.93000686 }
                            { 1, 1, 1, 0.15810187 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 900
                ColorLookUpTypeY: u8 = 3
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 90, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 70, 0.377, 0.377 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.9
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.2
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.2
                                    1.1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.2
                                    1.1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 70, 0.377, 0.377 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0.7, 1, 1 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            1
                        }
                        Values: list[vec3] = {
                            { 0.7, 1, 1 }
                            { 0.7, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin69_LensGlow01.tex"
                NumFrames: u16 = 4
                TexDiv: vec2 = { 2, 2 }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin69_Rainbow01.tex"
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 12
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            12
                        }
                    }
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.8
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1.2
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.8
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    1
                }
                Lifetime: option[f32] = {
                    1
                }
                EmitterName: string = "SparklesFast"
                Importance: u8 = 3
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 50, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 50, 0, 0 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 5, 5, 5 }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -400, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.65
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -400, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeSphere {
                    Flags: u8 = 1
                    Radius: f32 = 10
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 50, -10 }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.7300069 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        Values: list[vec4] = {
                            { 0.3529412, 0.85882354, 1, 1 }
                            { 0.38431373, 0.7019608, 1, 1 }
                            { 0.19215687, 0.20392157, 1, 1 }
                        }
                    }
                }
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 10, 35, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 10, 35, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.2
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 2, 0 }
                            { 0.8, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/TahmKench_Skin30_BasicAttack_Bubble01.tex"
                FrameRate: f32 = 5
                NumFrames: u16 = 4
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.25
                }
                ParticleLinger: option[f32] = {
                    1
                }
                Lifetime: option[f32] = {
                    0.5
                }
                EmitterName: string = "TrailBlend1"
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 30, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 400, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.8039216, 0.8509804, 1, 0.5019608 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            0.8
                            1
                        }
                        Values: list[vec4] = {
                            { 0.8039216, 0.8509804, 1, 0 }
                            { 0.8039216, 0.8509804, 1, 0.5019608 }
                            { 0.8039216, 0.8509804, 1, 0.5019608 }
                            { 0.8039216, 0.8509804, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.2
                            0.38907105
                            0.60182154
                            1
                        }
                        Values: list[vec4] = {
                            { 0.38431373, 0.9490196, 1, 0 }
                            { 0.34117648, 0.7490196, 1, 0.5921569 }
                            { 0.34117648, 0.48235294, 0.9372549, 1 }
                            { 0.30000764, 0.34999618, 0.8200046, 0.6599985 }
                            { 0.37254903, 0.21960784, 0.7607843, 0.3019608 }
                            { 0.22745098, 0.101960786, 0.49411765, 0 }
                        }
                    }
                }
                Pass: i16 = -2
                IsUniformScale: flag = true
                ParticlesShareRandomValue: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 40, 1, 1 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.3, 0.2, 0.2 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Q_Trail_fill.tex"
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.3, 0 }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.22
                }
                ParticleLinger: option[f32] = {
                    1
                }
                Lifetime: option[f32] = {
                    0.5
                }
                EmitterName: string = "TrailAdd"
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 30, 0 }
                }
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 400, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.919997 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            0.8
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.919997 }
                            { 1, 1, 1, 0.919997 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.3
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 0.38039216, 0.85490197, 1, 0 }
                            { 0.020004578, 0.4599985, 1, 0.37999544 }
                            { 0.1882353, 0.2, 1, 0.56078434 }
                            { 0.25882354, 0.09803922, 0.6, 0.92156863 }
                            { 0.1764706, 0.023529412, 0.40784314, 0 }
                        }
                    }
                }
                Pass: i16 = -2
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 50
                }
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 50, 50 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            0.5
                            1
                        }
                        Values: list[vec3] = {
                            { 0.6, 0.6, 0.6 }
                            { 0.6, 1, 1 }
                            { 0.3, 1, 1 }
                            { 0.1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_E_Trail_01.tex"
                EmitterUvScrollRate: vec2 = { -1, 0 }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.15
                }
                ParticleLinger: option[f32] = {
                    1
                }
                Lifetime: option[f32] = {
                    0.5
                }
                EmitterName: string = "TrailAdd1"
                SpawnShape: pointer = 0xee39916f {}
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 23, 0 }
                }
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 360, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.7000076 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.8
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.05
                            0.15
                            0.4
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 0.48235294, 0.13725491, 0 }
                            { 1, 0.7411765, 0.22745098, 1 }
                            { 0.17999542, 0.80999464, 1, 0.77000076 }
                            { 0.21960784, 0.53333336, 1, 0.4509804 }
                            { 0.2627451, 0.23921569, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 2
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 50
                }
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 20, 50, 50 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        Values: list[vec3] = {
                            { 1.2, 11, 1.5 }
                            { 1, 1.8, 1.8 }
                            { 0.2, 1.8, 1.8 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_BA_03.tex"
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { -1, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { -1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 16
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            16
                        }
                    }
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.7
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.7
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    0.6
                }
                Lifetime: option[f32] = {
                    5
                }
                EmitterName: string = "PSmoke3"
                Importance: u8 = 3
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 10, 20, 10 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 10, 20, 10 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeSphere {
                    Flags: u8 = 1
                    Radius: f32 = 10
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 50.1, 0 }
                }
                ParticleColorTexture: string = "ASSETS/Shared/Particles/15.tex"
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.55
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 11
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 20, 30, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.3
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 20, 30, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.4
                            0.6
                            1
                        }
                        Values: list[vec3] = {
                            { 0.6, 1, 1 }
                            { 2, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin62_EnergyMote.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Grenade4"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, -20 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_E_texmesh01.scb"
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.6500038 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 1001
                ReflectionDefinition: pointer = VfxReflectionDefinitionData {
                    Fresnel: f32 = 0
                }
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -90, 0, -180 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1.2, 30, 30 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_E_ShellMis0101.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Shared/Particles/Augment_Mercy_ChromaticGlaze_A.tex"
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 2
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLinger: option[f32] = {
                    0.4
                }
                Lifetime: option[f32] = {
                    1
                }
                EmitterName: string = "shineRing"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 20, 0 }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.75
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 962
                AlphaRef: u8 = 0
                DepthBiasFactors: vec2 = { 1, 20 }
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 360, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 120, 1, 1 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 120, 1, 1 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.257754
                            0.5080214
                            0.7497326
                            1
                        }
                        Values: list[vec3] = {
                            { 0.74817073, 0.74817073, 0.74817073 }
                            { 0.92317075, 0.9162045, 0.9162045 }
                            { 1, 1, 1 }
                            { 0.9060976, 0.91890246, 0.91890246 }
                            { 0.80792683, 0.80792683, 0.80792683 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Assets_1_369.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Caitlyn_Skin51_BA_Color03.tex"
                    BirthUvRotateRateMult: embed = ValueFloat {
                        ConstantValue: f32 = 200
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 2
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLinger: option[f32] = {
                    0.4
                }
                Lifetime: option[f32] = {
                    1
                }
                EmitterName: string = "shineRing1"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 20, 0 }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.7137255, 0.25490198, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.75
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec4] = {
                            { 1, 0.7137255, 0.25490198, 1 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 964
                AlphaRef: u8 = 0
                DepthBiasFactors: vec2 = { 1, 20 }
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 360, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 80, 1, 1 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.257754
                            0.5080214
                            0.7497326
                            1
                        }
                        Values: list[vec3] = {
                            { 0.74817073, 0.74817073, 0.74817073 }
                            { 0.92317075, 0.9162045, 0.9162045 }
                            { 1, 1, 1 }
                            { 0.9060976, 0.91890246, 0.91890246 }
                            { 0.80792683, 0.80792683, 0.80792683 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/BA_Hex_Indicator_1_01.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Caitlyn_Skin51_BA_Color03.tex"
                    BirthUvRotateRateMult: embed = ValueFloat {
                        ConstantValue: f32 = 200
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Grenade6"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, -20 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_E_texmesh01.scb"
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.77999544, 0.2500038, 0.9499962 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.65
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec4] = {
                            { 1, 0.77999544, 0.2500038, 0.9499962 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 1001
                ReflectionDefinition: pointer = VfxReflectionDefinitionData {
                    Fresnel: f32 = 0
                }
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -90, 0, -180 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1.2, 30, 30 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_E_ShellMis03.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Shared/Particles/3026_Items_Noise_02.tex"
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = 45
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.15
                }
                ParticleLinger: option[f32] = {
                    1
                }
                Lifetime: option[f32] = {
                    0.5
                }
                EmitterName: string = "TrailAdd3"
                SpawnShape: pointer = 0xee39916f {}
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 23, 0 }
                }
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 360, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.6 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.8
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.6 }
                            { 1, 1, 1, 0.6 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.05
                            0.15
                            0.4
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 0.40784314, 0.22745098, 0 }
                            { 1, 0.80784315, 0.23529412, 1 }
                            { 0.17999542, 0.80999464, 1, 0.7600061 }
                            { 0.22000457, 0.5300069, 1, 0.4 }
                            { 0.2627451, 0.23921569, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 1
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 50
                }
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 20, 50, 50 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        Values: list[vec3] = {
                            { 1.2, 1, 1.5 }
                            { 1, 1.8, 1.8 }
                            { 0.2, 1.8, 1.8 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_BA_03.tex"
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { -1, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { -1, 0 }
                        }
                    }
                }
            }
        }
        ParticleName: string = "Jinx_Skin66_E_Mis"
        ParticlePath: string = "Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_E_Mis"
        ObjectPath: hash = 0x12687e66
    }
    0x1a046b26 = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 24
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.6
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            24
                        }
                    }
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.8
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.8
                        }
                    }
                }
                EmitterName: string = "Basic7"
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -5, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -5, 0 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    Flags: u8 = 1
                    Size: vec3 = { 10, 20, 15 }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 4, 0, 0 }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.71691465, 0.7019608, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec4] = {
                            { 1, 0.71691465, 0.7019608, 1 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.3095499
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 901
                AlphaRef: u8 = 0
                0xcb13aff1: f32 = -2
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                UseNavmeshMask: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    360
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 15, 10, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.2
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 15, 10, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.44716242
                            1
                        }
                        Values: list[vec3] = {
                            { 0.49839142, 0, 0 }
                            { 0.6608579, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Nidalee_Skin29_egoprestige_speark.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_rainbow.tex"
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 1.5 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 60
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.5
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.5
                        }
                    }
                }
                EmitterName: string = "Basic8"
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -20, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -20, 0 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    Flags: u8 = 1
                    Size: vec3 = { 5, 20, 15 }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 8, -5, 0 }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.27041095
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 0.15294118, 0.16862746, 1, 0 }
                            { 0.13333334, 0.1764706, 1, 1 }
                            { 0.29411766, 0.90588236, 1, 1 }
                            { 0.1254902, 0.35686275, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 901
                AlphaRef: u8 = 0
                0xcb13aff1: f32 = -2
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                UseNavmeshMask: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    360
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 4, 10, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.3
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 4, 10, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.44716242
                            1
                        }
                        Values: list[vec3] = {
                            { 0.49839142, 0, 0 }
                            { 0.6608579, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Dance_Sparks.tex"
            }
        }
        ParticleName: string = "Jinx_Skin66_Idle_Flicker_1"
        ParticlePath: string = "Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Idle_Flicker_1"
        ScaleDynamicallyWithAttachedBone: bool = true
        ObjectPath: hash = 0x1a046b26
    }
    0x2ffe8895 = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.4
                }
                ParticleLinger: option[f32] = {
                    0.5
                }
                Lifetime: option[f32] = {
                    2
                }
                EmitterName: string = "TrailBlend"
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 20, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 300, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.5000076 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.05
                            0.8
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.5000076 }
                            { 1, 1, 1, 0.5000076 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.2
                            0.3
                            0.60182154
                            1
                        }
                        Values: list[vec4] = {
                            { 0.27450982, 0.78431374, 1, 0 }
                            { 0.28000304, 0.6, 1, 0.4 }
                            { 0.25882354, 0.45490196, 1, 0.83137256 }
                            { 0.27450982, 0.38039216, 0.9882353, 0.65882355 }
                            { 0.27450982, 0.23529412, 0.84313726, 0.34117648 }
                            { 0.29411766, 0.18039216, 0.6313726, 0 }
                        }
                    }
                }
                Pass: i16 = -2
                IsUniformScale: flag = true
                ParticlesShareRandomValue: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 35, 1, 1 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.6, 1, 1 }
                            { 0.2, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Q_Trail_fill.tex"
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.3, 0 }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.4
                }
                ParticleLinger: option[f32] = {
                    0.5
                }
                Lifetime: option[f32] = {
                    2
                }
                EmitterName: string = "TrailBlend1"
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -200, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -200, 0 }
                        }
                    }
                }
                Primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 500, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.7000076 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.05
                            0.8
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.12
                            0.55
                            1
                        }
                        Values: list[vec4] = {
                            { 0.21568628, 0.4509804, 1, 0 }
                            { 0.34000152, 0.40999466, 1, 0.85999846 }
                            { 0.3100023, 0.2899977, 0.8200046, 0.6200046 }
                            { 0.3137255, 0.13725491, 0.5647059, 0 }
                        }
                    }
                }
                Pass: i16 = -4
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0.2
                                1
                            }
                            Values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.25
                    ErosionFeatherOut: f32 = 0.25
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                IsUniformScale: flag = true
                ParticlesShareRandomValue: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 65, 1, 1 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.4
                            1
                        }
                        Values: list[vec3] = {
                            { 0.7, 0.7, 0.7 }
                            { 1, 1, 1 }
                            { 1.3, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Aurora_Skin20_Comet_Trail_01.tex"
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 0.3, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 0.3, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.2
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    2
                }
                EmitterName: string = "TrailAdd1"
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 320, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.05
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.15
                            0.35
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 0.2784314, 0.8784314, 1, 0 }
                            { 0.2784314, 0.78431374, 1, 1 }
                            { 0.25490198, 0.47843137, 1, 1 }
                            { 0.26999313, 0.37000075, 1, 0.5000076 }
                            { 0.4, 0.2, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 2
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 50
                }
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 23, 50, 50 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1.5 }
                            { 0.1, 1.8, 1.8 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_BA_03.tex"
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 1, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.2
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    2
                }
                EmitterName: string = "TrailAdd2"
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 320, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.05
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.15
                            0.35
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 0.2784314, 0.8784314, 1, 0 }
                            { 0.25882354, 0.6431373, 1, 0.8509804 }
                            { 0.17999542, 0.33000687, 1, 0.66999316 }
                            { 0.22999924, 0.26999313, 1, 0.42999923 }
                            { 0.2, 0.14509805, 0.6117647, 0 }
                        }
                    }
                }
                Pass: i16 = 1
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 50
                }
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 23, 50, 50 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.1, 1.8, 1.8 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_BA_03.tex"
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 1, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 28
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            28
                        }
                    }
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.5
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.35
                                    1.5
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.5
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    0.7
                }
                Lifetime: option[f32] = {
                    1
                }
                EmitterName: string = "STARS_BACKGROUND"
                Importance: u8 = 3
                BirthOrbitalVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 1, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 1, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 50, -10, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -0.2
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 50, -10, 0 }
                        }
                    }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeSphere {
                    Flags: u8 = 1
                    Radius: f32 = 10
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -50, -10 }
                }
                ParticleColorTexture: string = "ASSETS/Shared/Particles/15.tex"
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                ColorLookUpTypeY: u8 = 3
                DepthBiasFactors: vec2 = { -1, -18 }
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 40, 65, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.9
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.3
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 40, 65, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin51_W_BightSpark.tex"
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.03
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.5
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "FlameGlow"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 25, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.5000076 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.7000076 }
                }
                Pass: i16 = 150
                AlphaRef: u8 = 0
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 90, 0 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin62_Alpha_Backdrop.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_splash_ring_Mask_2_01.tex"
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = -90
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Lifetime: option[f32] = {
                    1.85
                }
                IsSingleParticle: flag = true
                EmitterName: string = "feather"
                Importance: u8 = 3
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0.01, 0 }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -30, 0 }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.4 }
                }
                Pass: i16 = -50
                AlphaRef: u8 = 0
                IsDirectionOriented: flag = true
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                IsRotationEnabled: flag = true
                DirectionVelocityScale: f32 = 0.001
                DirectionVelocityMinScale: f32 = 1.5
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 25, 1.26 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Soraka_ball32_02.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_mis_Mask_Color_6_8.tex"
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = 180
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.03
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "bullets"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {}
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Mis_Hand_grenade.scb"
                    }
                    AlignPitchToCamera: bool = true
                    AlignYawToCamera: bool = true
                }
                BlendMode: u8 = 3
                Pass: i16 = 80
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 180, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 3.2, 2, 2.2 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Q_Mis_Thorn_2.tex"
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.03
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "bullets1"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {}
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Mis_Hand_grenade.scb"
                    }
                    AlignPitchToCamera: bool = true
                    AlignYawToCamera: bool = true
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.2 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.7000076 }
                }
                Pass: i16 = 81
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 180, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 3.2, 2, 2.2 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Q_Mis_Thorn_2.tex"
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.03
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "DarkBG"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -45, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.09803922, 0.5647059, 1, 0.7019608 }
                }
                AlphaRef: u8 = 0
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 80, 0 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/MissFortune_Skin69_MisLead_Mask.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/MissFortune_Skin69_E_Screen_Flames_Soft.tex"
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 2, 1 }
                    }
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, -3 }
                    }
                }
            }
        }
        ParticleName: string = "Jinx_Skin66_Q_RocketHurricaneMis"
        ParticlePath: string = "Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Q_RocketHurricaneMis"
        ObjectPath: hash = 0x2ffe8895
    }
    0x3765d2be = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 24
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.6
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            24
                        }
                    }
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.8
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.8
                        }
                    }
                }
                EmitterName: string = "Basic"
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -5, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -5, 0 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    Flags: u8 = 1
                    Size: vec3 = { 10, 20, 15 }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { -4, 0, 5 }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.83677423, 0.7019608, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec4] = {
                            { 1, 0.83677423, 0.7019608, 1 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.3095499
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 901
                AlphaRef: u8 = 0
                0xcb13aff1: f32 = -2
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                UseNavmeshMask: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    360
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 15, 10, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.2
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 15, 10, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.44716242
                            1
                        }
                        Values: list[vec3] = {
                            { 0.49839142, 0, 0 }
                            { 0.6608579, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Nidalee_Skin29_egoprestige_speark.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_rainbow.tex"
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 1.5 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 60
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.5
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.5
                        }
                    }
                }
                EmitterName: string = "Basic1"
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -20, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -20, 0 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    Flags: u8 = 1
                    Size: vec3 = { 5, 20, 15 }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { -8, -5, 5 }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.27041095
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 0.15294118, 0.16862746, 1, 0 }
                            { 0.13333334, 0.1764706, 1, 1 }
                            { 0.29411766, 0.90588236, 1, 1 }
                            { 0.1254902, 0.35686275, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 901
                AlphaRef: u8 = 0
                0xcb13aff1: f32 = -2
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                UseNavmeshMask: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    360
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 4, 10, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.3
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 4, 10, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.44716242
                            1
                        }
                        Values: list[vec3] = {
                            { 0.49839142, 0, 0 }
                            { 0.6608579, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Dance_Sparks.tex"
            }
        }
        ParticleName: string = "Jinx_Skin66_Idle_Flicker"
        ParticlePath: string = "Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Idle_Flicker"
        ScaleDynamicallyWithAttachedBone: bool = true
        ObjectPath: hash = 0x3765d2be
    }
    0x45983dbb = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = -1
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Dark_Activate2"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xed500a70
                        }
                        mSubmeshesToDrawAlways: list[hash] = {
                            0xed500a70
                        }
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.81960785, 0.81960785, 0.81960785, 1 }
                }
                DepthBiasFactors: vec2 = { -1, -1 }
                IsUniformScale: flag = true
                IsLocalOrientation: flag = false
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin66/Jinx_Skin66_Weapon_TX_CM.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Mask_1_3_02.tex"
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterName: string = "Dark_Activate3"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xed500a70
                        }
                        mSubmeshesToDrawAlways: list[hash] = {
                            0xed500a70
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.70980394, 0.24313726, 0.5294118 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.45
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.30000764 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.30000764 }
                        }
                    }
                }
                Pass: i16 = 14
                DepthBiasFactors: vec2 = { -1, -1 }
                0xcb13aff1: f32 = -1
                IsUniformScale: flag = true
                IsLocalOrientation: flag = false
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Mask_1_3_03.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterName: string = "Dark_Activate5"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xed500a70
                        }
                        mSubmeshesToDrawAlways: list[hash] = {
                            0xed500a70
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.33000687, 0.7100023, 1, 0.86999315 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.30000764 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.30000764 }
                        }
                    }
                }
                Pass: i16 = 14
                DepthBiasFactors: vec2 = { -1, -1 }
                0xcb13aff1: f32 = -1
                IsUniformScale: flag = true
                IsLocalOrientation: flag = false
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Mask_1_3_02.tex"
            }
        }
        ParticleName: string = "Jinx_Skin66_Idle_glow"
        ParticlePath: string = "Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Idle_glow"
        ObjectPath: hash = 0x45983dbb
    }
    0x55c9e65b = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.1
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.15
                }
                Lifetime: option[f32] = {
                    2
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Distort_Warp"
                Importance: u8 = 3
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -100, 170 }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin60_color-rampdown32.tex"
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.7
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 3000
                DistortionDefinition: pointer = VfxDistortionDefinitionData {
                    Distortion: f32 = 0.01
                    NormalMapTexture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin60_distort_soft_shockwave.tex"
                }
                DepthBiasFactors: vec2 = { -1, -25 }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 450, 200, 200 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        Values: list[vec3] = {
                            { 0.6250996, 0.2, 0.2 }
                            { 1, 1, 1 }
                            { 1.3, 1.3, 1.3 }
                        }
                    }
                }
                Texture: string = "ASSETS/Shared/Particles/DefaultColorOverlifetime.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 30
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        Times: list[f32] = {
                            0
                            0.3
                            0.5
                            1
                        }
                        Values: list[f32] = {
                            60
                            30
                            3
                            0
                        }
                    }
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    0.7
                                    1.2
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            1
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    11
                }
                Lifetime: option[f32] = {
                    50
                }
                EmitterName: string = "SparklesFast"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 200, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.3
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 200, 0, 0 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 5, 5, 5 }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -600, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -600, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeSphere {
                    Flags: u8 = 1
                    Radius: f32 = 35
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -150, 90 }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.9000076 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.6
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.9000076 }
                            { 0.192157, 1, 0.827451, 0.9000076 }
                            { 1, 0, 0.682353, 0.9000076 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        Values: list[vec4] = {
                            { 0.23921569, 0.8352941, 1, 1 }
                            { 0.24313726, 0.7607843, 1, 1 }
                            { 0.13725491, 0.30588236, 0.85490197, 1 }
                        }
                    }
                }
                Pass: i16 = 50
                ColorLookUpTypeY: u8 = 3
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 30
                }
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 10, 35, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 10, 35, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.2
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.2, 2, 0 }
                            { 0.8, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Zeri_Skin10_Q_Bubble01.tex"
                NumFrames: u16 = 4
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 400
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.8
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.2
                                    1
                                    1.5
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.8
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    1
                }
                Lifetime: option[f32] = {
                    5
                }
                EmitterName: string = "PSmoke"
                Importance: u8 = 3
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -20, 0 }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -500, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -500, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeBox {
                    Flags: u8 = 1
                    Size: vec3 = { 15, 100, 30 }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 30, 100 }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin51_Flicker_04.tex"
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.66999316 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.2
                            0.3
                            1
                        }
                        Values: list[vec4] = {
                            { 0.5372549, 0.85490197, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.5137255, 0.7882353, 1, 1 }
                            { 0.14901961, 0.19215687, 1, 1 }
                            { 0.13333334, 0.19215687, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 997
                ColorLookUpTypeY: u8 = 3
                0xcb13aff1: f32 = -80
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 80, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 80, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 25, 0.377, 0.377 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.2
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.2
                                    1.1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.2
                                    1.1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 25, 0.377, 0.377 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            1
                        }
                        Values: list[vec3] = {
                            { 0.2, 0.2, 0.2 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin62_EnergyMote.tex"
                NumFrames: u16 = 2
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 6
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.6
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.4
                                    0.75
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.6
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    1
                }
                Lifetime: option[f32] = {
                    5
                }
                EmitterName: string = "PSmoke1"
                Importance: u8 = 3
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -20, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -20, 0 }
                        }
                    }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeBox {
                    Flags: u8 = 1
                    Size: vec3 = { 50, 150, 30 }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -100, -30 }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Bokeh_Color.tex"
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.42000458 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.42000458 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.13207547
                            0.3
                            0.43910807
                            0.77186966
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.84615386 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.8552036 }
                            { 1, 1, 1, 0.19004525 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 50
                ColorLookUpTypeY: u8 = 3
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 80, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 80, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 30, 6, 6 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 30, 6, 6 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Dance_Sparks.tex"
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.1
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "FakeShadow2"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -130, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, -10 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                ParticleColorTexture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/color-hold_2.tex"
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.34117648, 0.28235295, 0.67058825, 1 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.001
                            0.015
                            0.02
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = -1
                MeshRenderFlags: u8 = 0
                AlphaRef: u8 = 0
                MiscRenderFlags: u8 = 1
                IsGroundLayer: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 80, 300, 700 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/W_Beam_EPassive_03_1_1_2.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Caitlyn_Skin51_AnimeShapes061.tex"
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = 90
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.08
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.2
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Ground_light2"
                Importance: u8 = 3
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -40, 100 }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.77999544 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.3
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.8627451, 0.36078432, 1, 0.3019608 }
                            { 0.48235294, 0.13725491, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 20
                AlphaRef: u8 = 0
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 0, 90 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 0, 90 }
                        }
                    }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 10, 0, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 350, 350, 0 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        Values: list[vec3] = {
                            { 0.57768923, 0, 0 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 1.5 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Camille_Skin44_Q_Hex_Indicator_1_1_007.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Caitlyn_Skin51_BA_Color03.tex"
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = 1
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            ProbabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    KeyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    KeyValues: list[f32] = {
                                        -360
                                        1
                                    }
                                }
                            }
                            Times: list[f32] = {
                                0
                            }
                            Values: list[f32] = {
                                1
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 12
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.4
                }
                ParticleLinger: option[f32] = {
                    0.1
                }
                Lifetime: option[f32] = {
                    50
                }
                EmitterName: string = "WaterAdd"
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -100, 0 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Zeri_Skin10_R_Water.scb"
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.2399939, 0.7100023, 1, 0.2 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.01
                            1
                        }
                        Values: list[vec4] = {
                            { 0.2399939, 0.7100023, 1, 0 }
                            { 0.2399939, 0.7100023, 1, 0.2 }
                            { 0.2399939, 0.7100023, 1, 0.2 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.3
                            0.8
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = -2
                AlphaRef: u8 = 0
                MiscRenderFlags: u8 = 1
                IsGroundLayer: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -270, 0, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0.85, 0, 1.7 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.05
                            0.6
                            0.95
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 0.5, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 0, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Zeri_Skin10_Wave_Foam_Stylized_01.tex"
                UvMode: u8 = 2
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0, -0.2 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 0, -0.2 }
                        }
                    }
                }
                BirthUvoffset: embed = ValueVector2 {
                    ConstantValue: vec2 = { 1, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 0, 1 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 0, 1 }
                        }
                    }
                }
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { 1.3, 1.7 }
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_Water_Alpha01.tex"
                    TexAddressModeMult: u8 = 2
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 100
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.65
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            1
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    1
                }
                EmitterName: string = "circleSPARKLES"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -100, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -100, 0 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 3, 5, 0 }
                }
                SpawnShape: pointer = VfxShapeBox {
                    Flags: u8 = 1
                    Size: vec3 = { 10, 10, 10 }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 135, 60, 0 }
                }
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.7499962 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.2
                            0.4
                            1
                        }
                        Values: list[vec4] = {
                            { 0.29411766, 0.6, 1, 1 }
                            { 0.17000076, 0.5300069, 1, 0.2 }
                            { 0.08999771, 0.40999466, 1, 0.2 }
                        }
                    }
                }
                Pass: i16 = 6
                DepthBiasFactors: vec2 = { -1, -50 }
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 16, 10, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.15
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 16, 10, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_R_BightSpark.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 100
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.65
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            1
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    1
                }
                EmitterName: string = "circleSPARKLES1"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -100, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -100, 0 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 3, 5, 0 }
                }
                SpawnShape: pointer = VfxShapeBox {
                    Flags: u8 = 1
                    Size: vec3 = { 10, 10, 10 }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { -135, 60, 0 }
                }
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.7499962 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.2
                            0.4
                            1
                        }
                        Values: list[vec4] = {
                            { 0.29411766, 0.6, 1, 1 }
                            { 0.17000076, 0.5300069, 1, 0.2 }
                            { 0.08999771, 0.40999466, 1, 0.2 }
                        }
                    }
                }
                Pass: i16 = 6
                DepthBiasFactors: vec2 = { -1, -50 }
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 16, 10, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.15
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 16, 10, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_R_BightSpark.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 100
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.6
                }
                ParticleLinger: option[f32] = {
                    0.25
                }
                Lifetime: option[f32] = {
                    50
                }
                EmitterName: string = "L_Edge2"
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 2, 0, 2 }
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 150, 0, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 80, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 700, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.2 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.001
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.2 }
                            { 1, 1, 1, 0.2 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.2
                            0.4
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.2 }
                            { 1, 1, 1, 1 }
                            { 0.2901961, 0.59607846, 1, 0.3019608 }
                            { 0.20784314, 0.28627452, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 1
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                1
                            }
                            Values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    ErosionFeatherOut: f32 = 0.3
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_R_Water02.tex"
                }
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsGroundLayer: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 50, 50, 0 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        Values: list[vec3] = {
                            { 0.2, 1, 1 }
                            { 1, 1, 1 }
                            { 0.2, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_R_Water02.tex"
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.3, 0 }
                }
                BirthUvoffset: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.5, 0 }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.4
                }
                ParticleLinger: option[f32] = {
                    0.6
                }
                Lifetime: option[f32] = {
                    50
                }
                RateByVelocityFunction: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.1, 0.1 }
                }
                EmitterName: string = "Trail_BG6"
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { -35, 5, 100 }
                }
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 1500
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 500, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.5100023 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.02
                            0.9
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.5100023 }
                            { 1, 1, 1, 0.5100023 }
                            { 1, 1, 1, 0.40800184 }
                            { 1, 1, 1, 0.40800184 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.15
                            0.35
                            0.65
                            1
                        }
                        Values: list[vec4] = {
                            { 0.73333335, 0.3647059, 1, 0 }
                            { 0.7882353, 0.3647059, 1, 0.54901963 }
                            { 0.5254902, 0.2509804, 1, 0.67058825 }
                            { 0.050003815, 0.1600061, 0.7400015, 0.10000763 }
                            { 0.007843138, 0.12941177, 0.5647059, 0 }
                        }
                    }
                }
                Pass: i16 = 4
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        ConstantValue: f32 = 0
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                1
                            }
                            Values: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.25
                    ErosionFeatherOut: f32 = 0.25
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsGroundLayer: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 110, 1, 1 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.014
                            0.016
                            0.02
                            1
                        }
                        Values: list[vec3] = {
                            { 93.5, 0, 0 }
                            { 93.5, 1, 1 }
                            { 110, 0, 0 }
                            { 110, 0, 0 }
                            { 110, 0, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            1
                        }
                        Values: list[vec3] = {
                            { 0.8, 1, 1 }
                            { 1, 1, 1 }
                            { 0.4, 0.2, 0.2 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_09.tex"
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 0.05, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 0.05, 0 }
                        }
                    }
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/W_Mis_Water_1_01111.tex"
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = 90
                    }
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, 60 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.45
                }
                ParticleLinger: option[f32] = {
                    0.6
                }
                Lifetime: option[f32] = {
                    50
                }
                EmitterName: string = "TrailBlend5"
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -60, 90 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 350, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.001
                            0.1
                            0.2
                            0.8
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.8 }
                            { 1, 1, 1, 0.8 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.45
                            0.60182154
                            1
                        }
                        Values: list[vec4] = {
                            { 0.20392157, 0.654902, 1, 0 }
                            { 0.19215687, 0.654902, 0.9411765, 0.8392157 }
                            { 0.20999466, 0.34000152, 0.88000304, 0.46999314 }
                            { 0.2899977, 0.17000076, 0.59000534, 0.22000457 }
                            { 0.29411766, 0.050980393, 0.46666667, 0 }
                        }
                    }
                }
                Pass: i16 = 2
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsGroundLayer: flag = true
                ParticlesShareRandomValue: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 70, 1, 1 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.05
                            1
                        }
                        Values: list[vec3] = {
                            { 0.6, 1, 1 }
                            { 0.6, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Q_Trail_fill.tex"
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.3, 0 }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.6
                }
                ParticleLinger: option[f32] = {
                    0.6
                }
                Lifetime: option[f32] = {
                    50
                }
                EmitterName: string = "TrailBlend6"
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -300, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -300, 0 }
                        }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 85 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 700, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.85000384 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.01
                            0.015
                            0.9
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.6800031 }
                            { 1, 1, 1, 0.6800031 }
                            { 1, 1, 1, 0.85000384 }
                            { 1, 1, 1, 0.85000384 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.40406722
                            0.5482442
                            1
                        }
                        Values: list[vec4] = {
                            { 0.08627451, 0.52156866, 0.75686276, 0 }
                            { 0.2899977, 0.37000075, 0.86999315, 0.7000076 }
                            { 0.3764706, 0.30980393, 0.8784314, 0.9098039 }
                            { 0.4399939, 0.2, 0.7000076, 0.5600061 }
                            { 0.15686275, 0.015686275, 0.29803923, 0 }
                        }
                    }
                }
                Pass: i16 = 1
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                1
                            }
                            Values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.25
                    ErosionFeatherOut: f32 = 0.25
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsGroundLayer: flag = true
                ParticlesShareRandomValue: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 150, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.014
                            0.0165
                            0.02
                            1
                        }
                        Values: list[vec3] = {
                            { 120, 0, 0 }
                            { 120, 0, 0 }
                            { 150, 0, 0 }
                            { 135, 0, 0 }
                            { 135, 0, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        Values: list[vec3] = {
                            { 0.7, 1, 1 }
                            { 1.2, 1, 1 }
                            { 0.7, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Aurora_Skin20_Comet_Trail_01.tex"
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 0.3, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 0.3, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.1
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Conemesh_1"
                Velocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -70, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.0121
                            0.015
                            0.016
                        }
                        Values: list[vec3] = {
                            { 0, -7, 0 }
                            { 0, -70, 0 }
                            { 0, -70, 0 }
                            { 0, -0, 0 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -80, 100 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/fireball.SCB"
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.5254902, 0.8980392, 1, 1 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.3137255, 0.5764706, 1, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.014
                            0.016
                        }
                        Values: list[vec4] = {
                            { 0.3137255, 0.5764706, 1, 1 }
                            { 0.3137255, 0.5764706, 1, 1 }
                            { 0.3137255, 0.5764706, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 322
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    BeginIn: f32 = 20
                    DeltaIn: f32 = 10
                }
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        ConstantValue: f32 = 0
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                1
                            }
                            Values: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Shyvana_Base_E_ErosionLoweRes.tex"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    ErosionMapAddressMode: u8 = 0
                }
                MiscRenderFlags: u8 = 1
                ParticleIsLocalOrientation: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -90, 0, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 5, 5, 11 }
                }
                Scale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 2, 2, 2 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.012
                            0.016
                            1
                        }
                        Values: list[vec3] = {
                            { 2, 2, 2 }
                            { 2, 2, 2 }
                            { 2.4, 2.4, 2.6 }
                            { 2.4, 2.4, 2.6 }
                        }
                    }
                }
                Texture: string = "ASSETS/Shared/Particles/3026_Items_Streaks.tex"
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0, 0.55 }
                }
                BirthUvoffset: embed = ValueVector2 {
                    ConstantValue: vec2 = { -0.25, 0.5 }
                }
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 0.5, 2 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            0.5
                        }
                        Values: list[vec2] = {
                            { 0.5, 4 }
                            { 0.5, 4 }
                            { 0.5, 1 }
                        }
                    }
                }
                UvScale: embed = ValueVector2 {
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec2] = {
                            { 1, 2 }
                            { 1, 0.5 }
                            { 1, 1 }
                        }
                    }
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Morg_Base_E_MeshMult.tex"
                    TexAddressModeMult: u8 = 2
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, 1.35 }
                    }
                    BirthUvoffsetMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, -0.25 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.1
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                ChildParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    ChildrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            EffectKey: hash = "Jinx_R_Rocket_Child"
                        }
                    }
                }
                EmitterName: string = "FakeShadow3"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -50, 100 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                ParticleColorTexture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/color-hold_2.tex"
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.020004578, 0.020004578, 0.050003815, 0 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0 }
                }
                Pass: i16 = 103
                MeshRenderFlags: u8 = 0
                AlphaRef: u8 = 0
                MiscRenderFlags: u8 = 1
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -120, 0 }
                }
                Rotation0: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -15, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.002
                            0.01
                            0.012
                            0.018
                            0.019
                        }
                        Values: list[vec3] = {
                            { 0, -7.5, 0 }
                            { 0, -0, 0 }
                            { 0, -0, 0 }
                            { 0, -0, 0 }
                            { 0, -60, 0 }
                            { 0, -8.25, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 110, 200, 700 }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Projected21"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 30, 102 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.4 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.014
                            0.018
                            0.025
                            0.1
                            0.7
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 5
                MeshRenderFlags: u8 = 0
                AlphaRef: u8 = 0
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 80, 700 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0.08
                            0.018
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_splash_ring_Mask_1_1_011_3.tex"
                UvRotation: embed = ValueFloat {
                    ConstantValue: f32 = 180
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Trail_01_7.tex"
                    TexAddressModeMult: u8 = 2
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = 180
                    }
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, 1.1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.55
                }
                ParticleLinger: option[f32] = {
                    0.6
                }
                Lifetime: option[f32] = {
                    50
                }
                RateByVelocityFunction: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.1, 0.1 }
                }
                EmitterName: string = "Trail_BG7"
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -100, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -100, 0 }
                        }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 25, 35, 100 }
                }
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 1500
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 850, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.5100023, 0.7100023, 1, 0.42999923 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.9
                            1
                        }
                        Values: list[vec4] = {
                            { 0.5100023, 0.7100023, 1, 0 }
                            { 0.5100023, 0.7100023, 1, 0.42999923 }
                            { 0.5100023, 0.7100023, 1, 0.42999923 }
                            { 0.5100023, 0.7100023, 1, 0.42999923 }
                            { 0.5100023, 0.7100023, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.15
                            0.25
                            0.4
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.26999313 }
                            { 1, 1, 1, 0.65882355 }
                            { 1, 1, 1, 0.42000458 }
                            { 1, 1, 1, 0.2399939 }
                            { 0.5647059, 0.5647059, 0.5647059, 0 }
                        }
                    }
                }
                Pass: i16 = 3
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                1
                            }
                            Values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.25
                    ErosionFeatherOut: f32 = 0.25
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsGroundLayer: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 120, 1, 1 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.014
                            0.016
                            0.02
                            1
                        }
                        Values: list[vec3] = {
                            { 102, 0, 0 }
                            { 102, 1, 1 }
                            { 120, 0, 0 }
                            { 120, 0, 0 }
                            { 120, 0, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 0.5 }
                            { 0.3, 0.5, 0.5 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_08.tex"
                EmitterUvScrollRate: vec2 = { 0.15, 0 }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Caitlyn_Skin51_AnimeShapes061.tex"
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.4
                }
                ParticleLinger: option[f32] = {
                    0.6
                }
                Lifetime: option[f32] = {
                    50
                }
                RateByVelocityFunction: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.1, 0.1 }
                }
                EmitterName: string = "Trail_BG8"
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { -35, 5, 100 }
                }
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 1500
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 500, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.85000384, 0.4599985, 1, 0.4 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.9
                            1
                        }
                        Values: list[vec4] = {
                            { 0.85000384, 0.4599985, 1, 0 }
                            { 0.85000384, 0.4599985, 1, 0.4 }
                            { 0.85000384, 0.4599985, 1, 0.4 }
                            { 0.85000384, 0.4599985, 1, 0.4 }
                            { 0.85000384, 0.4599985, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.7499962 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.15
                            0.35
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.38999572 }
                            { 1, 1, 1, 0.5024923 }
                            { 1, 1, 1, 0.08250129 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 3
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        ConstantValue: f32 = 0
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                1
                            }
                            Values: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.25
                    ErosionFeatherOut: f32 = 0.25
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsGroundLayer: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 110, 1, 1 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.014
                            0.016
                            0.02
                            1
                        }
                        Values: list[vec3] = {
                            { 93.5, 0, 0 }
                            { 93.5, 1, 1 }
                            { 110, 0, 0 }
                            { 110, 0, 0 }
                            { 110, 0, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            1
                        }
                        Values: list[vec3] = {
                            { 0.8, 1, 1 }
                            { 1, 1, 1 }
                            { 0.4, 0.2, 0.2 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_09.tex"
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 0.05, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 0.05, 0 }
                        }
                    }
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_mis_Mask_Color_6_1.tex"
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Missle12"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -50, 100 }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { -2, 0, 0 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_Splash_1_004.scb"
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.73333335, 0, 0, 1 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.014
                            0.018
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 800
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    BeginIn: f32 = 20
                    DeltaIn: f32 = 10
                }
                DepthBiasFactors: vec2 = { -1, -100 }
                MiscRenderFlags: u8 = 1
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -95, 180, 0 }
                }
                Rotation0: embed = IntegratedValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.002
                            0.01
                            0.014
                            0.018
                            0.019
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 4, 4, 4 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.004
                            0.012
                            0.014
                            0.016
                            0.02
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.0053098, 1.0053098, 1.0053098 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 0.2 }
                            { 0.5, 0.5, 1.25 }
                            { 1.2, 1.2, 1.2 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_mis_Mask_Color_6_011.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Missle13"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -50, 100 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skl"
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.06999313, 0.06999313, 0.6 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.012
                            0.015
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 104
                DepthBiasFactors: vec2 = { -1, -100 }
                DoesCastShadow: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -95, 180, 0 }
                }
                Rotation0: embed = IntegratedValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.002
                            0.01
                            0.014
                            0.018
                            0.019
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 4, 4, 4 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.004
                            0.012
                            0.014
                            0.016
                            0.02
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.0053098, 1.0053098, 1.0053098 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 0.2 }
                            { 0.5, 0.5, 1.25 }
                            { 1.2, 1.2, 1.2 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Pufferfish_1_01.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Missle15"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -50, 100 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skl"
                    }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.42745098, 0.25490198, 1 }
                }
                Pass: i16 = 103
                DepthBiasFactors: vec2 = { -1, -100 }
                DoesCastShadow: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -95, 180, 0 }
                }
                Rotation0: embed = IntegratedValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.002
                            0.01
                            0.014
                            0.018
                            0.019
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 4, 4, 4 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.004
                            0.012
                            0.014
                            0.016
                            0.02
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.0053098, 1.0053098, 1.0053098 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 0.2 }
                            { 0.5, 0.5, 1.25 }
                            { 1.2, 1.2, 1.2 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_mis_globefish_Mask_1.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    5
                }
                IsSingleParticle: flag = true
                EmitterLinger: option[f32] = {
                    0.3
                }
                EmitterName: string = "head_"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {}
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -210, 95 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.78431374, 0.78431374, 0.78431374, 0.4 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.014
                            0.02
                            0.1
                            0.7
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 2
                MeshRenderFlags: u8 = 0
                AlphaRef: u8 = 0
                MiscRenderFlags: u8 = 1
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 180, 0, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 160, 100, 100 }
                }
                Scale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 2, 1, 1 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lux_Skin70_Idle_Glow051_4.tex"
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { -1, 1 }
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_Mask_1_1_01.tex"
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.1
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    3
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Temp_GroundGlow2"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -345, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.7921569, 0.30588236, 0.6 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.6 }
                }
                Pass: i16 = 1
                AlphaRef: u8 = 0
                MiscRenderFlags: u8 = 1
                IsGroundLayer: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 700, 430, 180 }
                }
                Scale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0.85, 0.8, 0.85 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Mis_Beam_1_01.tex"
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.1
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    3
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Temp_GroundGlow6"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -350, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.7400015, 0.7400015, 0.7400015, 0.68999773 }
                }
                Pass: i16 = -3
                AlphaRef: u8 = 0
                MiscRenderFlags: u8 = 1
                IsGroundLayer: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 700, 430, 180 }
                }
                Scale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0.85, 0.8, 0.85 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_07.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_06.tex"
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = 180
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Projected23"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -15, 102 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.8901961, 0.5019608, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 0.8901961, 0.5019608, 0 }
                            { 1, 0.8901961, 0.5019608, 1 }
                            { 1, 0.8901961, 0.5019608, 1 }
                            { 1, 0.8901961, 0.5019608, 1 }
                        }
                    }
                }
                Pass: i16 = 4
                MeshRenderFlags: u8 = 0
                AlphaRef: u8 = 0
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 90, 50 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.4
                            0.6
                            0.75
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.2, 1, 0.2 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_splash_ring_Mask_1_1_011_3.tex"
                UvRotation: embed = ValueFloat {
                    ConstantValue: f32 = 180
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Trail_01_7.tex"
                    TexAddressModeMult: u8 = 2
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = 180
                    }
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, 1.1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Projected24"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 30, 102 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.5000076 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.7000076 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.014
                            0.018
                            0.025
                            0.1
                            0.7
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0.7000076 }
                        }
                    }
                }
                Pass: i16 = 4
                MeshRenderFlags: u8 = 0
                AlphaRef: u8 = 0
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 100, 700 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0.08
                            0.018
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_splash_ring_Mask_1_1_011_3.tex"
                UvRotation: embed = ValueFloat {
                    ConstantValue: f32 = 180
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_splash_ring_Mask_2_01.tex"
                    TexAddressModeMult: u8 = 2
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = 180
                    }
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, 1.1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.55
                }
                ParticleLinger: option[f32] = {
                    0.6
                }
                Lifetime: option[f32] = {
                    50
                }
                RateByVelocityFunction: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.1, 0.1 }
                }
                EmitterName: string = "Trail_BG9"
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -100, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -100, 0 }
                        }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 25, 35, 100 }
                }
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 1500
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 850, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.4 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.02
                            0.9
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0.32 }
                            { 1, 1, 1, 0.32 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.15
                            0.25
                            0.4
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 0.30980393, 0.9647059, 1, 0 }
                            { 0.2399939, 0.7600061, 1, 0.37999544 }
                            { 0.2901961, 0.57254905, 1, 0.6784314 }
                            { 0.33000687, 0.37000075, 1, 0.4500038 }
                            { 0.2500038, 0.30000764, 1, 0.22000457 }
                            { 0.101960786, 0.101960786, 0.36862746, 0 }
                        }
                    }
                }
                Pass: i16 = 4
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                1
                            }
                            Values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.25
                    ErosionFeatherOut: f32 = 0.25
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsGroundLayer: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 120, 1, 1 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.014
                            0.016
                            0.02
                            1
                        }
                        Values: list[vec3] = {
                            { 102, 0, 0 }
                            { 102, 1, 1 }
                            { 120, 0, 0 }
                            { 120, 0, 0 }
                            { 120, 0, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 0.5 }
                            { 0.4, 0.5, 0.5 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_08.tex"
                EmitterUvScrollRate: vec2 = { 0.15, 0 }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/W_Mis_Water_1_01111.tex"
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = 90
                    }
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, 80 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.1
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Conemesh_5"
                Velocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -70, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.0121
                            0.015
                            0.016
                        }
                        Values: list[vec3] = {
                            { 0, -7, 0 }
                            { 0, -70, 0 }
                            { 0, -70, 0 }
                            { 0, -0, 0 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -155, 100 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin62_Q_dash_half_sphere.scb"
                    }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.60784316, 0.12941177, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.013
                            0.015
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 0.48389083, 0.041614763, 0 }
                            { 1, 0.60784316, 0.12941177, 1 }
                            { 1, 0.60784316, 0.12941177, 1 }
                        }
                    }
                }
                Pass: i16 = 100
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    BeginIn: f32 = 20
                    DeltaIn: f32 = 10
                }
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        ConstantValue: f32 = 0
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                1
                            }
                            Values: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Shyvana_Base_E_ErosionLoweRes.tex"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    ErosionMapAddressMode: u8 = 0
                }
                MiscRenderFlags: u8 = 1
                ParticleIsLocalOrientation: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 90, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1.7, 5, 1.7 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.012
                            0.015
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1.2, 1.2, 1.3 }
                            { 1.2, 1.2, 1.3 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/3026_Items_color01.tex"
                BirthUvoffset: embed = ValueVector2 {
                    ConstantValue: vec2 = { -0.25, 0.5 }
                }
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 0, -3 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 0, -3 }
                        }
                    }
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Gradient03_02.tex"
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 2, 1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Missle16"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -50, 100 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skl"
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.49411765, 0.03529412, 0.03529412, 1 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.012
                            0.015
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 105
                DepthBiasFactors: vec2 = { -1, -100 }
                DoesCastShadow: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -95, 180, 0 }
                }
                Rotation0: embed = IntegratedValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.002
                            0.01
                            0.014
                            0.018
                            0.019
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 4, 4, 4 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.004
                            0.012
                            0.014
                            0.016
                            0.02
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.0053098, 1.0053098, 1.0053098 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 0.2 }
                            { 0.5, 0.5, 1.25 }
                            { 1.2, 1.2, 1.2 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Mask_Pufferfish_3_01.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Missle17"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -50, 100 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skl"
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.078431375, 0.078431375, 1 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.012
                            0.015
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 106
                DepthBiasFactors: vec2 = { -1, -100 }
                DoesCastShadow: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -95, 180, 0 }
                }
                Rotation0: embed = IntegratedValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.002
                            0.01
                            0.014
                            0.018
                            0.019
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 4, 4, 4 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.004
                            0.012
                            0.014
                            0.016
                            0.02
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.0053098, 1.0053098, 1.0053098 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 0.2 }
                            { 0.5, 0.5, 1.25 }
                            { 1.2, 1.2, 1.2 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Mask_Pufferfish_3_01.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Shared/Particles/Augment_Mercy_WispMult.tex"
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 0.5 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 100
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.6
                }
                ParticleLinger: option[f32] = {
                    0.25
                }
                Lifetime: option[f32] = {
                    50
                }
                EmitterName: string = "L_Edge4"
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 2, 0, 2 }
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { -150, 0, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 80, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 700, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.2 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.001
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.2 }
                            { 1, 1, 1, 0.2 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.2
                            0.4
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.2 }
                            { 1, 1, 1, 1 }
                            { 0.2901961, 0.59607846, 1, 0.3019608 }
                            { 0.20784314, 0.28627452, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 1
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                1
                            }
                            Values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    ErosionFeatherOut: f32 = 0.3
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_R_Water03.tex"
                }
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsGroundLayer: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 50, 50, 0 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        Values: list[vec3] = {
                            { 0.2, 1, 1 }
                            { 1, 1, 1 }
                            { 0.2, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Ashe_Skin43_R_Water03.tex"
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.3, 0 }
                }
                BirthUvoffset: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.5, 0 }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.08
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Projected25"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -30, 100 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.6 }
                }
                Pass: i16 = -2
                MeshRenderFlags: u8 = 0
                AlphaRef: u8 = 0
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 420, 700, 700 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            5e-04
                            1
                        }
                        Values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Glow.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_mis_Mask_Color_6_8.tex"
                    TexAddressModeMult: u8 = 2
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = 180
                    }
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, 0.8 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.1
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Conemesh_8"
                Velocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -70, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.0121
                            0.015
                            0.016
                        }
                        Values: list[vec3] = {
                            { 0, -7, 0 }
                            { 0, -70, 0 }
                            { 0, -70, 0 }
                            { 0, -0, 0 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -155, 100 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin62_Q_dash_half_sphere.scb"
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.7411765, 0.22352941, 1 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.013
                            0.015
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 0.79607844, 0.32156864, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 322
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    BeginIn: f32 = 20
                    DeltaIn: f32 = 10
                }
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        ConstantValue: f32 = 0
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                1
                            }
                            Values: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Shyvana_Base_E_ErosionLoweRes.tex"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    ErosionMapAddressMode: u8 = 0
                }
                MiscRenderFlags: u8 = 1
                ParticleIsLocalOrientation: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 90, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1.7, 5, 1.7 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.012
                            0.015
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1.2, 1.2, 1.3 }
                            { 1.2, 1.2, 1.3 }
                        }
                    }
                }
                Texture: string = "ASSETS/Shared/Particles/3026_Items_Streaks.tex"
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0, 0.55 }
                }
                BirthUvoffset: embed = ValueVector2 {
                    ConstantValue: vec2 = { -0.25, 0.5 }
                }
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 0.25, 3 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            0.5
                        }
                        Values: list[vec2] = {
                            { 0.25, 6 }
                            { 0.25, 6 }
                            { 0.25, 6 }
                        }
                    }
                }
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { 1, -1.5 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec2] = {
                            { 1, -1.5 }
                            { 1, -0.75 }
                            { 1, -1.5 }
                        }
                    }
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Yone_Skin26_Air_Swoosh.tex"
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = 180
                    }
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 3, 1 }
                    }
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 5 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.1
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Conemesh_10"
                Velocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -70, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.0121
                            0.015
                            0.016
                        }
                        Values: list[vec3] = {
                            { 0, -7, 0 }
                            { 0, -70, 0 }
                            { 0, -70, 0 }
                            { 0, -0, 0 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -155, 100 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin62_Q_dash_half_sphere.scb"
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.83137256, 0.40392157, 0.61960787 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.013
                            0.015
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 0.79607844, 0.32156864, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 322
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    BeginIn: f32 = 20
                    DeltaIn: f32 = 10
                }
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        ConstantValue: f32 = 0
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                1
                            }
                            Values: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Shyvana_Base_E_ErosionLoweRes.tex"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    ErosionMapAddressMode: u8 = 0
                }
                MiscRenderFlags: u8 = 1
                ParticleIsLocalOrientation: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 90, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1.7, 5, 1.7 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.012
                            0.015
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1.2, 1.2, 1.3 }
                            { 1.2, 1.2, 1.3 }
                        }
                    }
                }
                Texture: string = "ASSETS/Shared/Particles/3026_Items_Streaks.tex"
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0, 0.55 }
                }
                BirthUvoffset: embed = ValueVector2 {
                    ConstantValue: vec2 = { -0.25, 0.5 }
                }
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 0, 3 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            0.5
                        }
                        Values: list[vec2] = {
                            { 0, 6 }
                            { 0, 6 }
                            { 0, 6 }
                        }
                    }
                }
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { 1, -1.5 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec2] = {
                            { 1, -1.5 }
                            { 1, -0.75 }
                            { 1, -1.5 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.05
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.2
                }
                ParticleLinger: option[f32] = {
                    2
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "shockwaves_out5"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -1700, 0 }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 10, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 100 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_Splash_1_002.scb"
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.7000076 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.6431373, 0.827451, 0.9529412, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.09374067
                            0.22703832
                            0.69844985
                            1
                        }
                        Values: list[vec4] = {
                            { 0.6431373, 0.827451, 0.9529412, 0 }
                            { 0.6431373, 0.827451, 0.9529412, 0.78547853 }
                            { 0.6431373, 0.827451, 0.9529412, 0.3257918 }
                            { 0.6431373, 0.827451, 0.9529412, 0.09722295 }
                            { 0.6431373, 0.827451, 0.9529412, 0 }
                        }
                    }
                }
                Pass: i16 = 900
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 80
                }
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                0.1388889
                                0.5148148
                                1
                            }
                            Values: list[f32] = {
                                0.1
                                0.18187252
                                0.70956177
                                2
                            }
                        }
                    }
                    ErosionFeatherOut: f32 = 0.15
                    ErosionSliceWidth: f32 = 1
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_6655_Items_stack_3.tex"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 1, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                Rotation0: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -3, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.35
                            0.5
                        }
                        Values: list[vec3] = {
                            { 0, -3, 0 }
                            { 0, -0.3, 0 }
                            { 0, -0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 60, 100 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.34444445
                            1
                        }
                        Values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 1.1, 1.1, 1.1 }
                            { 1.4, 2, 1.4 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_T2_dea_55.tex"
                TexDiv: vec2 = { 0.5, 1 }
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { -2, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                            0.30370373
                            0.5
                        }
                        Values: list[vec2] = {
                            { -4, 0 }
                            { -0.79402393, 0 }
                            { -0, 0 }
                        }
                    }
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_splash_ring_1_01_1.tex"
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, -1.5 }
                    }
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { -1, 0.3 }
                        Dynamics: pointer = VfxAnimatedVector2fVariableData {
                            Times: list[f32] = {
                                0
                                0.2
                                1
                            }
                            Values: list[vec2] = {
                                { -1, 0.3 }
                                { -1, 0 }
                                { -1, 0 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.05
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.85
                }
                ParticleLinger: option[f32] = {
                    2
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "shockwaves_out6"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -700, 0 }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 10, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 100, 100 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_Splash_1_002.scb"
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.6 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.6431373, 0.827451, 0.9529412, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.09374067
                            0.22703832
                            0.69844985
                            1
                        }
                        Values: list[vec4] = {
                            { 0.6431373, 0.827451, 0.9529412, 0 }
                            { 0.6431373, 0.827451, 0.9529412, 1 }
                            { 0.6431373, 0.827451, 0.9529412, 0.3257918 }
                            { 0.6431373, 0.827451, 0.9529412, 0.09722295 }
                            { 0.6431373, 0.827451, 0.9529412, 0 }
                        }
                    }
                }
                Pass: i16 = 900
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 80
                }
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                0.1388889
                                0.5148148
                                1
                            }
                            Values: list[f32] = {
                                0.1
                                0.18187252
                                0.70956177
                                2
                            }
                        }
                    }
                    ErosionFeatherOut: f32 = 0.15
                    ErosionSliceWidth: f32 = 1
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Irelia_Skin18_Q_Erode.tex"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 1, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                Rotation0: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, 0.5, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.35
                            0.5
                        }
                        Values: list[vec3] = {
                            { 0, 0.5, 0 }
                            { 0, 0.05, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 65, 60, 65 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.34444445
                            1
                        }
                        Values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 1.02, 1.1, 1.02 }
                            { 1.4, 2, 1.4 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_T2_dea_55.tex"
                TexDiv: vec2 = { 0.5, 1 }
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { -2, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                            0.30370373
                            0.5
                        }
                        Values: list[vec2] = {
                            { -4, 0 }
                            { -0.79402393, 0 }
                            { -0, 0 }
                        }
                    }
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_splash_ring_1_01_1.tex"
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, -1.5 }
                    }
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { -1, 0.2 }
                        Dynamics: pointer = VfxAnimatedVector2fVariableData {
                            Times: list[f32] = {
                                0
                                0.2
                                1
                            }
                            Values: list[vec2] = {
                                { -1, 0.2 }
                                { -1, 0 }
                                { -1, 0 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Missle18"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -50, 100 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skl"
                    }
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.012
                            0.015
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 102
                DepthBiasFactors: vec2 = { -1, -100 }
                DoesCastShadow: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -95, 180, 0 }
                }
                Rotation0: embed = IntegratedValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.002
                            0.01
                            0.014
                            0.018
                            0.019
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 4, 4, 4 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.004
                            0.012
                            0.014
                            0.016
                            0.02
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.0053098, 1.0053098, 1.0053098 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 0.2 }
                            { 0.5, 0.5, 1.25 }
                            { 1.2, 1.2, 1.2 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_R_mis_globefish.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Missle19"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -50, 100 }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { -2, 0, 0 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_Splash_1_004.scb"
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0, 0, 1 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.014
                            0.018
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 801
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    BeginIn: f32 = 20
                    DeltaIn: f32 = 10
                }
                DepthBiasFactors: vec2 = { -1, -100 }
                MiscRenderFlags: u8 = 1
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -95, 180, 0 }
                }
                Rotation0: embed = IntegratedValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.002
                            0.01
                            0.014
                            0.018
                            0.019
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 4, 4, 4 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.004
                            0.012
                            0.014
                            0.016
                            0.02
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.0053098, 1.0053098, 1.0053098 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 0.2 }
                            { 0.5, 0.5, 1.25 }
                            { 1.2, 1.2, 1.2 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_mis_Mask_Color_6_011.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Shared/Particles/3026_Items_Noise_02.tex"
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Missle20"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -50, 100 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skl"
                    }
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.012
                            0.015
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 102
                DepthBiasFactors: vec2 = { -1, -100 }
                DoesCastShadow: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -95, 180, 0 }
                }
                Rotation0: embed = IntegratedValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.002
                            0.01
                            0.014
                            0.018
                            0.019
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 4, 4, 4 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.004
                            0.012
                            0.014
                            0.016
                            0.02
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.0053098, 1.0053098, 1.0053098 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 0.2 }
                            { 0.5, 0.5, 1.25 }
                            { 1.2, 1.2, 1.2 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_R_mis_globefish_3_1.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Missle22"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -50, 100 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_01_1.skl"
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.6862745, 0.6862745, 0.6862745, 1 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.012
                            0.015
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 103
                DepthBiasFactors: vec2 = { -1, -100 }
                DoesCastShadow: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -95, 180, 0 }
                }
                Rotation0: embed = IntegratedValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.002
                            0.01
                            0.014
                            0.018
                            0.019
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 4, 4, 4 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.004
                            0.012
                            0.014
                            0.016
                            0.02
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.0053098, 1.0053098, 1.0053098 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 0.2 }
                            { 0.5, 0.5, 1.25 }
                            { 1.2, 1.2, 1.2 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_R_mis_globefish_3_1.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_Mask_3_12.tex"
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.55
                }
                ParticleLinger: option[f32] = {
                    0.6
                }
                Lifetime: option[f32] = {
                    50
                }
                RateByVelocityFunction: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.1, 0.1 }
                }
                EmitterName: string = "Trail_BG10"
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -100, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -100, 0 }
                        }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 25, 50, 100 }
                }
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 1500
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 800, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.4 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.9
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.15
                            0.25
                            0.4
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 0.23529412, 0.9882353, 1, 0 }
                            { 0.28000304, 0.77000076, 1, 0 }
                            { 0.30588236, 0.49019608, 1, 0 }
                            { 0.29411766, 0.48235294, 1, 0 }
                            { 0.2399939, 0.34000152, 1, 0 }
                            { 0.11764706, 0.1254902, 0.5647059, 0 }
                        }
                    }
                }
                Pass: i16 = 3
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                1
                            }
                            Values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.25
                    ErosionFeatherOut: f32 = 0.25
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsGroundLayer: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 120, 1, 1 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.014
                            0.016
                            0.02
                            1
                        }
                        Values: list[vec3] = {
                            { 102, 0, 0 }
                            { 102, 1, 1 }
                            { 120, 0, 0 }
                            { 120, 0, 0 }
                            { 120, 0, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 0.5 }
                            { 0.3, 0.5, 0.5 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_08.tex"
                EmitterUvScrollRate: vec2 = { 0.15, 0 }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.4
                }
                ParticleLinger: option[f32] = {
                    0.6
                }
                Lifetime: option[f32] = {
                    50
                }
                RateByVelocityFunction: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.1, 0.1 }
                }
                EmitterName: string = "Trail_BG11"
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { -30, 20, 100 }
                }
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 1500
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 450, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.4 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.9
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.15
                            0.35
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 0.30980393, 0.49411765, 0 }
                            { 0.8235294, 0.28627452, 1, 0 }
                            { 0.5803922, 0.2784314, 1, 0 }
                            { 0.37000075, 0.3100023, 1, 0 }
                            { 0.023529412, 0.23529412, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 3
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        ConstantValue: f32 = 0
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                1
                            }
                            Values: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.25
                    ErosionFeatherOut: f32 = 0.25
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsGroundLayer: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 105, 1, 1 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.014
                            0.016
                            0.02
                            1
                        }
                        Values: list[vec3] = {
                            { 89.25, 0, 0 }
                            { 89.25, 1, 1 }
                            { 105, 0, 0 }
                            { 105, 0, 0 }
                            { 105, 0, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            1
                        }
                        Values: list[vec3] = {
                            { 0.8, 1, 1 }
                            { 1, 1, 1 }
                            { 0.4, 0.2, 0.2 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_09.tex"
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 0.05, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 0.05, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.05
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 16
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        Times: list[f32] = {
                            0
                            0.018
                            0.025
                        }
                        Values: list[f32] = {
                            8
                            16
                            16
                        }
                    }
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.55
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.2
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.55
                        }
                    }
                }
                Lifetime: option[f32] = {
                    50
                }
                EmitterName: string = "Swirls"
                Importance: u8 = 3
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -350, 0 }
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 0, 100 }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -90, 0 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin13_R_CometSwirlMesh.scb"
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        Values: list[vec4] = {
                            { 0.14901961, 0.92941177, 1, 1 }
                            { 0.16470589, 0.5411765, 1, 1 }
                            { 0.023529412, 0.05490196, 0.36862746, 0 }
                        }
                    }
                }
                Pass: i16 = 40
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                1
                            }
                            Values: list[f32] = {
                                0
                                0.5
                            }
                        }
                    }
                    ErosionMapName: string = "ASSETS/Shared/Particles/Base_SmokeErosionT.tex"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 1, 0 }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 50, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1.4, 1.4, 1.3 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1.4, 1.4, 1.3 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        Values: list[vec3] = {
                            { 1.8, 1.8, 1.8 }
                            { 2.8, 2.8, 2.8 }
                            { 4, 4, 4 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_mis_Mask_Color_6_01.tex"
                BirthUvoffset: embed = ValueVector2 {
                    ConstantValue: vec2 = { 1, 1 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -0.5
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -0.5
                                    0.5
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
            }
        }
        VisibilityRadius: f32 = 1e+05
        ParticleName: string = "Jinx_Skin66_R_Mis"
        ParticlePath: string = "Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_R_Mis"
        SoundPersistentDefault: string = "Play_sfx_Jinx_JinxR_missilelaunch"
        Flags: u16 = 213
        ObjectPath: hash = 0x55c9e65b
    }
    0x989b246f = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 32
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            32
                        }
                    }
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.75
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.75
                        }
                    }
                }
                EmitterName: string = "Basic1"
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -10, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -10, 0 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    Flags: u8 = 1
                    Size: vec3 = { 8, 8, 15 }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.27041095
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 0.15294118, 0.16862746, 1, 0 }
                            { 0.13333334, 0.1764706, 1, 1 }
                            { 0.29411766, 0.90588236, 1, 1 }
                            { 0.1254902, 0.35686275, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 901
                AlphaRef: u8 = 0
                0xcb13aff1: f32 = -2
                IsUniformScale: flag = true
                IsRotationEnabled: flag = true
                UseNavmeshMask: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    360
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 4, 10, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.3
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 4, 10, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.44716242
                            1
                        }
                        Values: list[vec3] = {
                            { 0.49839142, 0, 0 }
                            { 0.6608579, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Dance_Sparks.tex"
            }
        }
        ParticleName: string = "Jinx_Skin66_Idle_Header"
        ParticlePath: string = "Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Idle_Header"
        ScaleDynamicallyWithAttachedBone: bool = true
        ObjectPath: hash = 0x989b246f
    }
    0xa408b903 = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = -1
                }
                ParticleLinger: option[f32] = {
                    0.15
                }
                IsSingleParticle: flag = true
                ChildParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    ChildrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            EffectKey: hash = 0x62333d7e
                        }
                    }
                }
                EmitterName: string = "Flash"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 15, 5, 5 }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.3
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 0.7100023, 0.13000686, 0.6 }
                            { 1, 1, 1, 1 }
                            { 0.8627451, 0.36078432, 1, 0.3019608 }
                            { 0.48235294, 0.13725491, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 150
                AlphaRef: u8 = 0
                MiscRenderFlags: u8 = 1
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 90, 0 }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 350, 350 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        Values: list[vec3] = {
                            { 0.42629483, 0, 0 }
                            { 1.5, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Camille_Skin44_Q_Hex_Indicator_1_1_007.tex"
            }
        }
        ParticleName: string = "Jinx_Skin66_Idle_Header_01"
        ParticlePath: string = "Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Idle_Header_01"
        ScaleDynamicallyWithAttachedBone: bool = true
        ObjectPath: hash = 0xa408b903
    }
    0xa508ba96 = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = -1
                }
                ParticleLinger: option[f32] = {
                    0.15
                }
                IsSingleParticle: flag = true
                ChildParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    ChildrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            EffectKey: hash = 0x62333d7e
                        }
                    }
                }
                EmitterName: string = "Flash"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { -15, -5, -10 }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.3
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 0.7100023, 0.13000686, 0.6 }
                            { 1, 1, 1, 1 }
                            { 0.8627451, 0.36078432, 1, 0.3019608 }
                            { 0.48235294, 0.13725491, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 150
                AlphaRef: u8 = 0
                MiscRenderFlags: u8 = 1
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 125, 0, 0 }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 350, 350 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        Values: list[vec3] = {
                            { 0.42629483, 0, 0 }
                            { 1.5, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Camille_Skin44_Q_Hex_Indicator_1_1_007.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Caitlyn_Skin51_BA_Color03.tex"
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = 1
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            ProbabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    KeyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    KeyValues: list[f32] = {
                                        -360
                                        1
                                    }
                                }
                            }
                            Times: list[f32] = {
                                0
                            }
                            Values: list[f32] = {
                                1
                            }
                        }
                    }
                }
            }
        }
        ParticleName: string = "Jinx_Skin66_Idle_Header_02"
        ParticlePath: string = "Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Idle_Header_02"
        ScaleDynamicallyWithAttachedBone: bool = true
        ObjectPath: hash = 0xa508ba96
    }
    0xc968f3f2 = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.35
                }
                ParticleLinger: option[f32] = {
                    0.2
                }
                Lifetime: option[f32] = {
                    2
                }
                EmitterName: string = "TrailAdd"
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 400, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.8
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.4
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 0.4899977, 0.88000304, 0.4 }
                            { 0.28235295, 0.02745098, 0.40784314, 0 }
                        }
                    }
                }
                Pass: i16 = 50
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 50
                }
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 85, 50, 50 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec3] = {
                            { 0.6, 1, 1 }
                            { 0.3, 1, 1 }
                            { 0.15, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_E_Trail_01.tex"
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 0.5, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 0.5, 0 }
                        }
                    }
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Radialring_01_04113.tex"
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 16
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.2
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    0.7
                                    1.2
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            1.2
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    1
                }
                Lifetime: option[f32] = {
                    1
                }
                EmitterName: string = "SparklesFast"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 200, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.3
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 200, 0, 0 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 5, 5, 5 }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -600, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -600, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeSphere {
                    Flags: u8 = 1
                    Radius: f32 = 10
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -10, -5 }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.9000076 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.6
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.9000076 }
                            { 0.192157, 1, 0.827451, 0.9000076 }
                            { 1, 0, 0.682353, 0.9000076 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        Values: list[vec4] = {
                            { 0.23921569, 0.8352941, 1, 1 }
                            { 0.24313726, 0.7607843, 1, 1 }
                            { 0.13725491, 0.30588236, 0.85490197, 1 }
                        }
                    }
                }
                Pass: i16 = -10
                ColorLookUpTypeY: u8 = 3
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 30
                }
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 10, 35, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 10, 35, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.2
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.2, 2, 0 }
                            { 0.8, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Zeri_Skin10_Q_Bubble01.tex"
                NumFrames: u16 = 4
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.03
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.5
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "FlameGlow"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 30, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.4 }
                }
                Pass: i16 = 150
                AlphaRef: u8 = 0
                MiscRenderFlags: u8 = 1
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 80, 100, 0 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin62_Alpha_Backdrop.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_splash_ring_Mask_2_01.tex"
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = -90
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Lifetime: option[f32] = {
                    1.85
                }
                IsSingleParticle: flag = true
                EmitterName: string = "feather"
                Importance: u8 = 3
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0.01, 0 }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -30, 0 }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.4 }
                }
                Pass: i16 = -50
                AlphaRef: u8 = 0
                IsDirectionOriented: flag = true
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                IsRotationEnabled: flag = true
                DirectionVelocityScale: f32 = 0.001
                DirectionVelocityMinScale: f32 = 1.5
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 25, 1.26 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Soraka_ball32_02.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_mis_Mask_Color_6_8.tex"
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = 180
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.03
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 2
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "FrontWaveBLUE"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 60, 0 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/MissFortune_Skin21_RQ_Mesh_Core.scb"
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.7600061, 0.34999618, 0.6 }
                }
                Pass: i16 = 15
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 360, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 360, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 2.3, 1 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/MissFortune_Skin21_BA_9571.tex"
                BirthUvoffset: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0, 0.1 }
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/MissFortune_Skin21_Dance_Einstein_01_mult.tex"
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 2, 1 }
                    }
                    ParticleIntegratedUvScrollMult: embed = IntegratedValueVector2 {
                        ConstantValue: vec2 = { 0, -3 }
                        Dynamics: pointer = VfxAnimatedVector2fVariableData {
                            Times: list[f32] = {
                                0
                            }
                            Values: list[vec2] = {
                                { 0, -3 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.4
                }
                ParticleLinger: option[f32] = {
                    0.1
                }
                Lifetime: option[f32] = {
                    1
                }
                RateByVelocityFunction: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.1, 0.1 }
                }
                EmitterName: string = "Trail_BG"
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -200, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -200, 0 }
                        }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { -5, -20, 0 }
                }
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 1500
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 780, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.5000076 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.9
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.5000076 }
                            { 1, 1, 1, 0.5000076 }
                            { 1, 1, 1, 0.5000076 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.15
                            0.3
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 0.21568628, 0.7254902, 1, 0 }
                            { 0.13333334, 0.46666667, 1, 0.6117647 }
                            { 0.5400015, 0.17000076, 1, 0.34000152 }
                            { 0.77999544, 0.11000229, 1, 0.2 }
                            { 0.64705884, 0.24313726, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 7
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                1
                            }
                            Values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.25
                    ErosionFeatherOut: f32 = 0.25
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 70, 1, 1 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            1
                        }
                        Values: list[vec3] = {
                            { 0.85, 1, 0.5 }
                            { 0.9, 1, 1 }
                            { 0.4, 0.5, 0.5 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Mis_music_1_01_13.tex"
                EmitterUvScrollRate: vec2 = { -0.2, 0 }
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { -1, 1 }
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/W_Mis_Water_1_01111.tex"
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = 90
                    }
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, 100 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.4
                }
                ParticleLinger: option[f32] = {
                    0.1
                }
                Lifetime: option[f32] = {
                    1
                }
                RateByVelocityFunction: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.1, 0.1 }
                }
                EmitterName: string = "Trail_BG1"
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -200, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -200, 0 }
                        }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { -5, -20, 0 }
                }
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 1500
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 780, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.8899977, 0.46999314, 1, 0.3100023 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.9
                            1
                        }
                        Values: list[vec4] = {
                            { 0.8899977, 0.46999314, 1, 0 }
                            { 0.8899977, 0.46999314, 1, 0.3100023 }
                            { 0.8899977, 0.46999314, 1, 0.3100023 }
                            { 0.8899977, 0.46999314, 1, 0.3100023 }
                            { 0.8899977, 0.46999314, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.7000076 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.15
                            0.3
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.12627588 }
                            { 1, 1, 1, 0.4611815 }
                            { 0.5100023, 0.2, 0.8899977, 0.08399878 }
                            { 0.34509805, 0.105882354, 0.6156863, 0 }
                        }
                    }
                }
                Pass: i16 = 6
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                1
                            }
                            Values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.25
                    ErosionFeatherOut: f32 = 0.25
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 1, 1 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            1
                        }
                        Values: list[vec3] = {
                            { 0.85, 1, 0.5 }
                            { 0.9, 1, 1 }
                            { 0.4, 0.5, 0.5 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Mis_music_1_01_13.tex"
                EmitterUvScrollRate: vec2 = { -0.2, 0 }
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { -1, 1 }
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Caitlyn_Skin51_AnimeShapes061.tex"
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.25
                }
                ParticleLinger: option[f32] = {
                    0.1
                }
                Lifetime: option[f32] = {
                    1
                }
                RateByVelocityFunction: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.1, 0.1 }
                }
                EmitterName: string = "Trail_BG2"
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { -50, 0, 0 }
                }
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 1500
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 450, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.4 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.9
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.15
                            0.3
                            0.65
                            1
                        }
                        Values: list[vec4] = {
                            { 0.73333335, 0.3647059, 1, 0 }
                            { 0.6200046, 0.14999619, 1, 0.30000764 }
                            { 0.39000535, 0.20999466, 1, 0.59000534 }
                            { 0.2, 0.30000764, 0.8399939, 0.22999924 }
                            { 0.05882353, 0.21960784, 0.5647059, 0 }
                        }
                    }
                }
                Pass: i16 = 7
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        ConstantValue: f32 = 0
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                1
                            }
                            Values: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.25
                    ErosionFeatherOut: f32 = 0.25
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -100, 1, 1 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            1
                        }
                        Values: list[vec3] = {
                            { 0.9, 1, 1 }
                            { 1, 1, 1 }
                            { 0.4, 0.2, 0.2 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Mis_music_1_01_14.tex"
                EmitterUvScrollRate: vec2 = { 0.25, 0 }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/W_Mis_Water_1_01111.tex"
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = 90
                    }
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, 70 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.25
                }
                ParticleLinger: option[f32] = {
                    0.1
                }
                Lifetime: option[f32] = {
                    1
                }
                RateByVelocityFunction: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.1, 0.1 }
                }
                EmitterName: string = "Trail_BG3"
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { -50, 0, 0 }
                }
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 1500
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 450, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.6431373, 0.46666667, 1, 0.5019608 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.001
                            0.002
                            0.01
                            0.9
                            1
                        }
                        Values: list[vec4] = {
                            { 0.6431373, 0.46666667, 1, 0 }
                            { 0.6431373, 0.46666667, 1, 0.5019608 }
                            { 0.6431373, 0.46666667, 1, 0.5019608 }
                            { 0.6431373, 0.46666667, 1, 0.5019608 }
                            { 0.6431373, 0.46666667, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.7000076 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.15
                            0.3
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.16196255 }
                            { 1, 1, 1, 0.40627894 }
                            { 1, 1, 1, 0.08509897 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 6
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        ConstantValue: f32 = 0
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                1
                            }
                            Values: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.25
                    ErosionFeatherOut: f32 = 0.25
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -100, 1, 1 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            1
                        }
                        Values: list[vec3] = {
                            { 0.9, 1, 1 }
                            { 1, 1, 1 }
                            { 0.4, 0.2, 0.2 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Mis_music_1_01_14.tex"
                EmitterUvScrollRate: vec2 = { 0.25, 0 }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_R_mis_globefish_Mask_1_1_01.tex"
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.03
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "DarkBG"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -45, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.09803922, 0.5647059, 1, 0.7019608 }
                }
                AlphaRef: u8 = 0
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 80, 0 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/MissFortune_Skin69_MisLead_Mask.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/MissFortune_Skin69_E_Screen_Flames_Soft.tex"
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 2, 1 }
                    }
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, -3 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "SoftHead"
                RotationOverride: vec3 = { 0, 0, 90 }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { -70, 0, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.4627451, 0.32156864, 0.8862745, 1 }
                }
                Pass: i16 = -10
                AlphaRef: u8 = 0
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, -90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 30, 80, 0 }
                }
                Scale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1.3, 1.3, 1 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/W_Beam_EPassive_03_1_1_2.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.4
                }
                ParticleLinger: option[f32] = {
                    0.5
                }
                Lifetime: option[f32] = {
                    2
                }
                EmitterName: string = "TrailBlend2"
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 20, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 300, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.7000076 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.05
                            0.8
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.2
                            0.3
                            0.60182154
                            1
                        }
                        Values: list[vec4] = {
                            { 0.27450982, 0.78431374, 1, 0 }
                            { 0.28000304, 0.6, 1, 0.4 }
                            { 0.25882354, 0.45490196, 1, 0.83137256 }
                            { 0.27450982, 0.38039216, 0.9882353, 0.65882355 }
                            { 0.34117648, 0.21568628, 0.84313726, 0.34117648 }
                            { 0.34117648, 0.105882354, 0.6313726, 0 }
                        }
                    }
                }
                Pass: i16 = -2
                IsUniformScale: flag = true
                ParticlesShareRandomValue: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 32, 1, 1 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.6, 1, 1 }
                            { 0.2, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Q_Trail_fill.tex"
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.3, 0 }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.45
                }
                ParticleLinger: option[f32] = {
                    0.5
                }
                Lifetime: option[f32] = {
                    2
                }
                EmitterName: string = "TrailBlend3"
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -200, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -200, 0 }
                        }
                    }
                }
                Primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 500, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.8899977 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.05
                            0.8
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.8899977 }
                            { 1, 1, 1, 0.8899977 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.12
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 0.21568628, 0.4509804, 1, 0 }
                            { 0.22745098, 0.49803922, 1, 0.85882354 }
                            { 0.28000304, 0.20999466, 0.8200046, 0.5499962 }
                            { 0.3137255, 0.13725491, 0.5647059, 0 }
                        }
                    }
                }
                Pass: i16 = -4
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0.2
                                1
                            }
                            Values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.25
                    ErosionFeatherOut: f32 = 0.25
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                IsUniformScale: flag = true
                ParticlesShareRandomValue: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 65, 1, 1 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.4
                            1
                        }
                        Values: list[vec3] = {
                            { 0.8, 0.7, 0.7 }
                            { 1, 1, 1 }
                            { 1.3, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Aurora_Skin20_Comet_Trail_01.tex"
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 0.3, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 0.3, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.2
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    2
                }
                EmitterName: string = "TrailAdd6"
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 320, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.05
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.15
                            0.35
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 0.2784314, 0.8784314, 1, 0 }
                            { 0.2784314, 0.78431374, 1, 1 }
                            { 0.25490198, 0.47843137, 1, 1 }
                            { 0.26999313, 0.37000075, 1, 0.5000076 }
                            { 0.4, 0.2, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 2
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 50
                }
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 24, 50, 50 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1.5 }
                            { 0.1, 1.8, 1.8 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_BA_03.tex"
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 1, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.2
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    2
                }
                EmitterName: string = "TrailAdd7"
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 320, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.05
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.15
                            0.35
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 0.2784314, 0.8784314, 1, 0 }
                            { 0.25882354, 0.6431373, 1, 0.8509804 }
                            { 0.17999542, 0.33000687, 1, 0.66999316 }
                            { 0.22999924, 0.26999313, 1, 0.42999923 }
                            { 0.2, 0.14509805, 0.6117647, 0 }
                        }
                    }
                }
                Pass: i16 = 1
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 50
                }
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 24, 50, 50 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.1, 1.8, 1.8 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_BA_03.tex"
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 1, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 40
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.5
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.35
                                    1.5
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.5
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    1
                }
                Lifetime: option[f32] = {
                    50
                }
                EmitterName: string = "STARS_BACKGROUND1"
                Importance: u8 = 3
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 30, -50, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 30, -50, 0 }
                        }
                    }
                }
                Velocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 1 }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -100, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -100, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeSphere {
                    Flags: u8 = 1
                    Radius: f32 = 20
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 20, 0 }
                }
                ParticleColorTexture: string = "ASSETS/Shared/Particles/15.tex"
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.4
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 50
                ColorLookUpTypeY: u8 = 3
                DepthBiasFactors: vec2 = { -1, -18 }
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 30, 30, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 30, 30, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.4
                            0.5
                            1
                        }
                        Values: list[vec3] = {
                            { 0.6, 1, 1 }
                            { 2, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Star01.tex"
                UvMode: u8 = 2
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.03
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "bullets2"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {}
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Mis_Hand_grenade.scb"
                    }
                    AlignPitchToCamera: bool = true
                    AlignYawToCamera: bool = true
                }
                BlendMode: u8 = 3
                Pass: i16 = 80
                IsUniformScale: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 180, 90 }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 3.2, 2, 2.2 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Q_Mis_Thorn_2.tex"
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.03
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "bullets3"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {}
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Mis_Hand_grenade.scb"
                    }
                    AlignPitchToCamera: bool = true
                    AlignYawToCamera: bool = true
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.4 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.6 }
                }
                Pass: i16 = 81
                IsUniformScale: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 180, 90 }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 3.2, 2, 2.2 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Q_Mis_Thorn_2.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 2
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Projected"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -50, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                ParticleColorTexture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/color-holdhalf.tex"
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.68000305, 0.22000457, 0.5000076 }
                }
                MeshRenderFlags: u8 = 0
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -90, 0, 0 }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 350, 450, 450 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Glow.tex"
            }
        }
        ParticleName: string = "Jinx_Skin66_Q_RocketCritMis"
        ParticlePath: string = "Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Q_RocketCritMis"
        ObjectPath: hash = 0xc968f3f2
    }
    0xd9710339 = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 2
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterName: string = "Flash3"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 10, 15 }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/color-rampdown.tex"
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.43529412, 0.2627451, 1, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 0.43529412, 0.2627451, 1, 0 }
                            { 0.43529412, 0.2627451, 1, 1 }
                            { 0.43529412, 0.2627451, 1, 0 }
                        }
                    }
                }
                MeshRenderFlags: u8 = 0
                DepthBiasFactors: vec2 = { -1, -16 }
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 15, 105, 105 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Glow.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 2
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterName: string = "Flash4"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 10, -10 }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/color-rampdown.tex"
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.43529412, 0.2627451, 1, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 0.43529412, 0.2627451, 1, 0 }
                            { 0.43529412, 0.2627451, 1, 1 }
                            { 0.43529412, 0.2627451, 1, 0 }
                        }
                    }
                }
                MeshRenderFlags: u8 = 0
                DepthBiasFactors: vec2 = { -1, -16 }
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 15, 105, 105 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Glow.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = -1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "chain_beam6"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mLocalSpaceSourceOffset: vec3 = { 0, 7, -10 }
                        mLocalSpaceTargetOffset: vec3 = { -5, 0, -5 }
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { -1, 120, 0 }
                        }
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.5000076 }
                }
                Pass: i16 = 1
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 15, 0, 0 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_02.tex"
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { -0.2, 0 }
                }
                BirthUvoffset: embed = ValueVector2 {
                    ConstantValue: vec2 = { 1, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Idle_Beam_Mult_1_01.tex"
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = -1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "chain_beam7"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mLocalSpaceSourceOffset: vec3 = { 0, 7, 15 }
                        mLocalSpaceTargetOffset: vec3 = { -5, 0, 20 }
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { -1, 120, 0 }
                        }
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.5000076 }
                }
                Pass: i16 = 1
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 15, 0, 0 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Idle_Beam_Mult_1_02.tex"
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { -0.2, 0 }
                }
                BirthUvoffset: embed = ValueVector2 {
                    ConstantValue: vec2 = { 1, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Idle_Beam_Mult_1_01.tex"
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = -1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "chain_beam11"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mLocalSpaceSourceOffset: vec3 = { 0, 7, 15 }
                        mLocalSpaceTargetOffset: vec3 = { -5, 0, 20 }
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { -1, 100, 0 }
                        }
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.5000076 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 5, 0, 0 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin60_W_Glow_Trail.tex"
                UvRotation: embed = ValueFloat {
                    ConstantValue: f32 = 90
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Idle_Beam_Mult_1_01.tex"
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = -1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "chain_beam12"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mLocalSpaceSourceOffset: vec3 = { 0, 7, -10 }
                        mLocalSpaceTargetOffset: vec3 = { -5, 0, -5 }
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { -1, 100, 0 }
                        }
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.5000076 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 5, 0, 0 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin60_W_Glow_Trail.tex"
                UvRotation: embed = ValueFloat {
                    ConstantValue: f32 = 90
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Idle_Beam_Mult_1_01.tex"
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 16
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.5
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.4
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.5
                        }
                    }
                }
                EmitterName: string = "Flash6"
                Importance: u8 = 3
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 3, 3, 3 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -3
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 3, 3, 3 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    Flags: u8 = 1
                    Size: vec3 = { 5, 15, 36 }
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -5, -10 }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Jinx/Skins/Skin66/Particles/Seraphine_Skin66_Q_RainbowMult.tex"
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                MeshRenderFlags: u8 = 0
                AlphaRef: u8 = 0
                DepthBiasFactors: vec2 = { -1, -16 }
                0xcb13aff1: f32 = -2
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                UseNavmeshMask: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 26, 6, 6 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 26, 6, 6 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Star01.tex"
            }
        }
        ParticleName: string = "Jinx_Skin66_Idle_01Hover"
        ParticlePath: string = "Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Idle_01Hover"
        ScaleDynamicallyWithAttachedBone: bool = true
        ObjectPath: hash = 0xd9710339
    }
    0xeb39a192 = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.4
                }
                ParticleLinger: option[f32] = {
                    0.5
                }
                Lifetime: option[f32] = {
                    2
                }
                EmitterName: string = "TrailBlend2"
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 20, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 300, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.5000076 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.05
                            0.8
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.5000076 }
                            { 1, 1, 1, 0.5000076 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.86999315 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.2
                            0.3
                            0.60182154
                            1
                        }
                        Values: list[vec4] = {
                            { 0.27450982, 0.78431374, 1, 0 }
                            { 0.28000304, 0.6, 1, 0.34799725 }
                            { 0.25882354, 0.45490196, 1, 0.7232884 }
                            { 0.27450982, 0.38039216, 0.9882353, 0.573172 }
                            { 0.27450982, 0.23529412, 0.84313726, 0.2968212 }
                            { 0.29411766, 0.18039216, 0.6313726, 0 }
                        }
                    }
                }
                Pass: i16 = -2
                IsUniformScale: flag = true
                ParticlesShareRandomValue: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 35, 1, 1 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.6, 1, 1 }
                            { 0.2, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_Q_Trail_fill.tex"
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.3, 0 }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.2
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    2
                }
                EmitterName: string = "TrailAdd1"
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 320, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.05
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.15
                            0.35
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 0.2784314, 0.8784314, 1, 0 }
                            { 0.2784314, 0.78431374, 1, 1 }
                            { 0.2509804, 0.4862745, 1, 1 }
                            { 0.26999313, 0.37000075, 1, 0.5000076 }
                            { 0.4, 0.2, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 2
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 50
                }
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 23, 50, 50 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1.5 }
                            { 0.1, 1.8, 1.8 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_BA_03.tex"
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 1, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.03
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "DarkBG"
                Importance: u8 = 3
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -45, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.09803922, 0.5647059, 1, 0.7019608 }
                }
                AlphaRef: u8 = 0
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 80, 0 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/MissFortune_Skin69_MisLead_Mask.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/MissFortune_Skin69_E_Screen_Flames_Soft.tex"
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 2, 1 }
                    }
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, -3 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.03
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "bullets3"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {}
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Mis_Hand_grenade.scb"
                    }
                    AlignPitchToCamera: bool = true
                    AlignYawToCamera: bool = true
                }
                BlendMode: u8 = 3
                Pass: i16 = 80
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 180, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 3.2, 2, 2.2 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Q_Mis_Thorn_2.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.2
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    2
                }
                EmitterName: string = "TrailAdd7"
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 320, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.05
                            0.6
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.15
                            0.35
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 0.2784314, 0.8784314, 1, 0 }
                            { 0.25882354, 0.6431373, 1, 0.8509804 }
                            { 0.20392157, 0.54901963, 1, 0.67058825 }
                            { 0.22999924, 0.26999313, 1, 0.42999923 }
                            { 0.2, 0.14509805, 0.6117647, 0 }
                        }
                    }
                }
                Pass: i16 = 1
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 50
                }
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 23, 50, 50 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.1, 1.8, 1.8 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_BA_03.tex"
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 1, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.4
                }
                ParticleLinger: option[f32] = {
                    0.5
                }
                Lifetime: option[f32] = {
                    2
                }
                EmitterName: string = "TrailBlend4"
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -200, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -200, 0 }
                        }
                    }
                }
                Primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 500, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.7000076 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.05
                            0.8
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0.7000076 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.12
                            0.55
                            1
                        }
                        Values: list[vec4] = {
                            { 0.21568628, 0.4509804, 1, 0 }
                            { 0.34000152, 0.40999466, 1, 0.85999846 }
                            { 0.3100023, 0.2899977, 0.8200046, 0.6200046 }
                            { 0.3137255, 0.13725491, 0.5647059, 0 }
                        }
                    }
                }
                Pass: i16 = -4
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0.2
                                1
                            }
                            Values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.25
                    ErosionFeatherOut: f32 = 0.25
                    ErosionMapName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Lissandra_Q_Spear_Diff_2_03_3.tex"
                }
                IsUniformScale: flag = true
                ParticlesShareRandomValue: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 65, 1, 1 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.4
                            1
                        }
                        Values: list[vec3] = {
                            { 0.7, 0.7, 0.7 }
                            { 1, 1, 1 }
                            { 1.3, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Aurora_Skin20_Comet_Trail_01.tex"
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 0.3, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 0.3, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.03
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.5
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "FlameGlow2"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 25, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.5000076 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.7000076 }
                }
                Pass: i16 = 150
                AlphaRef: u8 = 0
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 90, 0 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin62_Alpha_Backdrop.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_splash_ring_Mask_2_01.tex"
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = -90
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.3
                }
                ParticleLinger: option[f32] = {
                    0.2
                }
                Lifetime: option[f32] = {
                    2
                }
                EmitterName: string = "TrailAdd8"
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 2000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 400, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.919997 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.8
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.919997 }
                            { 1, 1, 1, 0.919997 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.35
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.85882354, 0.5254902, 1, 0.4 }
                            { 0.28235295, 0.02745098, 0.40784314, 0 }
                        }
                    }
                }
                Pass: i16 = 50
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 50
                }
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 80, 50, 50 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec3] = {
                            { 0.6, 1, 1 }
                            { 0.3, 1, 1 }
                            { 0.15, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Seraphine_Skin14_E_Trail_01.tex"
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 0.5, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 0.5, 0 }
                        }
                    }
                }
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_Radialring_01_04113.tex"
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Lifetime: option[f32] = {
                    1.85
                }
                IsSingleParticle: flag = true
                EmitterName: string = "feather1"
                Importance: u8 = 3
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0.01, 0 }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -30, 0 }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.4 }
                }
                Pass: i16 = -50
                AlphaRef: u8 = 0
                IsDirectionOriented: flag = true
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                IsRotationEnabled: flag = true
                DirectionVelocityScale: f32 = 0.001
                DirectionVelocityMinScale: f32 = 1.5
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 25, 1.26 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Soraka_ball32_02.tex"
                TextureMult: pointer = VfxTextureMultDefinitionData {
                    TextureMult: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/R_mis_Mask_Color_6_8.tex"
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = 180
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 28
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            28
                        }
                    }
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.5
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.35
                                    1.5
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.5
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    0.7
                }
                Lifetime: option[f32] = {
                    1
                }
                EmitterName: string = "STARS_BACKGROUND"
                Importance: u8 = 3
                BirthOrbitalVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 1, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 1, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 50, -10, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -0.2
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 50, -10, 0 }
                        }
                    }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeSphere {
                    Flags: u8 = 1
                    Radius: f32 = 10
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -50, -10 }
                }
                ParticleColorTexture: string = "ASSETS/Shared/Particles/15.tex"
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                ColorLookUpTypeY: u8 = 3
                DepthBiasFactors: vec2 = { -1, -18 }
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 40, 65, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.9
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.3
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 40, 65, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin51_W_BightSpark.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 16
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.2
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    0.7
                                    1.2
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            1.2
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    1
                }
                Lifetime: option[f32] = {
                    1
                }
                EmitterName: string = "SparklesFast1"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 200, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.3
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 200, 0, 0 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 5, 5, 5 }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -600, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -600, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeSphere {
                    Flags: u8 = 1
                    Radius: f32 = 10
                }
                EmitterPosition: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -10, -5 }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.9000076 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.6
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.9000076 }
                            { 0.192157, 1, 0.827451, 0.9000076 }
                            { 1, 0, 0.682353, 0.9000076 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        Values: list[vec4] = {
                            { 0.23921569, 0.8352941, 1, 1 }
                            { 0.24313726, 0.7607843, 1, 1 }
                            { 0.13725491, 0.30588236, 0.85490197, 1 }
                        }
                    }
                }
                Pass: i16 = -10
                ColorLookUpTypeY: u8 = 3
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 30
                }
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 10, 35, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 10, 35, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.1
                            0.2
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.2, 2, 0 }
                            { 0.8, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Zeri_Skin10_Q_Bubble01.tex"
                NumFrames: u16 = 4
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.03
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "bullets8"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {}
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Mis_Hand_grenade.scb"
                    }
                    AlignPitchToCamera: bool = true
                    AlignYawToCamera: bool = true
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.2 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.7000076 }
                }
                Pass: i16 = 81
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 180, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 3.2, 2, 2.2 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Q_Mis_Thorn_2.tex"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 2
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Projected"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -50, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                ParticleColorTexture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/color-holdhalf.tex"
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.68000305, 0.22000457, 0.5000076 }
                }
                MeshRenderFlags: u8 = 0
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -90, 0, 0 }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 305, 450, 450 }
                }
                Texture: string = "ASSETS/Characters/Jinx/Skins/Skin65/Particles/Jinx_Skin65_Q_Glow.tex"
            }
        }
        ParticleName: string = "Jinx_Skin66_Q_RocketMis"
        ParticlePath: string = "Characters/Jinx/Skins/Skin66/Particles/Jinx_Skin66_Q_RocketMis"
        ObjectPath: hash = 0xeb39a192
    }
    0x624fed9e = ResourceResolver {
        ResourceMap: map[hash,link] = {
            "Jinx_emote_dance_loop_sound" = 0x03ed066b
            "Jinx_emote_dance_sound" = 0x93ffdb2d
            0xdd783950 = 0x01bc0a2c
            "Jinx_emote_joke_sound" = 0x0247fcf5
            0x3b20197a = 0x835fb806
            "Jinx_emote_taunt2_sound" = 0x4069ffeb
            "Jinx_emote_taunt_sound" = 0x8d7fc122
            "Jinx_E_Fire" = 0x16c49de3
            "Jinx_E_Fire_Tar" = 0xf9c1af4a
            "Jinx_E_Mine_Debuff" = 0x1d704d4a
            "Jinx_E_Mine_Explosion" = 0xc4b19dc3
            "Jinx_E_Mine_Idle_Green" = 0x3d783153
            "Jinx_E_Mine_Idle_Red" = 0xd73b2e57
            "Jinx_E_Mine_Ready" = 0xb50a457b
            "Jinx_E_Mine_Ready_Green" = 0xec17545a
            "Jinx_E_Mine_Ready_Red" = 0x82b414ea
            "Jinx_E_Mine_Set" = 0x1db613c4
            0x2aa5050b = 0xfc69f7b0
            0xaf4a6103 = 0xa66c1dff
            "Jinx_E_Mis" = 0x12687e66
            0x1bf664d2 = 0x65a2e7be
            "Jinx_Passive_Buff" = 0x032e2695
            "Jinx_Passive_Buff_OnKill" = 0x0b5ec060
            "Jinx_Q_Minigun_Cas_Long" = 0xcf14bf15
            "Jinx_Q_Minigun_Cas_Long2" = 0x9ce3b977
            "Jinx_Q_Minigun_Cas_Medium" = 0x3681d014
            "Jinx_Q_Minigun_Cas_PointBlank" = 0xa44c679f
            "Jinx_Q_Minigun_Cas_Short" = 0x9be5a22b
            "Jinx_Q_Minigun_Crit_Cas" = 0xb8057a97
            "Jinx_Q_Minigun_Crit_Cas_Medium" = 0x31160558
            "Jinx_Q_Minigun_Crit_Cas_PointBlank" = 0x19102673
            "Jinx_Q_Minigun_Crit_Cas_Short" = 0x4fdc0d5f
            "Jinx_Q_Minigun_Mis" = 0xeb3cca21
            "Jinx_Q_Minigun_Tar" = 0xde7b7085
            "Jinx_Q_Rocket_Cas" = 0xa9c79040
            "Jinx_Q_Rocket_Crit_Mis" = 0xc968f3f2
            "Jinx_Q_Rocket_Hurricane_Mis" = 0x2ffe8895
            "Jinx_Q_Rocket_mis" = 0xeb39a192
            "Jinx_Q_Rocket_tar" = 0x88de24ca
            "Jinx_Q_Rocket_Tar_Unit" = 0xa76ec48c
            0x0a9f806c = 0xcc6c6637
            0xb20facf0 = 0xc96155b4
            0x1dc9cba7 = 0x7c6e6418
            0xa1e95d04 = 0xf87300ec
            "Jinx_Recall_Leadin_Sound" = 0x4935985d
            "Jinx_R_Booster" = 0xda78fa74
            "Jinx_R_Cas" = 0x8c0b598d
            "Jinx_R_Rocket_Child" = 0x6720951a
            "Jinx_R_Mis" = 0x55c9e65b
            "Jinx_R_Tar" = 0x488d9523
            0x4b73542c = 0x9d93dd5a
            0x785a85cd = 0xfe9e4e37
            0x618b1f9c = 0x1081f482
            0xb4a61f18 = 0x8aa786b4
            0x228c331d = 0x39c2d3c1
            0x703192a1 = 0xd6ebdbc5
            "Jinx_W_Beam" = 0x4ce657de
            "Jinx_W_Cas" = 0xc5c9ffda
            "Jinx_W_Mis" = 0x37aec124
            "Jinx_W_Tar" = 0xc1e3bdc0
            0xea4f59c0 = 0x4935985d
            0x617f2a95 = 0x48ae2523
            0x20da2a44 = 0xba392b92
            0xd71a3e41 = 0xf29ef386
            0xa8c7afb4 = 0x39c2d3c1
            0xc200f858 = 0xd6ebdbc5
            "Jinx_Q_Minigun_Tar_Child" = 0x2da001f6
            "Jinx_Q_Hurricane_Rocket_Tar_Unit" = 0xc010c817
            "Jinx_Q_Hurricane_Rocket_tar" = 0x72ec4c15
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
            0x1720d661 = 0xd9710339
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
            0x08a38d85 = 0x3765d2be
            0xe562facd = 0x1a046b26
            0x0fd6fa46 = 0xe8ec412c
            0xeeafbf04 = 0xd32bf67a
            0xa96c9a02 = 0x45983dbb
            0x62333d7e = 0x989b246f
            0x30efbad8 = 0xa408b903
            0x33efbf91 = 0xa508ba96
            0xf0ebf724 = 0x910404c8
        }
    }
    0x6c7042af = StaticMaterialDef {
        Name: string = "Characters/Jinx/Skins/Skin66/Materials/Matcap_Iridescent_Holographic_inst"
        SamplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Dissolve_Gradient_Texture"
                TexturePath: file = 0xb1070dff5a760d5c
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Dissolve_Texture"
                TexturePath: file = 0x529442b91a3a6c5e
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Diffuse_Texture"
                TexturePath: file = 0x4df2f8578eb4df48
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Mask_Texture"
                TexturePath: file = 0x16845f9071df4542
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "MatCap_Tex"
                TexturePath: file = 0x64f834ab13c5304b
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "iridescentTex"
                TexturePath: file = 0x729c729254135455
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Noise_Texture"
                TexturePath: file = 0x8b1cf0ca3b7e8f42
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Flowmap"
                TexturePath: file = 0xb2f42548b598ff28
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
        }
        ParamValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                Name: string = "Rim_Light_Power"
                Value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Rim_Light_Intensity"
                Value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Rim_Light_Color"
                Value: vec4 = { 0.10966659, 0.9057603, 0.9001907, 1 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "rimOffset"
                Value: vec4 = { 0.985, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "albedoNewMin"
                Value: vec4 = { 0.1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "albedoNewMax"
                Value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "modelHeight"
                Value: vec4 = { 275, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Alpha_Sharpness"
                Value: vec4 = { 0.001, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Dissolve_SmoothStep"
                Value: vec4 = { 0, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Gradient_Sharpness"
                Value: vec4 = { 4, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Dissolve_Bias"
            }
            StaticMaterialShaderParamDef {
                Name: string = "TintColor"
                Value: vec4 = { 1, 1, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "MatCap_Strength"
                Value: vec4 = { 0.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "MatCapSpecularPower"
                Value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "MatCapSpecularTintColor"
                Value: vec4 = { 1, 1, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Iridescent_Strength"
                Value: vec4 = { 0.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Iridescent_Value"
                Value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Iridescent_Power"
                Value: vec4 = { 10, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Iridescent_Normal_Blend"
                Value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Holo_Strength"
                Value: vec4 = { 0.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Holo_Gradient_Contrast"
                Value: vec4 = { 5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "BaseNoiseUVTile"
                Value: vec4 = { 0.1, 0.1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "BaseNoiseScrollSpeed"
                Value: vec4 = { 0.04, 0.006, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "NoiseStrength"
                Value: vec4 = { 5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Flowspeed"
            }
            StaticMaterialShaderParamDef {
                Name: string = "Bloom_Intensity"
                Value: vec4 = { 0.3, 0, 0, 0 }
            }
        }
        Switches: list2[embed] = {
            StaticMaterialSwitchDef {
                Name: string = "ADD_FRESNEL_RIM"
            }
            StaticMaterialSwitchDef {
                Name: string = "USE_ALBEDO_REMAP"
            }
            StaticMaterialSwitchDef {
                Name: string = "USE_RIM"
            }
            StaticMaterialSwitchDef {
                Name: string = "USE_DISSOLVE"
                On: bool = false
                Group: string = "Dissolve"
            }
            StaticMaterialSwitchDef {
                Name: string = "FRESNEL_MASK_HOLOGRAPHIC"
                Group: string = "Holographic"
            }
            StaticMaterialSwitchDef {
                Name: string = "MATCAP_ON"
                Group: string = "Mat Cap"
            }
            StaticMaterialSwitchDef {
                Name: string = "MATCAP_MASK_ON"
                Group: string = "Mat Cap"
            }
            StaticMaterialSwitchDef {
                Name: string = "IRIDESCENCE_ON"
                Group: string = "Iridescent"
            }
            StaticMaterialSwitchDef {
                Name: string = "IRIDESCENT_MASK_ON"
                Group: string = "Iridescent"
            }
            StaticMaterialSwitchDef {
                Name: string = "HOLOGRAPHIC_ON"
                Group: string = "Holographic"
            }
            StaticMaterialSwitchDef {
                Name: string = "HOLOGRAPHIC_MASK_ON"
                Group: string = "Holographic"
            }
            StaticMaterialSwitchDef {
                Name: string = "FLOWMAP_ON"
                On: bool = false
                Group: string = "Holographic"
            }
        }
        ShaderMacros: map[string,string] = {
            "NUM_BLEND_WEIGHTS" = "4"
        }
        Techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                Name: string = "normal"
                Passes: list[embed] = {
                    StaticMaterialPassDef {
                        Shader: link = 0xbceb4368
                        BlendEnable: bool = true
                        SrcColorBlendFactor: u32 = 6
                        SrcAlphaBlendFactor: u32 = 6
                        DstColorBlendFactor: u32 = 7
                        DstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
        ChildTechniques: list[embed] = {
            StaticMaterialChildTechniqueDef {
                Name: string = "transition"
                ParentName: string = "normal"
                ShaderMacros: map[string,string] = {
                    "TRANSITION" = "1"
                }
            }
        }
    }
    0x82dd64d2 = StaticMaterialDef {
        Name: string = "Characters/Jinx/Skins/Skin66/Materials/Skirt_inst"
        SamplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Diffuse_Texture"
                TexturePath: file = 0x4c88a8d3a55badb6
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Bottom_Texture"
                TexturePath: file = 0x5a6966203b2dcead
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Top_Texture"
                TexturePath: file = 0x81f3bead9d1186ea
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Alpha_Mask"
                TexturePath: file = 0x830863549ce1c9ef
                AddressW: u32 = 1
            }
        }
        ParamValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                Name: string = "modelHeight"
                Value: vec4 = { 275, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "rimOffset"
            }
            StaticMaterialShaderParamDef {
                Name: string = "albedoNewMax"
                Value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "albedoNewMin"
                Value: vec4 = { 0.1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "VertAnim_UV_Dir2"
                Value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Low_Quality_Bias"
                Value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Alpha_Bounds"
                Value: vec4 = { 0, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Alpha_Bias"
            }
            StaticMaterialShaderParamDef {
                Name: string = "Bottom_ScrollSpeed"
                Value: vec4 = { 0, -0.05, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Top_ScrollSpeed"
                Value: vec4 = { 0, -0.153, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Alpha_Scale"
                Value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Diffuse_AlphaIntensity"
                Value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Top_AlphaIntensity"
                Value: vec4 = { 0.6725, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Bottom_AlphaIntensity"
                Value: vec4 = { 0.5425, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Alpha_Rate"
                Value: vec4 = { 0.1, 0.2, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Top_UVScale"
                Value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Bottom_UVScale"
                Value: vec4 = { 1.3, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Diffuse_Tint"
                Value: vec4 = { 1, 1, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Bloom_Intensity"
                Value: vec4 = { 0.075, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "VertAnim_Intensity"
                Value: vec4 = { 0.4, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "VertAnim_Line_Thick"
                Value: vec4 = { 0.8, 16, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "VertAnim_UV_Speed"
                Value: vec4 = { 0.64, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "VertAnim_UV_Tiling"
                Value: vec4 = { 8, 8, 0, 0 }
            }
        }
        Switches: list2[embed] = {
            StaticMaterialSwitchDef {
                Name: string = "USE_RIM"
            }
            StaticMaterialSwitchDef {
                Name: string = "USE_ALBEDO_REMAP"
            }
            StaticMaterialSwitchDef {
                Name: string = "DIFFUSEHOLD_USING_BCHANNEL"
            }
            StaticMaterialSwitchDef {
                Name: string = "BLOOM"
            }
            StaticMaterialSwitchDef {
                Name: string = "VERTEX_WOBBLE_PANNING_LINE"
            }
            StaticMaterialSwitchDef {
                Name: string = "VERTEX_COLOR_MASK"
                On: bool = false
            }
        }
        ShaderMacros: map[string,string] = {
            "NUM_BLEND_WEIGHTS" = "4"
        }
        Techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                Name: string = "normal"
                Passes: list[embed] = {
                    StaticMaterialPassDef {
                        Shader: link = "Shaders/SkinnedMesh/ScrollingUVs_MultiLayer_Alpha_Bloom_Wobble"
                        BlendEnable: bool = true
                        SrcColorBlendFactor: u32 = 6
                        SrcAlphaBlendFactor: u32 = 6
                        DstColorBlendFactor: u32 = 7
                        DstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
        ChildTechniques: list[embed] = {
            StaticMaterialChildTechniqueDef {
                Name: string = "transition"
                ParentName: string = "normal"
                ShaderMacros: map[string,string] = {
                    "TRANSITION" = "1"
                }
            }
        }
        DynamicMaterial: pointer = DynamicMaterialDef {}
    }
    0xcd989594 = StaticMaterialDef {
        Name: string = "Characters/Jinx/Skins/Skin66/Materials/Matcap_Iridescent_Holographic_Body_inst"
        SamplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Dissolve_Gradient_Texture"
                TexturePath: file = 0xb1070dff5a760d5c
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Dissolve_Texture"
                TexturePath: file = 0x529442b91a3a6c5e
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Diffuse_Texture"
                TexturePath: file = 0xa4c9f5ddcdc88715
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Mask_Texture"
                TexturePath: file = 0x219c7582503c10c6
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "MatCap_Tex"
                TexturePath: file = 0x64f834ab13c5304b
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "iridescentTex"
                TexturePath: file = 0xabca77fa311c4e7a
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Noise_Texture"
                TexturePath: file = 0x8b1cf0ca3b7e8f42
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Flowmap"
                TexturePath: file = 0xb2f42548b598ff28
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
        }
        ParamValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                Name: string = "Rim_Light_Power"
                Value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Rim_Light_Intensity"
                Value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Rim_Light_Color"
                Value: vec4 = { 0.10966659, 0.9057603, 0.9001907, 1 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "rimOffset"
                Value: vec4 = { 0.985, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "albedoNewMin"
                Value: vec4 = { 0.1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "albedoNewMax"
                Value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "modelHeight"
                Value: vec4 = { 275, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Alpha_Sharpness"
                Value: vec4 = { 0.001, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Dissolve_SmoothStep"
                Value: vec4 = { 0, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Gradient_Sharpness"
                Value: vec4 = { 4, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Dissolve_Bias"
            }
            StaticMaterialShaderParamDef {
                Name: string = "TintColor"
                Value: vec4 = { 1, 1, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "MatCap_Strength"
                Value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "MatCapSpecularPower"
                Value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "MatCapSpecularTintColor"
                Value: vec4 = { 1, 1, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Iridescent_Strength"
                Value: vec4 = { 0.6, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Iridescent_Value"
                Value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Iridescent_Power"
                Value: vec4 = { 10, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Iridescent_Normal_Blend"
                Value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Holo_Strength"
                Value: vec4 = { 0.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Holo_Gradient_Contrast"
                Value: vec4 = { 5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "BaseNoiseUVTile"
                Value: vec4 = { 0.1, 0.1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "BaseNoiseScrollSpeed"
                Value: vec4 = { 0.04, 0.006, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "NoiseStrength"
                Value: vec4 = { 5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Flowspeed"
            }
            StaticMaterialShaderParamDef {
                Name: string = "Bloom_Intensity"
                Value: vec4 = { 0.3, 0, 0, 0 }
            }
        }
        Switches: list2[embed] = {
            StaticMaterialSwitchDef {
                Name: string = "ADD_FRESNEL_RIM"
            }
            StaticMaterialSwitchDef {
                Name: string = "USE_ALBEDO_REMAP"
            }
            StaticMaterialSwitchDef {
                Name: string = "USE_RIM"
            }
            StaticMaterialSwitchDef {
                Name: string = "USE_DISSOLVE"
                On: bool = false
                Group: string = "Dissolve"
            }
            StaticMaterialSwitchDef {
                Name: string = "FRESNEL_MASK_HOLOGRAPHIC"
                Group: string = "Holographic"
            }
            StaticMaterialSwitchDef {
                Name: string = "MATCAP_ON"
                Group: string = "Mat Cap"
            }
            StaticMaterialSwitchDef {
                Name: string = "MATCAP_MASK_ON"
                Group: string = "Mat Cap"
            }
            StaticMaterialSwitchDef {
                Name: string = "IRIDESCENCE_ON"
                Group: string = "Iridescent"
            }
            StaticMaterialSwitchDef {
                Name: string = "IRIDESCENT_MASK_ON"
                Group: string = "Iridescent"
            }
            StaticMaterialSwitchDef {
                Name: string = "HOLOGRAPHIC_ON"
                Group: string = "Holographic"
            }
            StaticMaterialSwitchDef {
                Name: string = "HOLOGRAPHIC_MASK_ON"
                Group: string = "Holographic"
            }
            StaticMaterialSwitchDef {
                Name: string = "FLOWMAP_ON"
                On: bool = false
                Group: string = "Holographic"
            }
        }
        ShaderMacros: map[string,string] = {
            "NUM_BLEND_WEIGHTS" = "4"
        }
        Techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                Name: string = "normal"
                Passes: list[embed] = {
                    StaticMaterialPassDef {
                        Shader: link = 0xbceb4368
                        BlendEnable: bool = true
                        SrcColorBlendFactor: u32 = 6
                        SrcAlphaBlendFactor: u32 = 6
                        DstColorBlendFactor: u32 = 7
                        DstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
        ChildTechniques: list[embed] = {
            StaticMaterialChildTechniqueDef {
                Name: string = "transition"
                ParentName: string = "normal"
                ShaderMacros: map[string,string] = {
                    "TRANSITION" = "1"
                }
            }
        }
    }
    0xdd817686 = StaticMaterialDef {
        Name: string = "Characters/Jinx/Skins/Skin66/Materials/WeaponVFX"
        SamplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Diffuse_Texture"
                TexturePath: file = 0x4df2f8578eb4df48
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Bottom_Texture"
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Top_Texture"
                TexturePath: file = 0x64fe2c2898bf5059
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                TextureName: string = "Alpha_Mask"
                TexturePath: file = 0x441946a7c63657f8
                AddressW: u32 = 1
            }
        }
        ParamValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                Name: string = "modelHeight"
                Value: vec4 = { 275, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "rimOffset"
                Value: vec4 = { 0.3, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "albedoNewMax"
                Value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "albedoNewMin"
                Value: vec4 = { 0.1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "VertAnim_UV_Dir2"
                Value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Low_Quality_Bias"
                Value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Alpha_Bounds"
                Value: vec4 = { 0, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Alpha_Bias"
            }
            StaticMaterialShaderParamDef {
                Name: string = "Bottom_ScrollSpeed"
                Value: vec4 = { 0, -0.1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Top_ScrollSpeed"
                Value: vec4 = { -0.3, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Alpha_Scale"
                Value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Diffuse_AlphaIntensity"
                Value: vec4 = { 0.805, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Top_AlphaIntensity"
                Value: vec4 = { 0.9875, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Bottom_AlphaIntensity"
            }
            StaticMaterialShaderParamDef {
                Name: string = "Alpha_Rate"
                Value: vec4 = { 0.1, 0.2, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Top_UVScale"
                Value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Bottom_UVScale"
                Value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Diffuse_Tint"
                Value: vec4 = { 0.7340963, 0.9729, 0.9963226, 1 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "Bloom_Intensity"
                Value: vec4 = { 0.3, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "VertAnim_Intensity"
                Value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "VertAnim_Line_Thick"
                Value: vec4 = { 0.618, 16, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "VertAnim_UV_Speed"
                Value: vec4 = { 0.64, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "VertAnim_UV_Tiling"
                Value: vec4 = { 16, 16, 0, 0 }
            }
        }
        Switches: list2[embed] = {
            StaticMaterialSwitchDef {
                Name: string = "USE_RIM"
            }
            StaticMaterialSwitchDef {
                Name: string = "USE_ALBEDO_REMAP"
            }
            StaticMaterialSwitchDef {
                Name: string = "DIFFUSEHOLD_USING_BCHANNEL"
            }
            StaticMaterialSwitchDef {
                Name: string = "BLOOM"
            }
            StaticMaterialSwitchDef {
                Name: string = "VERTEX_WOBBLE_PANNING_LINE"
                On: bool = false
            }
            StaticMaterialSwitchDef {
                Name: string = "VERTEX_COLOR_MASK"
                On: bool = false
            }
        }
        ShaderMacros: map[string,string] = {
            "NUM_BLEND_WEIGHTS" = "4"
        }
        Techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                Name: string = "normal"
                Passes: list[embed] = {
                    StaticMaterialPassDef {
                        Shader: link = "Shaders/SkinnedMesh/ScrollingUVs_MultiLayer_Alpha_Bloom_Wobble"
                        BlendEnable: bool = true
                        SrcColorBlendFactor: u32 = 6
                        SrcAlphaBlendFactor: u32 = 6
                        DstColorBlendFactor: u32 = 7
                        DstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
        ChildTechniques: list[embed] = {
            StaticMaterialChildTechniqueDef {
                Name: string = "transition"
                ParentName: string = "normal"
                ShaderMacros: map[string,string] = {
                    "TRANSITION" = "1"
                }
            }
        }
        DynamicMaterial: pointer = DynamicMaterialDef {}
    }
}
