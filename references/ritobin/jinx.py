#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    0xdcfb6d07 = StatStoneSet {
        Name: string = "stat_stone_set_name_1"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "6d5b12d3-97ea-48d2-836d-4d4f3d91dfc1"
            ItemId: u32 = 66600047
        }
        StatStones: list[link] = {
            0x7d6f5704
            0x12b9523e
            0xb8838b71
            0x05b0e987
        }
    }
    0x05b0e987 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_JinxQPAttacks"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "e55d35a8-dd0f-4d9f-9385-bd456393850f"
            ItemId: u32 = 126473
        }
        mDescriptionTraKey: string = "stat_stone_description_JinxQPAttacks"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 253
            }
        }
        Category: link = 0x06fc9407
        Milestones: list[u64] = {
            45
            125
            225
            275
            350
            150
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        StoneName: string = "JinxQPAttacks"
        DataCollectionOnly: bool = true
    }
    0x12b9523e = StatStoneData {
        mNameTraKey: string = "stat_stone_name_JinxQPDuration"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "9b54a58e-c5e4-4ce7-a181-98d7d2bcf222"
            ItemId: u32 = 50
        }
        mDescriptionTraKey: string = "stat_stone_description_JinxQPDuration"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 253
            }
        }
        Category: link = 0x47089000
        Milestones: list[u64] = {
            875
            2000
            4500
            5000
            6500
            2500
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        TrackingType: u8 = 1
        StoneName: string = "JinxQPDuration"
    }
    0x7d6f5704 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_JinxFullDamageDeathRockets"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "dba8bd83-0cf0-4058-a9d4-cde27d2380ca"
            ItemId: u32 = 56
        }
        mDescriptionTraKey: string = "stat_stone_description_JinxFullDamageDeathRockets"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 253
            }
        }
        Category: link = 0x1dab670a
        Milestones: list[u64] = {
            7
            15
            35
            40
            50
            20
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        StoneName: string = "JinxFullDamageDeathRockets"
    }
    0xb8838b71 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_JinxPDoubleTriggers"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "1d97ccc6-80e5-4e99-88ae-74377e4a73e7"
            ItemId: u32 = 51
        }
        mDescriptionTraKey: string = "stat_stone_description_JinxPDoubleTriggers"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 253
            }
        }
        Category: link = 0x47089000
        Milestones: list[u64] = {
            8
            20
            40
            45
            60
            25
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        StoneName: string = "JinxPDoubleTriggers"
    }
    0x9da21277 = StatStoneSet {
        Name: string = "stat_stone_set_name_starter"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "17eae5f9-edde-4ac6-aa87-f2305207fba3"
            ItemId: u32 = 66600271
        }
        StatStones: list[link] = {
            0xfd8a2608
            0xcce3227d
            0x2f2b3dd0
        }
    }
    0x2f2b3dd0 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_structures_destroyed"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "c7308f7f-0e73-4363-9bf9-7b75aa1b0d54"
            ItemId: u32 = 125752
        }
        mDescriptionTraKey: string = "stat_stone_description_StructuresDestroyed"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 63
            }
        }
        Category: link = 0x6ce57a50
        Milestones: list[u64] = {
            5
            15
            25
            30
            40
            15
        }
        StoneName: string = "JinxStructuresDestroyed"
    }
    0xcce3227d = StatStoneData {
        mNameTraKey: string = "stat_stone_name_takedowns"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "1a6f5c03-df62-48b6-a824-a4f84039538d"
            ItemId: u32 = 125751
        }
        mDescriptionTraKey: string = "stat_stone_description_Takedowns"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 7
            }
            StatStoneEventToTrack {
                EventToTrack: u32 = 86
                StatFilters: list[pointer] = {
                    TargetTypeFilter {
                        MinionsAreValid: bool = false
                    }
                }
            }
            StatStoneEventToTrack {
                EventToTrack: u32 = 230
            }
        }
        Category: link = 0x5c6e96a2
        Milestones: list[u64] = {
            25
            65
            125
            150
            185
            75
        }
        StoneName: string = "JinxTakedowns"
    }
    0xfd8a2608 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_EpicMonstersKilled"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "951dbef2-b95b-421f-ad18-c632b4908c6e"
            ItemId: u32 = 125750
        }
        mDescriptionTraKey: string = "stat_stone_description_EpicMonstersKilled"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 66
                StatFilters: list[pointer] = {
                    TargetHasUnitTagFilter {
                        UnitTags: embed = ObjectTags {
                            mObjectTagList: list2[hash] = {
                                0x592aa99b
                            }
                        }
                    }
                }
            }
            StatStoneEventToTrack {
                EventToTrack: u32 = 86
                StatFilters: list[pointer] = {
                    TargetTypeFilter {
                        ChampionsAreValid: bool = false
                    }
                    TargetHasUnitTagFilter {
                        UnitTags: embed = ObjectTags {
                            mObjectTagList: list2[hash] = {
                                0x592aa99b
                            }
                        }
                    }
                }
            }
            StatStoneEventToTrack {
                EventToTrack: u32 = 64
                StatFilters: list[pointer] = {
                    TargetHasUnitTagFilter {
                        UnitTags: embed = ObjectTags {
                            mObjectTagList: list2[hash] = {
                                0x592aa99b
                            }
                        }
                    }
                }
            }
        }
        Category: link = 0x6ce57a50
        Milestones: list[u64] = {
            3
            10
            20
            22
            25
            10
        }
        StoneName: string = "JinxEpicMonstersKilled"
    }
    0xddfb6e9a = StatStoneSet {
        Name: string = "stat_stone_set_name_2"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "ffaca668-24ca-4d2c-bd27-b0bdd48326a6"
            ItemId: u32 = 66600418
        }
        StatStones: list[link] = {
            0x8dc35d89
            0x8251f5f2
            0x2f72366c
        }
    }
    0x2f72366c = StatStoneData {
        mNameTraKey: string = "stat_stone_name_JinxWLongRange"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "e8cc4028-914c-41f4-b20c-86d45efcfed3"
            ItemId: u32 = 126040
        }
        mDescriptionTraKey: string = "stat_stone_description_JinxWLongRange"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 253
            }
        }
        Category: link = 0x1dab670a
        Milestones: list[u64] = {
            15
            45
            85
            100
            125
            50
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        StoneName: string = "JinxWLongRange"
    }
    0x8251f5f2 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_JinxETakedowns"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "51e708a6-bf9c-4e4c-a9cf-eb8837ad3c27"
            ItemId: u32 = 126039
        }
        mDescriptionTraKey: string = "stat_stone_description_JinxETakedowns"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 253
            }
        }
        Category: link = 0x06fc9407
        Milestones: list[u64] = {
            2500
            5500
            11000
            14000
            17000
            7000
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        StoneName: string = "JinxEDamage"
    }
    0x8dc35d89 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_JinxQDamage"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "caf3f6fa-c4e9-4cf9-ab76-18ec139269c5"
            ItemId: u32 = 126038
        }
        mDescriptionTraKey: string = "stat_stone_description_JinxQDamage"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 253
            }
        }
        Category: link = 0x1dab670a
        Milestones: list[u64] = {
            100
            250
            500
            600
            750
            300
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        StoneName: string = "JinxQHits"
    }
    "Characters/Jinx/Spells/JinxWAbility" = AbilityObject {
        mRootSpell: link = "Characters/Jinx/Spells/JinxWAbility/JinxW"
        mChildSpells: list[link] = {
            "Characters/Jinx/Spells/JinxWAbility/JinxW"
            "Characters/Jinx/Spells/JinxWAbility/JinxWMissile"
            "Characters/Jinx/Spells/JinxWAbility/JinxWSight"
        }
        mName: string = "JinxWAbility"
        AbilityTraits: u32 = 256
    }
    "Characters/Jinx/Spells/JinxWAbility/JinxWMissile" = SpellObject {
        ObjectName: string = "JinxWMissile"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxWAbility/JinxWMissile"
        mScriptName: string = "JinxWMissile"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "EzrealMysticShotMissile"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        30
                        90
                        150
                        245
                        315
                        440
                        565
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        2.25
                        2.5
                        2.75
                        3
                        3.25
                        3.5
                        3.75
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 1.2
            mAnimationName: string = "Spell2"
            mImgIconName: list[string] = {
                "FallenAngel_DarkBinding.dds"
            }
            mCastTime: f32 = 0.6
            0x11704a2b: f32 = 0.25
            0xf26881a0: f32 = 1
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            Cooldown: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
                0x0a3e0478: f32 = 0
            }
            mCantCancelWhileWindingUp: bool = true
            UseAnimatorFramerate: bool = true
            CastRange: list[f32] = {
                1500
                1500
                1500
                1500
                1500
                1500
                1500
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    1500
                    1500
                    1500
                    1500
                    1500
                    1500
                    1500
                }
                0x0a3e0478: f32 = 1500
            }
            CastRangeDisplayOverride: list[f32] = {
                1175
                1175
                1175
                1175
                1175
                1175
                1175
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 60
                MovementComponent: pointer = FixedSpeedMovement {
                    mUseHeightOffsetAtEnd: bool = true
                    0x03046674: bool = true
                    mTracksTarget: bool = false
                    mTargetHeightAugment: f32 = 100
                    mStartBoneName: string = "Pistol"
                    mStartBoneSkinOverrides: map[u32,string] = {
                        60 = "Cstm_Buffbone_Rocket_Launcher"
                    }
                    mProjectTargetToCastRange: bool = true
                    mSpeed: f32 = 3300
                }
                HeightSolver: pointer = BlendedLinearHeightSolver {}
                VerticalFacing: pointer = VerticalFacingFaceTarget {}
                Behaviors: list[pointer] = {
                    CastOnHit {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 3
            CastFrame: f32 = 7.53
            MissileSpeed: f32 = 3300
            mMissileEffectKey: hash = "Jinx_W_Mis"
            mLineWidth: f32 = 60
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            SelectionPriority: u32 = 2
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mUseTooltipFromAnotherSpell: hash = "Characters/Jinx/Spells/JinxWAbility/JinxW"
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        HideWithLineIndicator: bool = true
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionLine {
                        EndLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        LineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        LineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                60
                                60
                                60
                                60
                                60
                                60
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxWAbility/JinxW" = SpellObject {
        ObjectName: string = "JinxW"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxWAbility/JinxW"
        mScriptName: string = "JinxW"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 4
            mAffectsTypeFlags: u32 = 13327
            mRequiredUnitTags: embed = ObjectTags {
                mObjectTagList: list2[hash] = {
                    "Champion"
                }
            }
            mSpellTags: list[string] = {
                "Trait_DamageAbility"
                "Trait_SignatureSpell"
                "Trait_Ranged_StopsFirstHit"
            }
            DataValues: list2[embed] = {
                SpellDataValue {
                    Name: string = "JinxLowEndWCastTime"
                    Values: list[f32] = {
                        0.4
                        0.4
                        0.4
                        0.4
                        0.4
                        0.4
                        0.4
                    }
                }
                SpellDataValue {
                    Name: string = "JinxWASpeedCastTimeScalarPerHundrethSecond"
                    Values: list[f32] = {
                        0.08
                        0.08
                        0.08
                        0.08
                        0.08
                        0.08
                        0.08
                    }
                }
                SpellDataValue {
                    Name: string = "Damage"
                    Values: list[f32] = {
                        -40
                        10
                        60
                        110
                        160
                        210
                        260
                    }
                }
                SpellDataValue {
                    Name: string = "SlowPercent"
                    Values: list[f32] = {
                        30
                        40
                        50
                        60
                        70
                        80
                        90
                    }
                }
                SpellDataValue {
                    Name: string = "SlowDuration"
                    Values: list[f32] = {
                        2
                        2
                        2
                        2
                        2
                        2
                        2
                    }
                }
                SpellDataValue {
                    Name: string = "ADRatio"
                    Values: list[f32] = {
                        1.4
                        1.4
                        1.4
                        1.4
                        1.4
                        1.4
                        1.4
                    }
                }
            }
            DataValuesModeOverride: map[hash,embed] = {
                0x497ae878 = SpellDataValueVector {
                    SpellDataValues: list[embed] = {
                        SpellDataValue {
                            Name: string = "ADRatio"
                            Values: list[f32] = {
                                2
                                2
                                2
                                2
                                2
                                2
                                2
                            }
                        }
                        SpellDataValue {
                            Name: string = "Damage"
                            Values: list[f32] = {
                                -50
                                10
                                70
                                130
                                190
                                250
                                310
                            }
                        }
                    }
                }
            }
            mSpellCalculations: map[hash,pointer] = {
                "TotalDamage" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        NamedDataValueCalculationPart {
                            mDataValue: hash = "Damage"
                        }
                        StatByNamedDataValueCalculationPart {
                            mStat: u8 = 2
                            mDataValue: hash = "ADRatio"
                        }
                    }
                }
            }
            mAnimationName: string = ""
            mImgIconName: list[string] = {
                "ASSETS/Characters/Jinx/HUD/Icons2D/Jinx_W.dds"
            }
            mCastTime: f32 = 0.25
            0x11704a2b: f32 = 0.25
            0xf26881a0: f32 = 0
            CooldownTime: list[f32] = {
                9
                8
                7
                6
                5
                4
                3
            }
            Cooldown: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    9
                    8
                    7
                    6
                    5
                    4
                    3
                }
                0x0a3e0478: f32 = 9
            }
            mCantCancelWhileWindingUp: bool = true
            CastRange: list[f32] = {
                10000
                10000
                10000
                10000
                10000
                10000
                10000
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    10000
                    10000
                    10000
                    10000
                    10000
                    10000
                    10000
                }
                0x0a3e0478: f32 = 10000
            }
            CastRangeDisplayOverride: list[f32] = {
                1450
                1450
                1450
                1450
                1450
                1450
                1450
            }
            CastRadius: list[f32] = {
                210
                210
                210
                210
                210
                210
                210
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 1.98
            MissileSpeed: f32 = 1200
            mLineWidth: f32 = 60
            mHitBoneName: string = "C_BUFFBONE_GLB_HEAD_LOC"
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            Mana: list[f32] = {
                40
                45
                50
                55
                60
                65
            }
            0x210f9ec0: embed = 0x630af303 {
                Values: list[f32] = {
                    40
                    45
                    50
                    55
                    60
                    65
                }
                0x0a3e0478: f32 = 40
            }
            SelectionPriority: u32 = 2
            mTargetingTypeData: pointer = Location {}
            mCastingBreaksStealth: bool = true
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "JinxW"
                    mFormat: link = 0xd7c27163
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_JinxW_Name"
                        "keySummary" = "Spell_JinxW_Summary"
                        "keyTooltip" = "Spell_JinxW_Tooltip"
                        "keyTooltipExtendedBelowLine" = "Spell_JinxW_TooltipExtendedBelowLine"
                    }
                    mLists: map[string,embed] = {
                        "LevelUp" = TooltipInstanceList {
                            LevelCount: u32 = 5
                            Elements: list[embed] = {
                                TooltipInstanceListElement {
                                    Type: string = "Damage"
                                    TypeIndex: i32 = 1
                                    NameOverride: string = "Spell_ListType_Damage"
                                }
                                TooltipInstanceListElement {
                                    Type: string = "SlowPercent"
                                    TypeIndex: i32 = 2
                                    NameOverride: string = "Spell_ListType_Slow"
                                    Style: u32 = 1
                                }
                                TooltipInstanceListElement {
                                    Type: string = "Cooldown"
                                }
                                TooltipInstanceListElement {
                                    Type: string = "Cost"
                                }
                            }
                        }
                    }
                }
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        HideWithLineIndicator: bool = true
                    }
                    TargeterDefinitionLine {
                        EndLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        LineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        LineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                60
                                60
                                60
                                60
                                60
                                60
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
        BotData: pointer = BotsSpellData {
            DamageTag: u32 = 0
            0x6d548702: pointer = GameCalculation {
                mFormulaParts: list[pointer] = {
                    0xf3cbe7b2 {
                        mSpellCalculationKey: hash = "TotalDamage"
                    }
                }
            }
            0xec17e271: list2[embed] = {
                0xb09016f6 {
                    EffectTag: u32 = 1
                    EffectCalculation: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            NamedDataValueCalculationPart {
                                mDataValue: hash = "SlowDuration"
                            }
                        }
                    }
                }
                0xb09016f6 {
                    EffectTag: u32 = 32768
                    EffectCalculation: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            NumberCalculationPart {
                                mNumber: f32 = 60
                            }
                        }
                    }
                }
            }
            0x38382c53: list2[embed] = {
                0x150d1b92 {
                    0xe38f54f7: u32 = 1
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 4
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 1024
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 8192
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 2048
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxWAbility/JinxWSight" = SpellObject {
        ObjectName: string = "JinxWSight"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxWAbility/JinxWSight"
        mScriptName: string = "JinxWSight"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_JinxWSight"
        }
    }
    "Characters/Jinx/Spells/JinxEAbility" = AbilityObject {
        mRootSpell: link = "Characters/Jinx/Spells/JinxEAbility/JinxE"
        mChildSpells: list[link] = {
            "Characters/Jinx/Spells/JinxEAbility/JinxE"
            "Characters/Jinx/Spells/JinxEAbility/JinxEFireBurn"
            "Characters/Jinx/Spells/JinxEAbility/JinxEMine"
            "Characters/Jinx/Spells/JinxEAbility/JinxEMineSnare"
            "Characters/Jinx/Spells/JinxEAbility/JinxEHit"
            "Characters/Jinx/Spells/JinxEAbility/JinxEMineSight"
        }
        mName: string = "JinxEAbility"
        AbilityTraits: u32 = 3072
    }
    "Characters/Jinx/Spells/JinxEAbility/JinxEMineSight" = SpellObject {
        ObjectName: string = "JinxEMineSight"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxEAbility/JinxEMineSight"
        mScriptName: string = "JinxEMineSight"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_JinxEMineSight"
        }
    }
    "Characters/Jinx/Spells/JinxEAbility/JinxEHit" = SpellObject {
        ObjectName: string = "JinxEHit"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxEAbility/JinxEHit"
        mScriptName: string = "JinxEHit"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 4194304
            mAffectsTypeFlags: u32 = 23567
            mAlternateName: string = "JinxE"
            mAnimationName: string = "Spell3"
            mImgIconName: list[string] = {
                "Cryophoenix_FrigidOrb.dds"
            }
            0x11704a2b: f32 = 0.25
            0xf26881a0: f32 = 1
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            Cooldown: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
                0x0a3e0478: f32 = 0
            }
            CannotBeSuppressed: bool = true
            CanCastWhileDisabled: bool = true
            CastRange: list[f32] = {
                1200
                1200
                1200
                1200
                1200
                1200
                1200
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    1200
                    1200
                    1200
                    1200
                    1200
                    1200
                    1200
                }
                0x0a3e0478: f32 = 1200
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 120
                MovementComponent: pointer = FixedTimeMovement {
                    mTargetHeightAugment: f32 = 60
                    mOffsetInitialTargetHeight: f32 = 60
                    mTravelTime: f32 = 0.4
                }
                HeightSolver: pointer = GravityHeightSolver {
                    mGravity: f32 = 5000
                }
                VerticalFacing: pointer = VeritcalFacingMatchVelocity {}
                Behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
                0xc195fba6: bool = true
            }
            mCastType: u32 = 1
            CastFrame: f32 = 7.975
            MissileSpeed: f32 = 1100
            mMissileEffectKey: hash = "Jinx_E_Mis"
            mLineWidth: f32 = 120
            bHaveHitBone: bool = true
            mHitBoneName: string = "pelvis"
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        HideWithLineIndicator: bool = true
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionLine {
                        EndLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        LineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        LineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                120
                                120
                                120
                                120
                                120
                                120
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxEAbility/JinxEMine" = SpellObject {
        ObjectName: string = "JinxEMine"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxEAbility/JinxEMine"
        mScriptName: string = "JinxEMine"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 1029
            mRequiredUnitTags: embed = ObjectTags {
                mObjectTagList: list2[hash] = {
                    "Champion"
                }
            }
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        2
                        2
                        2
                        2
                        2
                        2
                        2
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        30
                        80
                        130
                        180
                        230
                        280
                        330
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        4
                        4
                        4
                        4
                        4
                        4
                        4
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 0.6
            mAnimationName: string = "Spell2"
            mImgIconName: list[string] = {
                "ASSETS/Spells/Icons2D/Caitlyn_YordleSnapTrap.dds"
            }
            0x11704a2b: f32 = 0.25
            0xf26881a0: f32 = 1
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            Cooldown: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
                0x0a3e0478: f32 = 0
            }
            mCantCancelWhileWindingUp: bool = true
            mProjectTargetToCastRange: bool = true
            mSpellRevealsChampion: bool = false
            CastRange: list[f32] = {
                800
                800
                800
                800
                800
                800
                800
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    800
                    800
                    800
                    800
                    800
                    800
                    800
                }
                0x0a3e0478: f32 = 800
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 7.5
            MissileSpeed: f32 = 1450
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Area {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionAoe {
                        CenterLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_JinxEMine"
        }
    }
    "Characters/Jinx/Spells/JinxEAbility/JinxEFireBurn" = SpellObject {
        ObjectName: string = "JinxEFireBurn"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxEAbility/JinxEFireBurn"
        mScriptName: string = "JinxEFireBurn"
        mSpell: pointer = SpellDataResource {
            mImgIconName: list[string] = {
                "ASSETS/Characters/Jinx/HUD/Icons2D/Jinx_E_Debuff.dds"
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_JinxEFireBurn"
        }
    }
    "Characters/Jinx/Spells/JinxEAbility/JinxEMineSnare" = SpellObject {
        ObjectName: string = "JinxEMineSnare"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxEAbility/JinxEMineSnare"
        mScriptName: string = "JinxEMineSnare"
        mSpell: pointer = SpellDataResource {
            mImgIconName: list[string] = {
                "ASSETS/Characters/Jinx/HUD/Icons2D/Jinx_E.dds"
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_JinxEMineSnare"
        }
    }
    "Characters/Jinx/Spells/JinxEAbility/JinxE" = SpellObject {
        ObjectName: string = "JinxE"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxEAbility/JinxE"
        mScriptName: string = "JinxE"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 4
            mAffectsTypeFlags: u32 = 1029
            mRequiredUnitTags: embed = ObjectTags {
                mObjectTagList: list2[hash] = {
                    "Champion"
                }
            }
            mSpellTags: list[string] = {
                "Trait_ImmobilizingCCSpell"
                "Trait_DamageAbility"
                "Trait_Target_Area"
                "Trait_Low_Damage"
                "Trait_AoE"
            }
            DataValues: list2[embed] = {
                SpellDataValue {
                    Name: string = "Damage"
                    Values: list[f32] = {
                        40
                        90
                        140
                        190
                        240
                        290
                        340
                    }
                }
                SpellDataValue {
                    Name: string = "RootDuration"
                    Values: list[f32] = {
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                    }
                }
                SpellDataValue {
                    Name: string = "GrenadeDuration"
                    Values: list[f32] = {
                        5
                        5
                        5
                        5
                        5
                        5
                        5
                    }
                }
                SpellDataValue {
                    Name: string = "GrenadeArmTime"
                    Values: list[f32] = {
                        0.5
                        0.5
                        0.5
                        0.5
                        0.5
                        0.5
                        0.5
                    }
                }
            }
            mSpellCalculations: map[hash,pointer] = {
                "TotalDamage" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        NamedDataValueCalculationPart {
                            mDataValue: hash = "Damage"
                        }
                        StatByCoefficientCalculationPart {
                            mCoefficient: f32 = 1
                        }
                    }
                }
            }
            mAnimationName: string = "Spell3"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Jinx/HUD/Icons2D/Jinx_E.dds"
            }
            mCastTime: f32 = 0.25
            0x11704a2b: f32 = 0.375
            0xf26881a0: f32 = 1.5
            CooldownTime: list[f32] = {
                27.5
                24
                20.5
                17
                13.5
                10
                10
            }
            Cooldown: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    27.5
                    24
                    20.5
                    17
                    13.5
                    10
                    10
                }
            }
            mCantCancelWhileWindingUp: bool = true
            mProjectTargetToCastRange: bool = true
            mSpellRevealsChampion: bool = false
            UseAnimatorFramerate: bool = true
            CastRange: list[f32] = {
                925
                925
                925
                925
                925
                925
                925
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    925
                    925
                    925
                    925
                    925
                    925
                    925
                }
                0x0a3e0478: f32 = 925
            }
            CastRadius: list[f32] = {
                315
                315
                315
                315
                315
                315
                315
            }
            CastConeDistance: f32 = 100
            CastTargetAdditionalUnitsRadius: f32 = 325
            CastFrame: f32 = 15
            MissileSpeed: f32 = 1750
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            Mana: list[f32] = {
                90
                90
                90
                90
                90
                90
            }
            0x210f9ec0: embed = 0x630af303 {
                Values: list[f32] = {
                    90
                    90
                    90
                    90
                    90
                    90
                }
                0x0a3e0478: f32 = 90
            }
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = LocationClamped {}
            mCastingBreaksStealth: bool = true
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "JinxE"
                    mFormat: link = 0xd7c27163
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_JinxE_Name"
                        "keySummary" = "Spell_JinxE_Summary"
                        "keyTooltip" = "Spell_JinxE_Tooltip"
                        "keyTooltipExtendedBelowLine" = "Spell_JinxE_TooltipExtendedBelowLine"
                    }
                    mLists: map[string,embed] = {
                        "LevelUp" = TooltipInstanceList {
                            LevelCount: u32 = 5
                            Elements: list[embed] = {
                                TooltipInstanceListElement {
                                    Type: string = "Damage"
                                    TypeIndex: i32 = 1
                                    NameOverride: string = "Spell_ListType_Damage"
                                }
                                TooltipInstanceListElement {
                                    Type: string = "Cooldown"
                                }
                            }
                        }
                    }
                }
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {}
                    TargeterDefinitionAoe {
                        CenterLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        TextureOrientation: u32 = 3
                        TextureRadiusOverrideName: file = 0xb3d591dcdd1118f2
                    }
                }
            }
        }
        BotData: pointer = BotsSpellData {
            DamageTag: u32 = 1
            0x6d548702: pointer = GameCalculation {
                mFormulaParts: list[pointer] = {
                    0xf3cbe7b2 {
                        mSpellCalculationKey: hash = "TotalDamage"
                    }
                }
            }
            0xec17e271: list2[embed] = {
                0xb09016f6 {
                    EffectTag: u32 = 4096
                    EffectCalculation: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            NamedDataValueCalculationPart {
                                mDataValue: hash = "RootDuration"
                            }
                        }
                    }
                }
            }
            0x38382c53: list2[embed] = {
                0x150d1b92 {
                    0xe38f54f7: u32 = 1
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 2
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 4
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 1024
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 8
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 4096
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 2048
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxQAbility" = AbilityObject {
        mRootSpell: link = "Characters/Jinx/Spells/JinxQAbility/JinxQ"
        mChildSpells: list[link] = {
            "Characters/Jinx/Spells/JinxQAbility/JinxQ"
            "Characters/Jinx/Spells/JinxQAbility/JinxQAttack"
            "Characters/Jinx/Spells/JinxQAbility/JinxQAttack2"
            "Characters/Jinx/Spells/JinxQAbility/JinxQCritAttack"
            "Characters/Jinx/Spells/JinxQAbility/JinxQIcon"
            "Characters/Jinx/Spells/JinxQAbility/JinxQIconManager"
        }
        mName: string = "JinxQAbility"
    }
    "Characters/Jinx/Spells/JinxQAbility/JinxQIconManager" = SpellObject {
        ObjectName: string = "JinxQIconManager"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxQAbility/JinxQIconManager"
        mScriptName: string = "JinxQIconManager"
    }
    "Characters/Jinx/Spells/JinxQAbility/JinxQ" = SpellObject {
        ObjectName: string = "JinxQ"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxQAbility/JinxQ"
        mScriptName: string = "JinxQ"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 4
            mAffectsTypeFlags: u32 = 13519
            mSpellTags: list[string] = {
                "Trait_DamageAbility"
                "Trait_RecastOrReplaceSpell"
                "Trait_Toggle"
                "Trait_AoE"
            }
            DataValues: list2[embed] = {
                SpellDataValue {
                    Name: string = "RocketAoERadius"
                    Values: list[f32] = {
                        250
                        250
                        250
                        250
                        250
                        250
                        250
                    }
                }
                SpellDataValue {
                    Name: string = "RocketBonusRange"
                    Values: list[f32] = {
                        75
                        100
                        125
                        150
                        175
                        200
                        225
                    }
                }
                SpellDataValue {
                    Name: string = "MinigunAttackSpeedMax"
                    Values: list[f32] = {
                        5
                        30
                        55
                        80
                        105
                        130
                        155
                    }
                }
                SpellDataValue {
                    Name: string = "MinigunAttackSpeedDuration"
                    Values: list[f32] = {
                        2.5
                        2.5
                        2.5
                        2.5
                        2.5
                        2.5
                        2.5
                    }
                }
                SpellDataValue {
                    Name: string = "MinigunAttackSpeedStacks"
                    Values: list[f32] = {
                        3
                        3
                        3
                        3
                        3
                        3
                        3
                    }
                }
                SpellDataValue {
                    Name: string = "RocketTAD"
                    Values: list[f32] = {
                        1.1
                        1.1
                        1.1
                        1.1
                        1.1
                        1.1
                        1.1
                    }
                }
                SpellDataValue {
                    Name: string = "RocketASPDPenalty"
                    Values: list[f32] = {
                        0.1
                        0.1
                        0.1
                        0.1
                        0.1
                        0.1
                        0.1
                    }
                }
            }
            mSpellCalculations: map[hash,pointer] = {
                "RocketDamage" = GameCalculation {
                    0x72c5c2a8: u32 = 0
                    mFormulaParts: list[pointer] = {
                        StatByNamedDataValueCalculationPart {
                            mStat: u8 = 2
                            mDataValue: hash = "RocketTAD"
                        }
                    }
                }
            }
            0xfe87f21e: list2[embed] = {
                0xfe87f21e {
                    0x6166b756: hash = "RocketDamage"
                    0x7a9d64ea: bool = true
                    0x01987941: list2[pointer] = {
                        HasBuffCastRequirement {
                            mInvertResult: bool = true
                            mBuffName: hash = 0x5c76b14c
                            0x7b66f15d: bool = false
                        }
                    }
                }
            }
            mAnimationName: string = "Spell1"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Jinx/HUD/Icons2D/Jinx_Q1.dds"
                "ASSETS/Characters/Jinx/HUD/Icons2D/Jinx_Q2.dds"
            }
            mCastTime: f32 = 0.25
            0x11704a2b: f32 = 0.485
            CooldownTime: list[f32] = {
                0.9
                0.9
                0.9
                0.9
                0.9
                0.9
                0.9
            }
            Cooldown: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    0.9
                    0.9
                    0.9
                    0.9
                    0.9
                    0.9
                    0.9
                }
                0x0a3e0478: f32 = 0.9
            }
            mCooldownNotAffectedByCdr: bool = true
            mCantCancelWhileWindingUp: bool = true
            bIsToggleSpell: bool = true
            mDoesNotConsumeMana: bool = true
            mLockedSpellOriginationCastId: bool = true
            CastRange: list[f32] = {
                600
                600
                600
                600
                600
                600
                600
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    600
                    600
                    600
                    600
                    600
                    600
                    600
                }
                0x0a3e0478: f32 = 600
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 22.605
            MissileSpeed: f32 = 2000
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            Mana: list[f32] = {
                20
                20
                20
                20
                20
                20
            }
            0x210f9ec0: embed = 0x630af303 {
                Values: list[f32] = {
                    20
                    20
                    20
                    20
                    20
                    20
                }
                0x0a3e0478: f32 = 20
            }
            mTargetingTypeData: pointer = Self {}
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "JinxQ"
                    mFormat: link = 0xd7c27163
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_JinxQ_Name"
                        "keySummary" = "Spell_JinxQ_Summary"
                        "keyTooltip" = "Spell_JinxQ_Tooltip"
                        "keyCost" = "Spell_JinxQ_Cost"
                        "keyTooltipExtendedBelowLine" = "Spell_JinxQ_TooltipExtendedBelowLine"
                    }
                    mLists: map[string,embed] = {
                        "LevelUp" = TooltipInstanceList {
                            LevelCount: u32 = 5
                            Elements: list[embed] = {
                                TooltipInstanceListElement {
                                    Type: string = "RocketBonusRange"
                                    TypeIndex: i32 = 3
                                    NameOverride: string = "Spell_ListType_JinxRocketBonusRange"
                                }
                                TooltipInstanceListElement {
                                    Type: string = "MinigunAttackSpeedMax"
                                    TypeIndex: i32 = 1
                                    NameOverride: string = "Spell_ListType_JinxMinigunTotalAttackSpeed"
                                    Style: u32 = 1
                                }
                            }
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_JinxQ"
        }
        BotData: pointer = BotsSpellData {
            DamageTag: u32 = 0
            0x6d548702: pointer = GameCalculation {}
            0x38382c53: list2[embed] = {
                0x150d1b92 {
                    0xe38f54f7: u32 = 1
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 4
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 64
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 1024
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 8
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 2
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 4096
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 128
                    0x0717e686: bool = false
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxQAbility/JinxQAttack2" = SpellObject {
        ObjectName: string = "JinxQAttack2"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxQAbility/JinxQAttack2"
        mScriptName: string = "JinxQAttack2"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6794
            mAlternateName: string = "JinxQAttack"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        60
                        90
                        120
                        150
                        180
                        210
                        240
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 0.6
            mAnimationName: string = "Attack2"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Jinx/HUD/Icons2D/Jinx_Q1.dds"
            }
            0x11704a2b: f32 = 0.25
            0xf26881a0: f32 = 1
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            Cooldown: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
                0x0a3e0478: f32 = 0
            }
            CanCastWhileDisabled: bool = true
            mUseAutoattackCastTimeData: pointer = UseAutoattackCastTimeData {}
            CastRange: list[f32] = {
                10000
                10000
                10000
                10000
                10000
                10000
                10000
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    10000
                    10000
                    10000
                    10000
                    10000
                    10000
                    10000
                }
                0x0a3e0478: f32 = 10000
            }
            CastRadius: list[f32] = {
                710
                710
                710
                710
                710
                710
                710
            }
            CastRadiusSecondary: list[f32] = {
                280
                280
                280
                280
                280
                280
                280
            }
            CastConeDistance: f32 = 100
            LuaOnMissileUpdateDistanceInterval: f32 = 75
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 20
                MovementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 50
                    mOffsetInitialTargetHeight: f32 = 50
                    mStartBoneName: string = "Cstm_Buffbone_Rocket_Launcher"
                    mStartBoneSkinOverrides: map[u32,string] = {
                        60 = "Minigun_Engine"
                    }
                    mSpeed: f32 = 2000
                }
                VerticalFacing: pointer = VeritcalFacingMatchVelocity {}
                Behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            CastFrame: f32 = 7
            MissileSpeed: f32 = 2000
            mMissileEffectKey: hash = "Jinx_Q_Rocket_mis"
            mLineWidth: f32 = 20
            mHitBoneName: string = "R_hand"
            SelectionPriority: u32 = 1
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionAoe {
                        CenterLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 2
                        }
                        OverrideRadius: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                280
                                280
                                280
                                280
                                280
                                280
                            }
                            mValueType: u32 = 2
                        }
                        TextureRadiusOverrideName: file = 0x4ebdc2dbfb4a32e5
                    }
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxQAbility/JinxQCritAttack" = SpellObject {
        ObjectName: string = "JinxQCritAttack"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxQAbility/JinxQCritAttack"
        mScriptName: string = "JinxQCritAttack"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6794
            mAlternateName: string = "JinxQAttack"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        60
                        90
                        120
                        150
                        180
                        210
                        240
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 0.6
            mImgIconName: list[string] = {
                "ASSETS/Characters/Jinx/HUD/Icons2D/Jinx_Q1.dds"
            }
            0x11704a2b: f32 = 0.25
            0xf26881a0: f32 = 1
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            Cooldown: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
                0x0a3e0478: f32 = 0
            }
            CanCastWhileDisabled: bool = true
            mUseAutoattackCastTimeData: pointer = UseAutoattackCastTimeData {}
            CastRange: list[f32] = {
                10000
                10000
                10000
                10000
                10000
                10000
                10000
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    10000
                    10000
                    10000
                    10000
                    10000
                    10000
                    10000
                }
                0x0a3e0478: f32 = 10000
            }
            CastRadius: list[f32] = {
                710
                710
                710
                710
                710
                710
                710
            }
            CastRadiusSecondary: list[f32] = {
                280
                280
                280
                280
                280
                280
                280
            }
            CastConeDistance: f32 = 100
            LuaOnMissileUpdateDistanceInterval: f32 = 75
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 20
                MovementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 50
                    mOffsetInitialTargetHeight: f32 = 50
                    mStartBoneName: string = "Cstm_Buffbone_Rocket_Launcher"
                    mStartBoneSkinOverrides: map[u32,string] = {
                        60 = "Minigun_Engine"
                    }
                    mSpeed: f32 = 2000
                }
                VerticalFacing: pointer = VeritcalFacingMatchVelocity {}
                Behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            CastFrame: f32 = 7
            MissileSpeed: f32 = 2000
            mMissileEffectKey: hash = "Jinx_Q_Rocket_Crit_Mis"
            mLineWidth: f32 = 20
            mHitBoneName: string = "R_hand"
            SelectionPriority: u32 = 1
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionAoe {
                        CenterLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 2
                        }
                        OverrideRadius: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                280
                                280
                                280
                                280
                                280
                                280
                            }
                            mValueType: u32 = 2
                        }
                        TextureRadiusOverrideName: file = 0x4ebdc2dbfb4a32e5
                    }
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxQAbility/JinxQAttack" = SpellObject {
        ObjectName: string = "JinxQAttack"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxQAbility/JinxQAttack"
        mScriptName: string = "JinxQAttack"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6794
            mAlternateName: string = "JinxQAttack"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        60
                        90
                        120
                        150
                        180
                        210
                        240
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 0.6
            mImgIconName: list[string] = {
                "ASSETS/Characters/Jinx/HUD/Icons2D/Jinx_Q1.dds"
            }
            0x11704a2b: f32 = 0.25
            0xf26881a0: f32 = 1
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            Cooldown: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
                0x0a3e0478: f32 = 0
            }
            CanCastWhileDisabled: bool = true
            mUseAutoattackCastTimeData: pointer = UseAutoattackCastTimeData {}
            CastRange: list[f32] = {
                10000
                10000
                10000
                10000
                10000
                10000
                10000
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    10000
                    10000
                    10000
                    10000
                    10000
                    10000
                    10000
                }
                0x0a3e0478: f32 = 10000
            }
            CastRadius: list[f32] = {
                710
                710
                710
                710
                710
                710
                710
            }
            CastRadiusSecondary: list[f32] = {
                280
                280
                280
                280
                280
                280
                280
            }
            CastConeDistance: f32 = 100
            LuaOnMissileUpdateDistanceInterval: f32 = 75
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 20
                MovementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 50
                    mOffsetInitialTargetHeight: f32 = 50
                    mStartBoneName: string = "Cstm_Buffbone_Rocket_Launcher"
                    mStartBoneSkinOverrides: map[u32,string] = {
                        60 = "Minigun_Engine"
                    }
                    mSpeed: f32 = 2000
                }
                VerticalFacing: pointer = VeritcalFacingMatchVelocity {}
                Behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            CastFrame: f32 = 7
            MissileSpeed: f32 = 2000
            mMissileEffectKey: hash = "Jinx_Q_Rocket_mis"
            mLineWidth: f32 = 20
            mHitBoneName: string = "R_hand"
            SelectionPriority: u32 = 1
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionAoe {
                        CenterLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 2
                        }
                        OverrideRadius: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                280
                                280
                                280
                                280
                                280
                                280
                            }
                            mValueType: u32 = 2
                        }
                        TextureRadiusOverrideName: file = 0x4ebdc2dbfb4a32e5
                    }
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxQAbility/JinxQIcon" = SpellObject {
        ObjectName: string = "JinxQIcon"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxQAbility/JinxQIcon"
        mScriptName: string = "JinxQIcon"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_JinxQIcon"
        }
    }
    "Characters/Jinx/Spells/JinxCatchMe" = SpellObject {
        ObjectName: string = "JinxCatchMe"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxCatchMe"
        mScriptName: string = "JinxCatchMe"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_JinxCatchMe"
        }
    }
    "Characters/Jinx/Spells/JinxPassiveMarkerAbility" = AbilityObject {
        mRootSpell: link = "Characters/Jinx/Spells/JinxPassiveMarkerAbility/JinxPassiveMarker"
        mChildSpells: list[link] = {
            "Characters/Jinx/Spells/JinxPassiveMarkerAbility/JinxPassiveMarker"
            "Characters/Jinx/Spells/JinxPassiveMarkerAbility/JinxPassiveKillAttackSpeed"
            "Characters/Jinx/Spells/JinxPassiveMarkerAbility/JinxPassiveKill"
        }
        mName: string = "JinxPassiveMarkerAbility"
        mType: u8 = 3
    }
    "Characters/Jinx/Spells/JinxPassiveMarkerAbility/JinxPassiveKill" = SpellObject {
        ObjectName: string = "JinxPassiveKill"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxPassiveMarkerAbility/JinxPassiveKill"
        mScriptName: string = "JinxPassiveKill"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_JinxPassiveKill"
        }
    }
    "Characters/Jinx/Spells/JinxPassiveMarkerAbility/JinxPassiveKillAttackSpeed" = SpellObject {
        ObjectName: string = "JinxPassiveKillAttackSpeed"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxPassiveMarkerAbility/JinxPassiveKillAttackSpeed"
        mScriptName: string = "JinxPassiveKillAttackSpeed"
        mSpell: pointer = SpellDataResource {
            mImgIconName: list[string] = {
                "ASSETS/Characters/Jinx/HUD/Icons2D/Jinx_Passive.dds"
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_JinxPassiveKillAttackSpeed"
        }
    }
    "Characters/Jinx/Spells/JinxPassiveMarkerAbility/JinxPassiveMarker" = SpellObject {
        ObjectName: string = "JinxPassiveMarker"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxPassiveMarkerAbility/JinxPassiveMarker"
        mScriptName: string = "JinxPassiveMarker"
        mSpell: pointer = SpellDataResource {
            DataValues: list2[embed] = {
                SpellDataValue {
                    Name: string = "BuffDuration"
                    Values: list[f32] = {
                        6
                        6
                        6
                        6
                        6
                        6
                        6
                    }
                }
                SpellDataValue {
                    Name: string = "ASBuff"
                    Values: list[f32] = {
                        25
                        25
                        25
                        25
                        25
                        25
                        25
                    }
                }
                SpellDataValue {
                    Name: string = "MSBuff"
                    Values: list[f32] = {
                        175
                        175
                        175
                        175
                        175
                        175
                        175
                    }
                }
                SpellDataValue {
                    Name: string = "MSDecayRate"
                    Values: list[f32] = {
                        0.875
                        0.875
                        0.875
                        0.875
                        0.875
                        0.875
                        0.875
                    }
                }
                SpellDataValue {
                    Name: string = "AssistMarkerDuration"
                    Values: list[f32] = {
                        3
                        3
                        3
                        3
                        3
                        3
                        3
                    }
                }
            }
            mImgIconName: list[string] = {
                "ASSETS/Characters/Jinx/HUD/Icons2D/Jinx_Passive.dds"
            }
            CastRange: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
                0x0a3e0478: f32 = 0
            }
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "JinxPassiveMarker"
                    mFormat: link = 0x476ec0b8
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_JinxPassiveMarker_Name"
                        "keySummary" = "Spell_JinxPassiveMarker_Summary"
                        "keyTooltip" = "Spell_JinxPassiveMarker_Tooltip"
                        "keyTooltipExtended" = "Spell_JinxPassiveMarker_TooltipExtended"
                    }
                }
            }
        }
    }
    "Characters/Jinx/Spells/ItemHurricaneJinxAttack" = SpellObject {
        ObjectName: string = "ItemHurricaneJinxAttack"
        ObjectPath: hash = "Characters/Jinx/Spells/ItemHurricaneJinxAttack"
        mScriptName: string = "ItemHurricaneJinxAttack"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 4
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "Disintegrate"
            mSpellTags: list[string] = {
                "Trait_NonPrimaryAttack"
            }
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        45
                        85
                        125
                        165
                        205
                        245
                        285
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 0.7
            mAnimationName: string = "Spell3"
            mImgIconName: list[string] = {
                "Annie_Disintegrate.dds"
            }
            0x11704a2b: f32 = 0.25
            0xf26881a0: f32 = 1
            CooldownTime: list[f32] = {
                4
                4
                4
                4
                4
                4
                4
            }
            Cooldown: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    4
                    4
                    4
                    4
                    4
                    4
                    4
                }
                0x0a3e0478: f32 = 4
            }
            mCantCancelWhileWindingUp: bool = true
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                1400
                1400
                1400
                1400
                1400
                1400
                1400
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    1400
                    1400
                    1400
                    1400
                    1400
                    1400
                    1400
                }
                0x0a3e0478: f32 = 1400
            }
            CastRadius: list[f32] = {
                710
                710
                710
                710
                710
                710
                710
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                MovementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "root"
                    mSpeed: f32 = 2000
                }
                VerticalFacing: pointer = VeritcalFacingMatchVelocity {}
                Behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            CastFrame: f32 = 8.7
            MissileSpeed: f32 = 2000
            mMissileEffectKey: hash = "Jinx_Q_Rocket_Hurricane_Mis"
            mHitEffectName: string = "doesnotexist.troy"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_buffbone_glb_chest_loc"
            SelectionPriority: u32 = 1
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxRAbility" = AbilityObject {
        mRootSpell: link = "Characters/Jinx/Spells/JinxRAbility/JinxR"
        mChildSpells: list[link] = {
            "Characters/Jinx/Spells/JinxRAbility/JinxR"
        }
        mName: string = "JinxRAbility"
        mType: u8 = 2
        AbilityTraits: u32 = 3
    }
    "Characters/Jinx/Spells/JinxRAbility/JinxR" = SpellObject {
        ObjectName: string = "JinxR"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxRAbility/JinxR"
        mScriptName: string = "JinxR"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 4106
            mRequiredUnitTags: embed = ObjectTags {
                mObjectTagList: list2[hash] = {
                    "Champion"
                }
            }
            mAlternateName: string = "JinxR"
            mSpellTags: list[string] = {
                "Trait_Ultimate"
                "Trait_DamageAbility"
                "Trait_RecastOrReplaceSpell"
                "Trait_AoE"
            }
            DataValues: list2[embed] = {
                SpellDataValue {
                    Name: string = "BaseDamage"
                    Values: list[f32] = {
                        5
                        20
                        35
                        50
                        65
                        80
                        95
                    }
                }
                SpellDataValue {
                    Name: string = "MaxDamage"
                    Values: list[f32] = {
                        50
                        200
                        350
                        500
                        650
                        800
                        950
                    }
                }
                SpellDataValue {
                    Name: string = "PercentDamage"
                    Values: list[f32] = {
                        20
                        25
                        30
                        35
                        40
                        45
                        50
                    }
                }
                SpellDataValue {
                    Name: string = "AoEDamageMult"
                    Values: list[f32] = {
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                    }
                }
                SpellDataValue {
                    Name: string = "MonsterExecuteMax"
                    Values: list[f32] = {
                        1200
                        1200
                        1200
                        1200
                        1200
                        1200
                        1200
                    }
                }
                SpellDataValue {
                    Name: string = "AoERadius"
                    Values: list[f32] = {
                        400
                        400
                        400
                        400
                        400
                        400
                        400
                    }
                }
            }
            0xf9c2333e: map[hash,embed] = {
                0x497ae878 = SpellEffectAmount {
                    Value: list[f32] = {
                        60
                        50
                        40
                        30
                        20
                        10
                        10
                    }
                }
            }
            mSpellCalculations: map[hash,pointer] = {
                "DamageFloor" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        NamedDataValueCalculationPart {
                            mDataValue: hash = "BaseDamage"
                        }
                        StatByCoefficientCalculationPart {
                            mStat: u8 = 2
                            mStatFormula: u8 = 2
                            mCoefficient: f32 = 0.12
                        }
                    }
                }
                "DamageMax" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        NamedDataValueCalculationPart {
                            mDataValue: hash = "MaxDamage"
                        }
                        StatByCoefficientCalculationPart {
                            mStat: u8 = 2
                            mStatFormula: u8 = 2
                            mCoefficient: f32 = 1.2
                        }
                    }
                }
            }
            mAnimationName: string = "Spell4"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Jinx/HUD/Icons2D/Jinx_R.dds"
            }
            mMinimapIconName: file = 0x5949d5489fe00138
            mCastTime: f32 = 0.6
            0x11704a2b: f32 = 0.25
            0xf26881a0: f32 = 1
            CooldownTime: list[f32] = {
                85
                85
                65
                45
                45
                45
                45
            }
            Cooldown: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    85
                    85
                    65
                    45
                    45
                    45
                    45
                }
            }
            mCantCancelWhileWindingUp: bool = true
            mSpellRevealsChampion: bool = false
            mUseMinimapTargeting: bool = true
            mMinimapIconRotation: bool = true
            AlwaysSnapFacing: bool = true
            UseAnimatorFramerate: bool = true
            CastRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    25000
                    25000
                    25000
                    25000
                    25000
                    25000
                    25000
                }
                0x0a3e0478: f32 = 25000
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            LuaOnMissileUpdateDistanceInterval: f32 = 1350
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 140
                MovementComponent: pointer = FixedSpeedMovement {
                    mUseHeightOffsetAtEnd: bool = true
                    mTracksTarget: bool = false
                    mStartBoneName: string = "Rocket_Launcher_Mouth_Top"
                    mProjectTargetToCastRange: bool = true
                    mSpeed: f32 = 1700
                }
                VisibilityComponent: pointer = Defaultvisibility {
                    mPerceptionBubbleRadius: f32 = 1000
                }
                HeightSolver: pointer = FollowTerrainHeightSolver {}
                VerticalFacing: pointer = VerticalFacingFaceTarget {}
                Behaviors: list[pointer] = {
                    CastOnHit {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 3
            CastFrame: f32 = 7.5
            MissileSpeed: f32 = 1700
            mMissileEffectKey: hash = "Jinx_R_Mis"
            mLineWidth: f32 = 140
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            Mana: list[f32] = {
                100
                100
                100
                100
                100
                100
            }
            0x210f9ec0: embed = 0x630af303 {
                Values: list[f32] = {
                    100
                    100
                    100
                    100
                    100
                    100
                }
                0x0a3e0478: f32 = 100
            }
            mTargetingTypeData: pointer = Location {}
            mCastingBreaksStealth: bool = true
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "JinxR"
                    mFormat: link = 0xd7c27163
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_JinxR_Name"
                        "keySummary" = "Spell_JinxR_Summary"
                        "keyTooltip" = "Spell_JinxR_Tooltip"
                    }
                    mLists: map[string,embed] = {
                        "LevelUp" = TooltipInstanceList {
                            LevelCount: u32 = 3
                            Elements: list[embed] = {
                                TooltipInstanceListElement {
                                    Type: string = "BaseDamage"
                                    TypeIndex: i32 = 1
                                    NameOverride: string = "Spell_ListType_MinimumDamage"
                                }
                                TooltipInstanceListElement {
                                    Type: string = "MaxDamage"
                                    TypeIndex: i32 = 2
                                    NameOverride: string = "Spell_ListType_MaximumDamage"
                                }
                                TooltipInstanceListElement {
                                    Type: string = "PercentDamage"
                                    TypeIndex: i32 = 3
                                    NameOverride: string = "Spell_ListType_PercentMissingHealthDamage"
                                    Style: u32 = 1
                                }
                                TooltipInstanceListElement {
                                    Type: string = "Cooldown"
                                }
                            }
                        }
                    }
                }
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionLine {
                        StartLocator: embed = DrawablePositionLocator {
                            OrientationType: u32 = 1
                        }
                        EndLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        FallbackDirection: u32 = 3
                        UseGlobalLineIndicator: bool = true
                        LineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                140
                                140
                                140
                                140
                                140
                                140
                            }
                            mValueType: u32 = 2
                        }
                        TextureBaseOverrideName: file = 0x9bc73a27e067c4fc
                        TextureTargetOverrideName: file = 0x76c66d40b0483776
                    }
                }
            }
        }
        BotData: pointer = BotsSpellData {
            DamageTag: u32 = 0
            0x6d548702: pointer = GameCalculation {
                mFormulaParts: list[pointer] = {
                    0xf3cbe7b2 {
                        mSpellCalculationKey: hash = "DamageMax"
                    }
                }
            }
            0x38382c53: list2[embed] = {
                0x150d1b92 {
                    0xe38f54f7: u32 = 8
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 4096
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 8
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 4096
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 2048
                }
            }
            0x591f8423: option[f32] = {
                30000
            }
        }
    }
    "Characters/Jinx/Spells/JinxCaitAgitate" = SpellObject {
        ObjectName: string = "JinxCaitAgitate"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxCaitAgitate"
        mScriptName: string = "JinxCaitAgitate"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_JinxCaitAgitate"
        }
    }
    "Characters/Jinx/Spells/JinxCritAttack" = SpellObject {
        ObjectName: string = "JinxCritAttack"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxCritAttack"
        mScriptName: string = "JinxCritAttack"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "JinxBasicAttack"
            0x11704a2b: f32 = 0.45964912
            mApplyMaterialOnHitSound: bool = true
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                600
                600
                600
                600
                600
                600
                600
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    600
                    600
                    600
                    600
                    600
                    600
                    600
                }
                0x0a3e0478: f32 = 600
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                MovementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "Buffbone_Glb_Weapon_1"
                    mSpeed: f32 = 2750
                }
                VerticalFacing: pointer = VeritcalFacingMatchVelocity {}
                Behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            CastFrame: f32 = 8.5
            MissileSpeed: f32 = 2750
            mMissileEffectKey: hash = "Jinx_Q_Minigun_Mis"
            mHitEffectKey: hash = "Jinx_Q_Minigun_Tar"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {}
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxCritAttack5" = SpellObject {
        ObjectName: string = "JinxCritAttack5"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxCritAttack5"
        mScriptName: string = "JinxCritAttack5"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "JinxBasicAttack"
            mAnimationName: string = "Attack5"
            0x11704a2b: f32 = 0.45964912
            mApplyMaterialOnHitSound: bool = true
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                600
                600
                600
                600
                600
                600
                600
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    600
                    600
                    600
                    600
                    600
                    600
                    600
                }
                0x0a3e0478: f32 = 600
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                MovementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "Buffbone_Glb_Weapon_1"
                    mSpeed: f32 = 2750
                }
                VerticalFacing: pointer = VeritcalFacingMatchVelocity {}
                Behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            CastFrame: f32 = 8.5
            MissileSpeed: f32 = 2750
            mMissileEffectKey: hash = "Jinx_Q_Minigun_Mis"
            mHitEffectKey: hash = "Jinx_Q_Minigun_Tar"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {}
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxCritAttack4" = SpellObject {
        ObjectName: string = "JinxCritAttack4"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxCritAttack4"
        mScriptName: string = "JinxCritAttack4"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "JinxBasicAttack"
            mAnimationName: string = "Attack4"
            0x11704a2b: f32 = 0.45964912
            mApplyMaterialOnHitSound: bool = true
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                600
                600
                600
                600
                600
                600
                600
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    600
                    600
                    600
                    600
                    600
                    600
                    600
                }
                0x0a3e0478: f32 = 600
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                MovementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "Buffbone_Glb_Weapon_1"
                    mSpeed: f32 = 2750
                }
                VerticalFacing: pointer = VeritcalFacingMatchVelocity {}
                Behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            CastFrame: f32 = 8.5
            MissileSpeed: f32 = 2750
            mMissileEffectKey: hash = "Jinx_Q_Minigun_Mis"
            mHitEffectKey: hash = "Jinx_Q_Minigun_Tar"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {}
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxRunCycleManager" = SpellObject {
        ObjectName: string = "JinxRunCycleManager"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxRunCycleManager"
        mScriptName: string = "JinxRunCycleManager"
    }
    "Characters/Jinx/Spells/JinxCritAttack6" = SpellObject {
        ObjectName: string = "JinxCritAttack6"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxCritAttack6"
        mScriptName: string = "JinxCritAttack6"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "JinxBasicAttack"
            mAnimationName: string = "Attack6"
            0x11704a2b: f32 = 0.45964912
            mApplyMaterialOnHitSound: bool = true
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                600
                600
                600
                600
                600
                600
                600
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    600
                    600
                    600
                    600
                    600
                    600
                    600
                }
                0x0a3e0478: f32 = 600
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                MovementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "Buffbone_Glb_Weapon_1"
                    mSpeed: f32 = 2750
                }
                VerticalFacing: pointer = VeritcalFacingMatchVelocity {}
                Behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            CastFrame: f32 = 8.5
            MissileSpeed: f32 = 2750
            mMissileEffectKey: hash = "Jinx_Q_Minigun_Mis"
            mHitEffectKey: hash = "Jinx_Q_Minigun_Tar"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {}
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxCritAttack3" = SpellObject {
        ObjectName: string = "JinxCritAttack3"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxCritAttack3"
        mScriptName: string = "JinxCritAttack3"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "JinxBasicAttack"
            mAnimationName: string = "Attack3"
            0x11704a2b: f32 = 0.45964912
            mApplyMaterialOnHitSound: bool = true
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                600
                600
                600
                600
                600
                600
                600
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    600
                    600
                    600
                    600
                    600
                    600
                    600
                }
                0x0a3e0478: f32 = 600
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                MovementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "Buffbone_Glb_Weapon_1"
                    mSpeed: f32 = 2750
                }
                VerticalFacing: pointer = VeritcalFacingMatchVelocity {}
                Behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            CastFrame: f32 = 8.5
            MissileSpeed: f32 = 2750
            mMissileEffectKey: hash = "Jinx_Q_Minigun_Mis"
            mHitEffectKey: hash = "Jinx_Q_Minigun_Tar"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {}
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxCritAttack2" = SpellObject {
        ObjectName: string = "JinxCritAttack2"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxCritAttack2"
        mScriptName: string = "JinxCritAttack2"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "JinxBasicAttack"
            mAnimationName: string = "Attack2"
            0x11704a2b: f32 = 0.45964912
            mApplyMaterialOnHitSound: bool = true
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                600
                600
                600
                600
                600
                600
                600
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    600
                    600
                    600
                    600
                    600
                    600
                    600
                }
                0x0a3e0478: f32 = 600
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                MovementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "Buffbone_Glb_Weapon_1"
                    mSpeed: f32 = 2750
                }
                VerticalFacing: pointer = VeritcalFacingMatchVelocity {}
                Behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            CastFrame: f32 = 8.5
            MissileSpeed: f32 = 2750
            mMissileEffectKey: hash = "Jinx_Q_Minigun_Mis"
            mHitEffectKey: hash = "Jinx_Q_Minigun_Tar"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {}
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxBasicAttack" = SpellObject {
        ObjectName: string = "JinxBasicAttack"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxBasicAttack"
        mScriptName: string = "JinxBasicAttack"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "JinxBasicAttack"
            mImgIconName: list[string] = {
                "Udyr_TigerStance.dds"
            }
            0x11704a2b: f32 = 0.25
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            Cooldown: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
                0x0a3e0478: f32 = 0
            }
            CanCastWhileDisabled: bool = true
            mApplyMaterialOnHitSound: bool = true
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                600
                600
                600
                600
                600
                600
                600
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    600
                    600
                    600
                    600
                    600
                    600
                    600
                }
                0x0a3e0478: f32 = 600
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                MovementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "Buffbone_Glb_Weapon_1"
                    mSpeed: f32 = 2750
                }
                VerticalFacing: pointer = VeritcalFacingMatchVelocity {}
                Behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            CastFrame: f32 = 8.5
            MissileSpeed: f32 = 2750
            mMissileEffectKey: hash = "Jinx_Q_Minigun_Mis"
            mHitEffectKey: hash = "Jinx_Q_Minigun_Tar"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxBasicAttack5" = SpellObject {
        ObjectName: string = "JinxBasicAttack5"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxBasicAttack5"
        mScriptName: string = "JinxBasicAttack5"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "JinxBasicAttack"
            mAnimationName: string = "Attack5"
            mImgIconName: list[string] = {
                "Udyr_TigerStance.dds"
            }
            0x11704a2b: f32 = 0.25
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            Cooldown: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
                0x0a3e0478: f32 = 0
            }
            CanCastWhileDisabled: bool = true
            mApplyMaterialOnHitSound: bool = true
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                600
                600
                600
                600
                600
                600
                600
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    600
                    600
                    600
                    600
                    600
                    600
                    600
                }
                0x0a3e0478: f32 = 600
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                MovementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "Buffbone_Glb_Weapon_1"
                    mSpeed: f32 = 2750
                }
                VerticalFacing: pointer = VeritcalFacingMatchVelocity {}
                Behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            CastFrame: f32 = 8.5
            MissileSpeed: f32 = 2750
            mMissileEffectKey: hash = "Jinx_Q_Minigun_Mis"
            mHitEffectKey: hash = "Jinx_Q_Minigun_Tar"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxBasicAttack4" = SpellObject {
        ObjectName: string = "JinxBasicAttack4"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxBasicAttack4"
        mScriptName: string = "JinxBasicAttack4"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "JinxBasicAttack"
            mAnimationName: string = "Attack4"
            mImgIconName: list[string] = {
                "Udyr_TigerStance.dds"
            }
            0x11704a2b: f32 = 0.25
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            Cooldown: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
                0x0a3e0478: f32 = 0
            }
            CanCastWhileDisabled: bool = true
            mApplyMaterialOnHitSound: bool = true
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                600
                600
                600
                600
                600
                600
                600
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    600
                    600
                    600
                    600
                    600
                    600
                    600
                }
                0x0a3e0478: f32 = 600
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                MovementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "Buffbone_Glb_Weapon_1"
                    mSpeed: f32 = 2750
                }
                VerticalFacing: pointer = VeritcalFacingMatchVelocity {}
                Behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            CastFrame: f32 = 8.5
            MissileSpeed: f32 = 2750
            mMissileEffectKey: hash = "Jinx_Q_Minigun_Mis"
            mHitEffectKey: hash = "Jinx_Q_Minigun_Tar"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxBasicAttack6" = SpellObject {
        ObjectName: string = "JinxBasicAttack6"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxBasicAttack6"
        mScriptName: string = "JinxBasicAttack6"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "JinxBasicAttack"
            mAnimationName: string = "Attack6"
            mImgIconName: list[string] = {
                "Udyr_TigerStance.dds"
            }
            0x11704a2b: f32 = 0.25
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            Cooldown: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
                0x0a3e0478: f32 = 0
            }
            CanCastWhileDisabled: bool = true
            mApplyMaterialOnHitSound: bool = true
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                600
                600
                600
                600
                600
                600
                600
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    600
                    600
                    600
                    600
                    600
                    600
                    600
                }
                0x0a3e0478: f32 = 600
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                MovementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "Buffbone_Glb_Weapon_1"
                    mSpeed: f32 = 2750
                }
                VerticalFacing: pointer = VeritcalFacingMatchVelocity {}
                Behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            CastFrame: f32 = 8.5
            MissileSpeed: f32 = 2750
            mMissileEffectKey: hash = "Jinx_Q_Minigun_Mis"
            mHitEffectKey: hash = "Jinx_Q_Minigun_Tar"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxBasicAttack3" = SpellObject {
        ObjectName: string = "JinxBasicAttack3"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxBasicAttack3"
        mScriptName: string = "JinxBasicAttack3"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "JinxBasicAttack"
            mAnimationName: string = "Attack3"
            mImgIconName: list[string] = {
                "Udyr_TigerStance.dds"
            }
            0x11704a2b: f32 = 0.25
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            Cooldown: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
                0x0a3e0478: f32 = 0
            }
            CanCastWhileDisabled: bool = true
            mApplyMaterialOnHitSound: bool = true
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                600
                600
                600
                600
                600
                600
                600
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    600
                    600
                    600
                    600
                    600
                    600
                    600
                }
                0x0a3e0478: f32 = 600
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                MovementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "Buffbone_Glb_Weapon_1"
                    mSpeed: f32 = 2750
                }
                VerticalFacing: pointer = VeritcalFacingMatchVelocity {}
                Behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            CastFrame: f32 = 8.5
            MissileSpeed: f32 = 2750
            mMissileEffectKey: hash = "Jinx_Q_Minigun_Mis"
            mHitEffectKey: hash = "Jinx_Q_Minigun_Tar"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxBasicAttack2" = SpellObject {
        ObjectName: string = "JinxBasicAttack2"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxBasicAttack2"
        mScriptName: string = "JinxBasicAttack2"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "JinxBasicAttack"
            mAnimationName: string = "Attack2"
            mImgIconName: list[string] = {
                "Udyr_TigerStance.dds"
            }
            0x11704a2b: f32 = 0.25
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            Cooldown: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
                0x0a3e0478: f32 = 0
            }
            CanCastWhileDisabled: bool = true
            mApplyMaterialOnHitSound: bool = true
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                600
                600
                600
                600
                600
                600
                600
            }
            0x0e1136d1: embed = 0x0a0eddc9 {
                Values: list[f32] = {
                    600
                    600
                    600
                    600
                    600
                    600
                    600
                }
                0x0a3e0478: f32 = 600
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                MovementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "Buffbone_Glb_Weapon_1"
                    mSpeed: f32 = 2750
                }
                VerticalFacing: pointer = VeritcalFacingMatchVelocity {}
                Behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            CastFrame: f32 = 8.5
            MissileSpeed: f32 = 2750
            mMissileEffectKey: hash = "Jinx_Q_Minigun_Mis"
            mHitEffectKey: hash = "Jinx_Q_Minigun_Tar"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Jinx/Spells/JinxCatchMeEnemy" = SpellObject {
        ObjectName: string = "JinxCatchMeEnemy"
        ObjectPath: hash = "Characters/Jinx/Spells/JinxCatchMeEnemy"
        mScriptName: string = "JinxCatchMeEnemy"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_JinxCatchMeEnemy"
        }
    }
    0xfbb1fc59 = SpellObject {
        ObjectName: string = "JinxSkin60MultiKillTracker"
        ObjectPath: hash = 0xfbb1fc59
        mScriptName: string = "JinxSkin60MultiKillTracker"
    }
    0xffc12e05 = SpellObject {
        ObjectName: string = "JinxSkin60Manager"
        ObjectPath: hash = 0xffc12e05
        mScriptName: string = "JinxSkin60Manager"
    }
    0x2769234f = SpellObject {
        ObjectName: string = "Crepe_JinxVsEkko_JinxPoroTracker"
        ObjectPath: hash = 0x2769234f
        mScriptName: string = "Crepe_JinxVsEkko_JinxPoroTracker"
        mSpell: pointer = SpellDataResource {
            mImgIconName: list[string] = {
                "ASSETS/Characters/Jinx/HUD/Icons2D/JinxEkko64.dds"
            }
        }
        mBuff: pointer = BuffData {
            mTooltipData: pointer = TooltipInstanceBuff {
                mObjectName: string = "Crepe_JinxVsEkko_JinxPoroTracker"
                mFormat: link = 0x2ca8f134
                mLocKeys: map[string,string] = {
                    "keyName" = "Quests_EkkoTeam_Name"
                    "keyTooltip" = "Quests_JinxVsEkko_JinxInstructions"
                }
            }
        }
    }
    0x8c4cdccf = SpellObject {
        ObjectName: string = "Crepe_JinxVsEkko_JinxWin"
        ObjectPath: hash = 0x8c4cdccf
        mScriptName: string = "Crepe_JinxVsEkko_JinxWin"
        mBuff: pointer = BuffData {}
    }
    0x9b5aa500 = SpellObject {
        ObjectName: string = "Crepe_JinxVsEkko_JinxReward"
        ObjectPath: hash = 0x9b5aa500
        mScriptName: string = "Crepe_JinxVsEkko_JinxReward"
        mSpell: pointer = SpellDataResource {
            DataValues: list2[embed] = {
                SpellDataValue {
                    Name: string = "AH"
                    Values: list[f32] = {
                        10
                        10
                        10
                        10
                        10
                        10
                        10
                    }
                }
            }
            mImgIconName: list[string] = {
                "ASSETS/Characters/Jinx/HUD/Icons2D/JinxEkko64.dds"
            }
        }
        mBuff: pointer = BuffData {
            mTooltipData: pointer = TooltipInstanceBuff {
                mObjectName: string = "Crepe_JinxVsEkko_JinxReward"
                mFormat: link = 0x2ca8f134
                mLocKeys: map[string,string] = {
                    "keyName" = "Crepe_JinxVsEkko_JinxReward"
                    "keyTooltip" = "Crepe_JinxVsEkko_JinxReward_Tooltip"
                }
            }
        }
    }
    0xfd28d9ad = SpellObject {
        ObjectName: string = "Crepe_JinxVsEkko_JinxStart"
        ObjectPath: hash = 0xfd28d9ad
        mScriptName: string = "Crepe_JinxVsEkko_JinxStart"
        mSpell: pointer = SpellDataResource {
            mImgIconName: list[string] = {
                "ASSETS/Characters/Jinx/HUD/Icons2D/JinxEkko64.dds"
            }
        }
        mBuff: pointer = BuffData {
            mTooltipData: pointer = TooltipInstanceBuff {
                mObjectName: string = "Crepe_JinxVsEkko_JinxStart"
                mFormat: link = 0x2ca8f134
                mLocKeys: map[string,string] = {
                    "keyName" = "Quests_EkkoTeam_Name"
                    "keyTooltip" = "Quests_JinxVsEkko_JinxInstructions"
                }
            }
        }
    }
    0x30a9896f = SpellObject {
        ObjectName: string = "Crepe_JinxVsCaitlyn_CaitlynLose"
        ObjectPath: hash = 0x30a9896f
        mScriptName: string = "Crepe_JinxVsCaitlyn_CaitlynLose"
        mSpell: pointer = SpellDataResource {
            mImgIconName: list[string] = {
                "ASSETS/Characters/Jhin/HUD/Icons2D/JhinQuestLoser.dds"
            }
        }
        mBuff: pointer = BuffData {
            mTooltipData: pointer = TooltipInstanceBuff {
                mObjectName: string = "Crepe_JinxVsCaitlyn_CaitlynLose"
                mFormat: link = 0x2ca8f134
                mLocKeys: map[string,string] = {
                    "keyName" = "Crepe_JinxCait_CaitLose"
                    "keyTooltip" = "Crepe_JinxCait_CaitLose_Tooltip"
                }
            }
            CanTimeoutWhileCasting: bool = false
            mShowDuration: bool = false
            mShowAccumulatedDuration: bool = false
        }
    }
    0x576c018a = SpellObject {
        ObjectName: string = "Crepe_JinxVsCaitlyn_JinxReward"
        ObjectPath: hash = 0x576c018a
        mScriptName: string = "Crepe_JinxVsCaitlyn_JinxReward"
        mSpell: pointer = SpellDataResource {
            mImgIconName: list[string] = {
                "ASSETS/Characters/Jhin/HUD/Icons2D/JhinQuestVictory.dds"
            }
        }
        mBuff: pointer = BuffData {
            mTooltipData: pointer = TooltipInstanceBuff {
                mObjectName: string = "Crepe_JinxVsCaitlyn_JinxReward"
                mFormat: link = 0x2ca8f134
                mLocKeys: map[string,string] = {
                    "keyName" = "Crepe_JinxCait_JinxReward"
                    "keyTooltip" = "Crepe_JinxCait_JinxReward_Tooltip"
                }
            }
        }
    }
    0x748519a9 = SpellObject {
        ObjectName: string = "Crepe_JinxVsCaitlyn_JinxWin"
        ObjectPath: hash = 0x748519a9
        mScriptName: string = "Crepe_JinxVsCaitlyn_JinxWin"
        mBuff: pointer = BuffData {}
    }
    0x79fd7399 = SpellObject {
        ObjectName: string = "Crepe_JinxVsCaitlyn_JinxDescription"
        ObjectPath: hash = 0x79fd7399
        mScriptName: string = "Crepe_JinxVsCaitlyn_JinxDescription"
        mSpell: pointer = SpellDataResource {
            mImgIconName: list[string] = {
                "ASSETS/Characters/Jinx/HUD/Icons2D/JinxCaitlyn64.dds"
            }
        }
        mBuff: pointer = BuffData {
            mTooltipData: pointer = TooltipInstanceBuff {
                mObjectName: string = "Crepe_JinxVsCaitlyn_JinxDescription"
                mFormat: link = 0xb34f999a
                mLocKeys: map[string,string] = {
                    "keyName" = "Quests_JinxVsCaitlyn_Name"
                    "keyTooltip" = "Quests_JinxVsCaitlyn_InstructionsJinx"
                }
            }
        }
    }
    0x8d1a328f = SpellObject {
        ObjectName: string = "Crepe_JinxVsCaitlyn_JinxStart"
        ObjectPath: hash = 0x8d1a328f
        mScriptName: string = "Crepe_JinxVsCaitlyn_JinxStart"
        mSpell: pointer = SpellDataResource {
            mImgIconName: list[string] = {
                "ASSETS/Characters/Jinx/HUD/Icons2D/JinxCaitlyn64.dds"
            }
        }
        mBuff: pointer = BuffData {
            mTooltipData: pointer = TooltipInstanceBuff {
                mObjectName: string = "Crepe_JinxVsCaitlyn_JinxStart"
                mFormat: link = 0xb34f999a
                mLocKeys: map[string,string] = {
                    "keyName" = "Quests_JinxVsCaitlyn_Name"
                    "keyTooltip" = "Quests_JinxVsCaitlyn_InstructionsJinx"
                }
            }
        }
    }
    "Characters/Jinx/CharacterRecords/Root" = CharacterRecord {
        mCharacterName: string = "Jinx"
        0x8662cf12: embed = 0xce9b917b {
            0xb35aa769: f32 = 630
        }
        0x4d37af28: embed = 0xce9b917b {
            0xb35aa769: f32 = 105
        }
        0x9eedebad: embed = 0xce9b917b {
            0xb35aa769: f32 = 0.75
        }
        0x913157bb: embed = 0xce9b917b {
            0xb35aa769: f32 = 0.1
        }
        PrimaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 0
            0x726ee5cd: embed = 0xce9b917b {
                0xb35aa769: f32 = 260
            }
            0x6216bf7b: embed = 0xce9b917b {
                0xb35aa769: f32 = 50
            }
            0xc4ab3550: embed = 0xce9b917b {
                0xb35aa769: f32 = 1.34
            }
            0x3a509002: embed = 0xce9b917b {
                0xb35aa769: f32 = 0.2
            }
        }
        0x4af40dc3: embed = 0xce9b917b {
            0xb35aa769: f32 = 59
        }
        0xe2b5d80d: embed = 0xce9b917b {
            0xb35aa769: f32 = 3.25
        }
        0xea6100d5: embed = 0xce9b917b {
            0xb35aa769: f32 = 26
        }
        0x18956a21: embed = 0xce9b917b {
            0xb35aa769: f32 = 4.2
        }
        BaseMR: embed = 0xce9b917b {
            0xb35aa769: f32 = 33
        }
        0x01262a25: embed = 0xce9b917b {
            0xb35aa769: f32 = 1.1
        }
        CritDamageMultiplier: f32 = 2
        0xe62d9d92: embed = 0xce9b917b {
            0xb35aa769: f32 = 325
        }
        0x7bd4b298: embed = 0xce9b917b {
            0xb35aa769: f32 = 525
        }
        0x836cc82a: embed = 0xce9b917b {
            0xb35aa769: f32 = 0.625
        }
        0x4f89c991: embed = 0xce9b917b {
            0xb35aa769: f32 = 0.625
        }
        0xb9f2b365: embed = 0xce9b917b {
            0xb35aa769: f32 = 1
        }
        AcquisitionRange: f32 = 550
        BasicAttack: embed = AttackSlotData {
            mAttackTotalTime: option[f32] = {
                1.6
            }
            mAttackCastTime: option[f32] = {
                0.28333
            }
            mAttackProbability: option[f32] = {
                1
            }
        }
        ExtraAttacks: list[embed] = {
            AttackSlotData {
                mAttackName: option[string] = {
                    "JinxBasicAttack2"
                }
            }
            AttackSlotData {}
            AttackSlotData {}
            AttackSlotData {}
            AttackSlotData {}
            AttackSlotData {
                mAttackTotalTime: option[f32] = {
                    1.6
                }
                mAttackCastTime: option[f32] = {
                    0.27
                }
                mAttackName: option[string] = {
                    "JinxQAttack2"
                }
            }
            AttackSlotData {
                mAttackTotalTime: option[f32] = {
                    1.6
                }
                mAttackCastTime: option[f32] = {
                    0.27
                }
                mAttackName: option[string] = {
                    "JinxQAttack"
                }
            }
        }
        CritAttacks: list[embed] = {
            AttackSlotData {
                mAttackName: option[string] = {
                    "JinxCritAttack"
                }
            }
            AttackSlotData {
                mAttackTotalTime: option[f32] = {
                    1.6
                }
                mAttackCastTime: option[f32] = {
                    0.27
                }
                mAttackName: option[string] = {
                    "JinxQCritAttack"
                }
            }
        }
        SpellNames: list[string] = {
            "JinxQAbility/JinxQ"
            "JinxWAbility/JinxW"
            "JinxEAbility/JinxE"
            "JinxRAbility/JinxR"
        }
        Spells: list[link] = {
            "Characters/Jinx/Spells/JinxQAbility/JinxQ"
            "Characters/Jinx/Spells/JinxWAbility/JinxW"
            "Characters/Jinx/Spells/JinxEAbility/JinxE"
            "Characters/Jinx/Spells/JinxRAbility/JinxR"
        }
        ExtraSpells: list[string] = {
            "JinxR"
            "JinxQCritAttack"
            "JinxQAttack"
            "JinxQAttack2"
            "JinxEHit"
            "BaseSpell"
            "JinxWMissile"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
        }
        0xc1984296: list[link] = {
            "Characters/Jinx/Spells/JinxRAbility/JinxR"
            "Characters/Jinx/Spells/JinxQAbility/JinxQCritAttack"
            "Characters/Jinx/Spells/JinxQAbility/JinxQAttack"
            "Characters/Jinx/Spells/JinxQAbility/JinxQAttack2"
            "Characters/Jinx/Spells/JinxEAbility/JinxEHit"
            "Shared/Spells/BaseSpell"
            "Characters/Jinx/Spells/JinxWAbility/JinxWMissile"
            "Shared/Spells/BaseSpell"
            "Shared/Spells/BaseSpell"
            "Shared/Spells/BaseSpell"
            "Shared/Spells/BaseSpell"
            "Shared/Spells/BaseSpell"
            "Shared/Spells/BaseSpell"
            "Shared/Spells/BaseSpell"
            "Shared/Spells/BaseSpell"
            "Shared/Spells/BaseSpell"
        }
        mAbilities: list[link] = {
            "Characters/Jinx/Spells/JinxPassiveMarkerAbility"
            "Characters/Jinx/Spells/JinxRAbility"
            "Characters/Jinx/Spells/JinxEAbility"
            "Characters/Jinx/Spells/JinxWAbility"
            "Characters/Jinx/Spells/JinxQAbility"
        }
        PassiveName: string = "game_character_passiveName_Jinx"
        PassiveLuaName: string = "JinxPassiveMarker"
        PassiveToolTip: string = "game_character_passiveDescription_Jinx"
        Passive1IconName: file = "assets/characters/jinx/hud/icons2d/jinx_passive.dds"
        Name: string = "game_character_displayname_Jinx"
        mUseCcAnimations: bool = true
        SelectionHeight: f32 = 155
        SelectionRadius: f32 = 120
        PathfindingCollisionRadius: f32 = 35
        0xeb74898c: option[f32] = {
            0.17
        }
        UnitTagsString: string = "Champion"
        mEducationToolData: embed = ToolEducationData {
            FirstItem: i32 = 1055
            SkillOrder: i32 = 1
        }
        mAbilitySlotCc: list[i32] = {
            0
            14
            15
            0
        }
        CharacterToolData: embed = CharacterToolData {
            MapAiPresence: map[u32,embed] = {
                0 = ToolAiPresence {
                    0xca762bfc: bool = true
                    0xb75b2ab8: bool = true
                    0xb66d0e47: bool = true
                    0x6175bb7b: bool = true
                }
                3 = ToolAiPresence {
                    0xca762bfc: bool = true
                    0xb75b2ab8: bool = true
                    0xb66d0e47: bool = true
                    0x6175bb7b: bool = true
                }
                4 = ToolAiPresence {
                    0xca762bfc: bool = true
                    0xb75b2ab8: bool = true
                    0xb66d0e47: bool = true
                    0x6175bb7b: bool = true
                }
                5 = ToolAiPresence {
                    0x6175bb7b: bool = true
                }
            }
            PassiveData: list[embed] = {
                ToolPassiveData {
                    Name: string = "game_character_passiveName_Jinx"
                }
            }
            SearchTags: string = "marksman"
            ChampionId: i32 = 222
            Roles: string = "ATTACKER"
            MagicRank: i32 = 4
            LevelSpellEffectiveness: f32 = 3
            DifficultyRank: i32 = 6
            Description: string = "game_character_description_Jinx"
            DefenseRank: i32 = 2
            ChasingAttackRangePercent: f32 = 0.8
            BotEnabled: bool = true
            BotEnabledMm: bool = true
            AttackRank: i32 = 9
        }
        PlatformEnabled: bool = true
        PurchaseIdentities: list[hash] = {
            "Ranged"
        }
        mPreferredPerkStyle: link = "Perks/Styles/Precision"
        mCharacterPassiveSpell: link = "Characters/Jinx/Spells/JinxPassiveMarkerAbility/JinxPassiveMarker"
        mCharacterPassiveBuffs: list[embed] = {
            CharacterPassiveData {
                mParentPassiveBuff: link = "Characters/Jinx/Spells/JinxPassiveMarkerAbility/JinxPassiveMarker"
            }
            CharacterPassiveData {
                mParentPassiveBuff: link = "Characters/Jinx/Spells/JinxRunCycleManager"
            }
            CharacterPassiveData {
                mParentPassiveBuff: link = 0xffc12e05
                SkinFilter: pointer = SkinFilterData {
                    SkinIds: list[u32] = {
                        60
                    }
                }
            }
            CharacterPassiveData {
                mParentPassiveBuff: link = 0xfbb1fc59
                SkinFilter: pointer = SkinFilterData {
                    SkinIds: list[u32] = {
                        60
                    }
                }
            }
        }
        0xc5c48b41: u8 = 1
    }
    "Characters/Jinx/Skins/Meta" = SkinCharacterMetaDataProperties {}
    0xadcdd464 = RecSpellRankUpInfolist {
        RecSpellRankUpInfos: list[embed] = {
            RecSpellRankUpInfo {
                MapId: u32 = 11
                Position: hash = 0x4ea76b2a
                IsDefaultRecommendation: bool = true
                mEarlyLevelOverrides: list[u32] = {
                    0
                    1
                    2
                    0
                }
            }
            RecSpellRankUpInfo {
                MapId: u32 = 12
                Position: hash = "None"
                mEarlyLevelOverrides: list[u32] = {
                    0
                    1
                    2
                    0
                }
            }
        }
    }
    0xc7008e20 = ChampionRuneRecommendationsContext {}
}
