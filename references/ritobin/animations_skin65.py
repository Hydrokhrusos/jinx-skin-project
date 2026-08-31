#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    0x6e5ceb16 = AnimationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            "Death" = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Death" = SoundEventData {
                        mSoundName: string = "Play_sfx_Jinx_Death3D_cast"
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_minigun_death.anm"
                }
            }
            "Idle1_Base" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_minigun_idle1.anm"
                }
            }
            "Idle2_Base" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_minigun_idle2.anm"
                }
            }
            0x76bbc6a0 = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_minigun_idle3.anm"
                }
            }
            "Run_Base" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Dragon_On" = ConformToPathEventData {
                        mMaskDataName: hash = 0x26a07077
                        mBlendOutTime: f32 = 0.2
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_minigun_run.anm"
                }
            }
            "Spell2" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Spell3"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = 0x4763fb3419b2797e
                }
            }
            0x34673efd = AtomicClipData {
                mFlags: u32 = 2
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Dragon_On" = ConformToPathEventData {
                        mMaskDataName: hash = 0x26a07077
                        mBlendInTime: f32 = 0.1
                        mBlendOutTime: f32 = 0.1
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_rlauncher_run.anm"
                }
            }
            "Spell3_Run" = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = 0x731cb44a
                mTrackDataName: hash = "Spell3"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_minigun_spell3_run.anm"
                }
            }
            "Spell4" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xb7a25e86 = ParticleEventData {
                        mStartFrame: f32 = 2
                        mEffectKey: hash = 0x691e95c6
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x2a5ada38
                            }
                        }
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_minigun_spell4.anm"
                }
            }
            "Channel_Wndup" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x123c95d1 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            0xed500a70
                        }
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_channel_windup.anm"
                }
            }
            "Attack1" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = 0x42395c08
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_minigun_attack1.anm"
                }
            }
            "Attack2" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = 0x42395c08
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_minigun_attack5.anm"
                }
            }
            0xa6f38079 = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = 0x16dfde88
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_rlauncher_idle1.anm"
                }
            }
            0x21237563 = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = 0x16dfde88
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_rlauncher_idle2.anm"
                }
            }
            0xcceaa86e = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = 0x16dfde88
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_rlauncher_idle3.anm"
                }
            }
            0xa7d08706 = AtomicClipData {
                mFlags: u32 = 2
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Dragon_On" = ConformToPathEventData {
                        mMaskDataName: hash = 0x26a07077
                        mBlendInTime: f32 = 0.1
                        mBlendOutTime: f32 = 0.1
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_rlauncher_run2.anm"
                }
            }
            0x66a26e91 = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = 0x3e352725
                mTrackDataName: hash = 0x42395c08
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_rlauncher_attack1.anm"
                }
            }
            0x63a269d8 = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = 0x42395c08
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_rlauncher_attack2.anm"
                }
            }
            0x01e9bb4c = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Death" = SoundEventData {
                        mSoundName: string = "Play_sfx_Jinx_Death3D_cast"
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_rlauncher_death.anm"
                }
            }
            0xbdaf4563 = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Dragon_On" = ConformToPathEventData {
                        mStartFrame: f32 = 7
                        mMaskDataName: hash = 0x26a07077
                        mBlendInTime: f32 = 0.1
                        mBlendOutTime: f32 = 0.2
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_minigun_run_in.anm"
                }
            }
            "Run" = SequencerClipData {
                mClipNameList: list[hash] = {
                    0xbdaf4563
                    "Run_Base"
                }
            }
            "IdleIn1" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Dragon_On" = ConformToPathEventData {
                        mEndFrame: f32 = 1
                        mMaskDataName: hash = 0x26a07077
                        mBlendOutTime: f32 = 0.3
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_minigun_idlein1.anm"
                }
            }
            "Idle1" = SequencerClipData {
                mFlags: u32 = 8
                mClipNameList: list[hash] = {
                    0x5d9ac533
                    "Idle1_Base"
                    "Idle1_Base"
                    "Idle1_Base"
                    0x914db254
                }
            }
            "Rlauncher_Idlein1" = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Dragon_On" = ConformToPathEventData {
                        mEndFrame: f32 = 1
                        mMaskDataName: hash = 0x26a07077
                        mBlendOutTime: f32 = 0.5
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_rlauncher_idlein1.anm"
                }
            }
            0xbb6b9d3b = SequencerClipData {
                mFlags: u32 = 2
                mClipNameList: list[hash] = {
                    "Rlauncher_Idlein1"
                    0xa6f38079
                    0xa6f38079
                    0xa6f38079
                    0x6d50d37c
                }
            }
            0x914db254 = SelectorClipData {
                mFlags: u32 = 2
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = "Idle1_Base"
                        mProbability: f32 = 90
                    }
                    SelectorPairData {
                        mClipName: hash = "Idle2_Base"
                        mProbability: f32 = 5
                    }
                    SelectorPairData {
                        mClipName: hash = 0x76bbc6a0
                        mProbability: f32 = 5
                    }
                }
            }
            0x6d50d37c = SelectorClipData {
                mFlags: u32 = 2
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = 0xa6f38079
                        mProbability: f32 = 50
                    }
                    SelectorPairData {
                        mClipName: hash = 0xcec76c2e
                        mProbability: f32 = 25
                    }
                    SelectorPairData {
                        mClipName: hash = 0xcaf10417
                        mProbability: f32 = 25
                    }
                }
            }
            0xc6d33584 = AtomicClipData {
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_rlauncher_spell4.anm"
                }
            }
            0xc4d3325e = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Spell3"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = 0x41d1132b8a2088fa
                }
            }
            "Rlauncher_Spell3" = AtomicClipData {
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_rlauncher_spell3.anm"
                }
            }
            0xf8a62a4b = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = 0x68d78255
                mTrackDataName: hash = "Spell3"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_rlauncher_spell3.anm"
                }
            }
            0xadc1b4e7 = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = 0x42395c08
                mTrackDataName: hash = 0x42395c08
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/minigun_spell1_weapon_gunonly.anm"
                }
            }
            0x1d39abef = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/minigun_spell1_weapon2.anm"
                }
            }
            "Spell1" = ParallelClipData {
                mClipNameList: list[hash] = {
                    0xadc1b4e7
                    0x1d39abef
                }
            }
            0xc3d330cb = ParallelClipData {
                mClipNameList: list[hash] = {
                    0x0fd7fa17
                    0x5316001f
                }
            }
            0x0fd7fa17 = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = 0x42395c08
                mTrackDataName: hash = 0x42395c08
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/launcher_spell1_weapon.anm"
                }
            }
            0x5316001f = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/launcher_spell1_weapon2.anm"
                }
            }
            "Attack3" = AtomicClipData {
                mTrackDataName: hash = 0x42395c08
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_minigun_attack3.anm"
                }
            }
            "Attack4" = AtomicClipData {
                mTrackDataName: hash = 0x42395c08
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_minigun_attack4.anm"
                }
            }
            "Attack5" = AtomicClipData {
                mTrackDataName: hash = 0x42395c08
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_minigun_attack2.anm"
                }
            }
            "Attack6" = AtomicClipData {
                mTrackDataName: hash = 0x42395c08
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_minigun_attack6.anm"
                }
            }
            "Dance_Loop" = AtomicClipData {
                mFlags: u32 = 2
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xa97c2af4 = SoundEventData {
                        mSoundName: string = "Play_sfx_Jinx_Dance3D_loop"
                    }
                    0x316aa066 = ParticleEventData {
                        mEffectKey: hash = 0xf1f9e076
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x42395c08
                                mTargetBoneName: hash = 0x6d229b3a
                            }
                        }
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_dance_loop.anm"
                }
            }
            "Dance_Windup" = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xbc45bbc5 = SoundEventData {
                        mSoundName: string = "Play_sfx_Jinx_Dance3D_buffactivate"
                        mIsLoop: bool = false
                    }
                    0x61f288c4 = ParticleEventData {
                        mEffectKey: hash = 0xe6629014
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x42395c08
                                mTargetBoneName: hash = 0x6d229b3a
                            }
                        }
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_dance_windup.anm"
                }
            }
            "Dance" = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Dance_Windup"
                    "Dance_Loop"
                }
            }
            0x628a47d7 = SequencerClipData {
                mFlags: u32 = 8
                mClipNameList: list[hash] = {
                    0xd003b624
                    0x34673efd
                }
            }
            0xd003b624 = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Dragon_On" = ConformToPathEventData {
                        mMaskDataName: hash = 0x26a07077
                        mBlendInTime: f32 = 0.1
                        mBlendOutTime: f32 = 0.1
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_rlauncher_run_in.anm"
                }
            }
            0x1903a210 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Launch_Start" = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mEffectKey: hash = 0x1dc9cba7
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0x07002de7 = ParticleEventData {
                        mName: hash = 0x07002de7
                        mEffectKey: hash = 0x618b1f9c
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                    "audio_recall_leadout" = SoundEventData {
                        mSoundName: string = "Play_sfx_JinxSkin65_Recall3D_buffactivate"
                        mIsLoop: bool = false
                    }
                    "cam" = FaceTargetEventData {}
                    0x3c842249 = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "Recall"
                        }
                    }
                    0x504073bd = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 28
                        mEffectKey: hash = 0x5d77ce60
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x68169a65
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0x4d406f04 = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 45
                        mEffectKey: hash = 0x6077d319
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x68169a65
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0x7c6c13d4 = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 145
                        mEffectKey: hash = 0x1b69edab
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0x7f6c188d = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 230
                        mEffectKey: hash = 0x1c69ef3e
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0x7e6c16fa = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 28
                        mEffectKey: hash = 0x5f77d186
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0x526b0558 = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 56
                        mEffectKey: hash = 0x35f82e85
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0x556b0a11 = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 94
                        mEffectKey: hash = 0x2ef82380
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0x576b0d37 = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 22
                        mEffectKey: hash = 0x34f82cf2
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0xda421f70 = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 31
                        mEffectKey: hash = 0xcb760d49
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0xdd422429 = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 78
                        mEffectKey: hash = 0xc8760890
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0xdc422296 = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 132
                        mEffectKey: hash = 0xc9760a23
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0x596b105d = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 104
                        mEffectKey: hash = 0x31f82839
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0x586b0eca = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 194
                        mEffectKey: hash = 0x3af83664
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0xb41f3ae2
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0x4c406d71 = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 6
                        mEffectKey: hash = 0x6177d4ac
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0x796c0f1b = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 194
                        mEffectKey: hash = 0x1d69f0d1
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0x786c0d88 = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 159
                        mEffectKey: hash = 0x1e69f264
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x51c2c5e8
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0x7b6c1241 = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 144
                        mEffectKey: hash = 0x1f69f3f7
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0x7a6c10ae = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 194
                        mEffectKey: hash = 0x2069f58a
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0xb31f394f
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0x3bd7509d = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 220
                        mEffectKey: hash = 0xbb1d1ab9
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0xdf42274f = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mStartFrame: f32 = 167
                        mEffectKey: hash = 0xf0ebf724
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0x691de090 = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 260
                        mFireIfAnimationEndsEarly: bool = true
                        mHideSubmeshList: list[hash] = {
                            "Recall"
                        }
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = 0xd80a012ac84bd862
                }
            }
            "Recall" = SequencerClipData {
                mFlags: u32 = 8
                mClipNameList: list[hash] = {
                    0x1903a210
                }
            }
            "Emote_Enter_Minigun" = AtomicClipData {
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_emote_enter_minigun.anm"
                }
            }
            "Emote_Enter_Rocket" = AtomicClipData {
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_emote_enter_rocket.anm"
                }
            }
            "Emote_Exit_Minigun" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_emote_exit_minigun.anm"
                }
            }
            "Emote_Exit_Rocket" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_emote_exit_rocket.anm"
                }
            }
            "Taunt_Base" = AtomicClipData {
                mMaskDataName: hash = 0xfc667fec
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xfc0eaccc = ParticleEventData {
                        mName: hash = 0xfc0eaccc
                        mEffectKey: hash = 0x228c331d
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                    "Audio_Taunt" = SoundEventData {
                        mSoundName: string = "Play_sfx_Jinx_Taunt3D_buffactivate"
                        mIsLoop: bool = false
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_joke.anm"
                }
            }
            "Taunt" = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Emote_Enter_Minigun"
                    "Taunt_Base"
                    "Emote_Exit_Minigun"
                    0x914db254
                }
            }
            0x441e6f5d = SequencerClipData {
                mFlags: u32 = 8
                mClipNameList: list[hash] = {
                    "Emote_Enter_Minigun"
                    0x909da5ab
                    "Emote_Exit_Minigun"
                    0x914db254
                }
            }
            "Respawn" = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Launcher" = JointSnapEventData {
                        mName: hash = "Launcher"
                        mStartFrame: f32 = 25
                        mJointNameToOverride: hash = 0x0672b6b2
                        mJointNameToSnapTo: hash = 0x68169a65
                    }
                    "audio_respawn" = SoundEventData {
                        mSoundName: string = "Play_sfx_Jinx_Respawn3D_buffactivate"
                        mIsLoop: bool = false
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_respawn.anm"
                }
            }
            "Recall_Winddown" = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Launcher" = JointSnapEventData {
                        mName: hash = "Launcher"
                        mStartFrame: f32 = 25
                        mJointNameToOverride: hash = 0x0672b6b2
                        mJointNameToSnapTo: hash = 0x68169a65
                    }
                    "audio_recall_winddown" = SoundEventData {
                        mSoundName: string = "Play_sfx_Jinx_Winddown3D_buffactivate"
                        mIsLoop: bool = false
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_respawn.anm"
                }
            }
            "Idlein2" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Dragon_On" = ConformToPathEventData {
                        mEndFrame: f32 = 1
                        mMaskDataName: hash = 0x26a07077
                        mBlendOutTime: f32 = 0.3
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_minigun_idlein2.anm"
                }
            }
            0x5d9ac533 = SelectorClipData {
                mFlags: u32 = 8
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = "IdleIn1"
                        mProbability: f32 = 50
                    }
                    SelectorPairData {
                        mClipName: hash = "Idlein2"
                        mProbability: f32 = 50
                    }
                }
            }
            "Run_Fast" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Dragon_On" = ConformToPathEventData {
                        mMaskDataName: hash = 0x26a07077
                        mBlendInTime: f32 = 0.1
                        mBlendOutTime: f32 = 0.2
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_minigun_run2.anm"
                }
            }
            "Laugh" = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Emote_Enter_Minigun"
                    "Laugh_In"
                    0x0488fc41
                }
            }
            0x4aacc3f2 = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Emote_Enter_Rocket"
                    "Taunt_Base"
                    "Emote_Exit_Rocket"
                    0x6d50d37c
                }
            }
            0x4df82740 = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Emote_Enter_Rocket"
                    0x909da5ab
                    "Emote_Exit_Rocket"
                    0x6d50d37c
                }
            }
            0x9d46ce26 = AtomicClipData {
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xeed2417d = SoundEventData {
                        mSoundName: string = "Play_sfx_Jinx_Joke3D_buffactivate"
                        mIsLoop: bool = false
                    }
                    0x123c95d1 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            0xed500a70
                        }
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_joke3.anm"
                }
            }
            0x267519f9 = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Emote_Enter_Rocket"
                    0x9d46ce26
                    "Emote_Exit_Rocket"
                    0x6d50d37c
                }
            }
            "Joke" = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Emote_Enter_Minigun"
                    0x9d46ce26
                    "Emote_Exit_Minigun"
                    0x914db254
                }
            }
            0x4354dad7 = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Emote_Enter_Rocket"
                    "Laugh_In"
                    0x0488fc41
                }
            }
            "Laugh_In" = AtomicClipData {
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x56eebc91 = ParticleEventData {
                        mName: hash = 0x56eebc91
                        mEffectKey: hash = 0x4b73542c
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_laugh_in.anm"
                }
            }
            "Laugh_Loop" = AtomicClipData {
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xb1e643a2 = ParticleEventData {
                        mName: hash = 0xb1e643a2
                        mEffectKey: hash = 0x785a85cd
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                }
                mTickDuration: f32 = 0.028570998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_laugh_loop.anm"
                }
            }
            "Channel" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x123c95d1 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            0xed500a70
                        }
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_channel.anm"
                }
            }
            0x909da5ab = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x87566c32 = ParticleEventData {
                        mName: hash = 0x87566c32
                        mEffectKey: hash = 0x703192a1
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                    0xf44d7fb4 = SoundEventData {
                        mSoundName: string = "Play_sfx_Jinx_Taunt23D_buffactivate"
                        mIsLoop: bool = false
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_taunt2.anm"
                }
            }
            0xc5d333f1 = AtomicClipData {
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Spell3"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_rlauncher_spell3.anm"
                }
            }
            "Spell3" = AtomicClipData {
                mTrackDataName: hash = "Spell3"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_minigun_spell3.anm"
                }
            }
            "Stunned" = AtomicClipData {
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_stunned.anm"
                }
            }
            "Laugh_Breath" = AtomicClipData {
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.039999995
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_laugh_breath.anm"
                }
            }
            0x0488fc41 = SequencerClipData {
                mFlags: u32 = 2
                mClipNameList: list[hash] = {
                    "Laugh_Loop"
                    "Laugh_Loop"
                    "Laugh_Loop"
                    "Laugh_Breath"
                }
            }
            "Run_Haste" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Dragon_On" = ConformToPathEventData {
                        mMaskDataName: hash = 0x26a07077
                        mBlendInTime: f32 = 0.1
                        mBlendOutTime: f32 = 0.2
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_minigun_runhaste.anm"
                }
            }
            0x5a527c0b = AtomicClipData {
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Dragon_On" = ConformToPathEventData {
                        mMaskDataName: hash = 0x26a07077
                        mBlendInTime: f32 = 0.1
                        mBlendOutTime: f32 = 0.1
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_rlauncher_runhaste.anm"
                }
            }
            0xcec76c2e = SequencerClipData {
                mFlags: u32 = 8
                mClipNameList: list[hash] = {
                    0x21237563
                    0xa6f38079
                    0xa6f38079
                    0xa6f38079
                    0xa6f38079
                }
            }
            0xcaf10417 = SequencerClipData {
                mClipNameList: list[hash] = {
                    0xcceaa86e
                    0xa6f38079
                    0xa6f38079
                    0xa6f38079
                    0xa6f38079
                }
            }
            0x5f2e0306 = SequencerClipData {
                mFlags: u32 = 8
                mClipNameList: list[hash] = {
                    0xfb7159de
                    0x7715e3e6
                }
            }
            0x7715e3e6 = AtomicClipData {
                mFlags: u32 = 2
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Launch_Start" = ParticleEventData {
                        mName: hash = "Launch_Start"
                        mEffectKey: hash = 0x1dc9cba7
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x2a5ada38
                            }
                        }
                        mIsLoop: bool = false
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_rlauncher_drecall.anm"
                }
            }
            0xfb7159de = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xa3aec9fc = ParticleEventData {
                        mName: hash = 0xa3aec9fc
                        mStartFrame: f32 = 45
                        mEffectKey: hash = 0x0a9f806c
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x2a5ada38
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0xa6aeceb5 = ParticleEventData {
                        mName: hash = 0xa6aeceb5
                        mStartFrame: f32 = 50
                        mEffectKey: hash = 0x0a9f806c
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x2a5ada38
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0xa5aecd22 = ParticleEventData {
                        mName: hash = 0xa5aecd22
                        mStartFrame: f32 = 67
                        mEffectKey: hash = 0x0a9f806c
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x2a5ada38
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0xa0aec543 = ParticleEventData {
                        mName: hash = 0xa0aec543
                        mStartFrame: f32 = 80
                        mEffectKey: hash = 0x0a9f806c
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x2a5ada38
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0x9faec3b0 = ParticleEventData {
                        mName: hash = 0x9faec3b0
                        mStartFrame: f32 = 25
                        mEffectKey: hash = 0x0a9f806c
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x2a5ada38
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_rlauncher_drecall_in.anm"
                }
            }
            0x9028089f = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Recall" = ParticleEventData {
                        mName: hash = "Recall"
                        mEffectKey: hash = 0xb20facf0
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x2a5ada38
                            }
                        }
                        mIsLoop: bool = false
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_rlauncher_drecall_out.anm"
                }
            }
            0x998c286c = SequencerClipData {
                mFlags: u32 = 8
                mClipNameList: list[hash] = {
                    "Emote_Enter_Minigun"
                    0x95ba6117
                    "Emote_Exit_Minigun"
                    0x914db254
                }
            }
            0x95ba6117 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x7388cbb9 = ParticleEventData {
                        mName: hash = 0x7388cbb9
                        mEffectKey: hash = 0xb4a61f18
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                    0xf44d7fb4 = SoundEventData {
                        mSoundName: string = "Play_sfx_Jinx_Taunt23D_buffactivate"
                        mIsLoop: bool = false
                    }
                }
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_taunt2.anm"
                }
            }
            "Rlauncher_Death" = AtomicClipData {
                mMaskDataName: hash = 0x123c95d1
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.033333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_rlauncher_death.anm"
                }
            }
            0x622bd465 = AtomicClipData {
                mFlags: u32 = 6
                mMaskDataName: hash = "WeaponBuffbone"
                mTrackDataName: hash = 0x0092b9c4
                mEventDataMap: map[hash,pointer] = {
                    0x0092b9c4 = JointSnapEventData {
                        mName: hash = 0x0092b9c4
                        mJointNameToOverride: hash = 0x7976b31b
                        mJointNameToSnapTo: hash = 0x2a5ada38
                    }
                }
                mTickDuration: f32 = 1
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_buffbone_swap.anm"
                }
            }
            0x2ec639bb = AtomicClipData {
                mFlags: u32 = 6
                mMaskDataName: hash = "WeaponBuffbone"
                mTrackDataName: hash = 0x0092b9c4
                mEventDataMap: map[hash,pointer] = {
                    0x0092b9c4 = JointSnapEventData {
                        mName: hash = 0x0092b9c4
                        mJointNameToOverride: hash = 0x7976b31b
                        mJointNameToSnapTo: hash = 0x3f4b5a02
                    }
                }
                mTickDuration: f32 = 1
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/characters/jinx/skins/base/animations/jinx_buffbone_swap.anm"
                }
            }
            0xaabc447a = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Emote_Enter_Rocket"
                    0x95ba6117
                    "Emote_Exit_Rocket"
                    0x6d50d37c
                }
            }
            0x0356ec6e = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Emote_Enter_Rocket"
                    0x909da5ab
                    "Emote_Exit_Rocket"
                    0x6d50d37c
                }
            }
        }
        mMaskDataMap: map[hash,embed] = {
            0x42395c08 = MaskData {
                mWeightList: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    0
                    0
                    0
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
            0x731cb44a = MaskData {
                mId: u32 = 1
                mWeightList: list[f32] = {
                    0
                    0.5
                    0.5
                    0.5
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
            0x68d78255 = MaskData {
                mId: u32 = 2
                mWeightList: list[f32] = {
                    0
                    0.5
                    0.5
                    0.5
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
            "WeaponBuffbone" = MaskData {
                mId: u32 = 3
                mWeightList: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
            0x26a07077 = MaskData {
                mWeightList: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0.5
                    0.59999996
                    0.75
                    0.65
                    0.84999996
                    1
                    0.5
                    0.59999996
                    0.75
                    0.65
                    0.84999996
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
            0xef7cfc3b = MaskData {
                mWeightList: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
            0x3e352725 = MaskData {
                mWeightList: list[f32] = {
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    0.34
                    1
                    0.47
                    1
                    1
                    1
                    1
                    1
                    1
                    0.47
                    0.47
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    0
                    0
                    0
                    1
                    1
                    1
                    1
                    1
                }
            }
            0x123c95d1 = MaskData {
                mWeightList: list[f32] = {
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0.58
                    1
                    1
                    1
                    1
                    1
                    1
                    0.58
                    0.58
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                }
            }
            0xfc667fec = MaskData {
                mWeightList: list[f32] = {
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0.86
                    1
                    1
                    1
                    1
                    1
                    1
                    0.86
                    0.86
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                }
            }
            0x16dfde88 = MaskData {
                mWeightList: list[f32] = {
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0.41
                    1
                    1
                    1
                    1
                    1
                    1
                    0.41
                    0.41
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                }
            }
        }
        mTrackDataMap: map[hash,embed] = {
            0x0092b9c4 = TrackData {}
            "Spell3" = TrackData {
                mPriority: u8 = 1
            }
            0x42395c08 = TrackData {
                mPriority: u8 = 2
            }
            "Default" = TrackData {
                mPriority: u8 = 3
            }
        }
        mBlendDataTable: map[u64,pointer] = {
            137847198735514444 = TimeBlendData {
                mTime: f32 = 0
            }
            137847201876983117 = TimeBlendData {
                mTime: f32 = 0
            }
            137847202875058763 = TimeBlendData {
                mTime: f32 = 0
            }
            225378344485565545 = TimeBlendData {
                mTime: f32 = 0
            }
            225378347606654285 = TimeBlendData {
                mTime: f32 = 0
            }
            225378348604729931 = TimeBlendData {
                mTime: f32 = 0
            }
            240639590475021645 = TimeBlendData {
                mTime: f32 = 0
            }
            326788332260998477 = TimeBlendData {
                mTime: f32 = 0
            }
            396460210618663542 = TimeBlendData {
                mTime: f32 = 0
            }
            396460213699919181 = TimeBlendData {
                mTime: f32 = 0
            }
            396460214697994827 = TimeBlendData {
                mTime: f32 = 0
            }
            897461252391201857 = TimeBlendData {
                mTime: f32 = 0
            }
            897461255355809101 = TimeBlendData {
                mTime: f32 = 0
            }
            897461256353884747 = TimeBlendData {
                mTime: f32 = 0
            }
            1141656007518714391 = TimeBlendData {
                mTime: f32 = 0
            }
            1141656010426465613 = TimeBlendData {
                mTime: f32 = 0
            }
            1141656011424541259 = TimeBlendData {
                mTime: f32 = 0
            }
            1802462465901175312 = TimeBlendData {
                mTime: f32 = 0
            }
            1802462468655070541 = TimeBlendData {
                mTime: f32 = 0
            }
            1802462469653146187 = TimeBlendData {
                mTime: f32 = 0
            }
            2105903344248269807 = TimeBlendData {
                mTime: f32 = 0
            }
            2105903346931514701 = TimeBlendData {
                mTime: f32 = 0
            }
            2105903347929590347 = TimeBlendData {
                mTime: f32 = 0
            }
            2291038459341268823 = TimeBlendData {
                mTime: f32 = 0
            }
            2291038461981408589 = TimeBlendData {
                mTime: f32 = 0
            }
            2291038462979484235 = TimeBlendData {
                mTime: f32 = 0
            }
            2387881296054678883 = TimeBlendData {
                mTime: f32 = 0
            }
            2387881298672270669 = TimeBlendData {
                mTime: f32 = 0
            }
            2387881299670346315 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597613627986596 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597616235167053 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597617233242699 = TimeBlendData {
                mTime: f32 = 0
            }
            2771149703599167993 = TimeBlendData {
                mTime: f32 = 0
            }
            2771149706127523149 = TimeBlendData {
                mTime: f32 = 0
            }
            2786235697150344525 = TimeBlendData {
                mTime: f32 = 0
            }
            3084207950027116234 = TimeBlendData {
                mTime: f32 = 0
            }
            3084207952482581837 = TimeBlendData {
                mTime: f32 = 0
            }
            3370444847239805371 = TimeBlendData {
                mTime: f32 = 0
            }
            3370444849628626253 = TimeBlendData {
                mTime: f32 = 0
            }
            3776056069800279805 = TimeBlendData {
                mTime: f32 = 0
            }
            3776056072094661965 = TimeBlendData {
                mTime: f32 = 0
            }
            3776056073092737611 = TimeBlendData {
                mTime: f32 = 0
            }
            3943776447673974093 = TimeBlendData {
                mTime: f32 = 0
            }
            4110781524298460676 = TimeBlendData {
                mTime: f32 = 0
            }
            4110781526514908493 = TimeBlendData {
                mTime: f32 = 0
            }
            4110781527512984139 = TimeBlendData {
                mTime: f32 = 0
            }
            4851743316667325143 = TimeBlendData {
                mTime: f32 = 0
            }
            4851743318711254349 = TimeBlendData {
                mTime: f32 = 0
            }
            4908483090245906269 = TimeBlendData {
                mTime: f32 = 0
            }
            4908483092276624717 = TimeBlendData {
                mTime: f32 = 0
            }
            5380891100203238386 = TimeBlendData {
                mTime: f32 = 0
            }
            5380891102123965773 = TimeBlendData {
                mTime: f32 = 0
            }
            5618283692284192576 = TimeBlendData {
                mTime: f32 = 0
            }
            5618283694149647693 = TimeBlendData {
                mTime: f32 = 0
            }
            5958793200716079832 = TimeBlendData {
                mTime: f32 = 0
            }
            5958793202502253901 = TimeBlendData {
                mTime: f32 = 0
            }
            5958793203500329547 = TimeBlendData {
                mTime: f32 = 0
            }
            5986972889173590047 = TimeBlendData {
                mTime: f32 = 0
            }
            5986972890953203021 = TimeBlendData {
                mTime: f32 = 0
            }
            5986972891951278667 = TimeBlendData {
                mTime: f32 = 0
            }
            6030852525642605675 = TimeBlendData {
                mTime: f32 = 0
            }
            6030852527412002125 = TimeBlendData {
                mTime: f32 = 0
            }
            6030852528410077771 = TimeBlendData {
                mTime: f32 = 0
            }
            6174971175495657361 = TimeBlendData {
                mTime: f32 = 0
            }
            6174971177231498573 = TimeBlendData {
                mTime: f32 = 0
            }
            6174971178229574219 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030500422183204 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030502141246797 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030503118004900 = TimeBlendData {
                mTime: f32 = 5
            }
            6247030503139322443 = TimeBlendData {
                mTime: f32 = 0
            }
            6391149150275234890 = TimeBlendData {
                mTime: f32 = 0
            }
            6391149151960743245 = TimeBlendData {
                mTime: f32 = 0
            }
            6391149152937501348 = TimeBlendData {
                mTime: f32 = 5
            }
            6391149152958818891 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208475201760733 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208476870491469 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208477847249572 = TimeBlendData {
                mTime: f32 = 5
            }
            6463208477868567115 = TimeBlendData {
                mTime: f32 = 0
            }
            6508400801363836237 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702300539534768 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702302194646349 = TimeBlendData {
                mTime: f32 = 0
            }
            6700548058796335349 = TimeBlendData {
                mTime: f32 = 0
            }
            6700548060409806157 = TimeBlendData {
                mTime: f32 = 0
            }
            6700548061407881803 = TimeBlendData {
                mTime: f32 = 0
            }
            6744920216345167155 = TimeBlendData {
                mTime: f32 = 0
            }
            6744920217948306765 = TimeBlendData {
                mTime: f32 = 0
            }
            6750317598668091927 = TimeBlendData {
                mTime: f32 = 0
            }
            6750317600269974861 = TimeBlendData {
                mTime: f32 = 0
            }
            6750317601268050507 = TimeBlendData {
                mTime: f32 = 0
            }
            6858422610010094925 = TimeBlendData {
                mTime: f32 = 0
            }
            7073981171619320933 = TimeBlendData {
                mTime: f32 = 0
            }
            7073981173145845069 = TimeBlendData {
                mTime: f32 = 0
            }
            7100566752899778519 = TimeBlendData {
                mTime: f32 = 0
            }
            7100566754420112717 = TimeBlendData {
                mTime: f32 = 0
            }
            7179417134087432664 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135589408077 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417136587483723 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108867010193 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595110318652749 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595111316728395 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7469273466100301133 = TimeBlendData {
                mTime: f32 = 0
            }
            7794375147286900454 = TimeBlendData {
                mTime: f32 = 0
            }
            7794375148645694797 = TimeBlendData {
                mTime: f32 = 0
            }
            7794375149643770443 = TimeBlendData {
                mTime: f32 = 0
            }
            7877028279634416508 = TimeBlendData {
                mTime: f32 = 0
            }
            7877028280973966669 = TimeBlendData {
                mTime: f32 = 0
            }
            8555650309609473696 = TimeBlendData {
                mTime: f32 = 0
            }
            8555650310791019853 = TimeBlendData {
                mTime: f32 = 0
            }
            8555650311789095499 = TimeBlendData {
                mTime: f32 = 0
            }
            8581015245179895117 = TimeBlendData {
                mTime: f32 = 0
            }
            10387562022696435021 = TimeBlendData {
                mTime: f32 = 0
            }
            10420667269089437099 = TimeBlendData {
                mTime: f32 = 0
            }
            10420667269836750157 = TimeBlendData {
                mTime: f32 = 0
            }
            10420667270834825803 = TimeBlendData {
                mTime: f32 = 0
            }
            10470220784991056468 = TimeBlendData {
                mTime: f32 = 0
            }
            10470220785726831949 = TimeBlendData {
                mTime: f32 = 0
            }
            10789042611905150285 = TimeBlendData {
                mTime: f32 = 0
            }
            10998256077507766177 = TimeBlendData {
                mTime: f32 = 0
            }
            10998256078120598861 = TimeBlendData {
                mTime: f32 = 0
            }
            10998256079118674507 = TimeBlendData {
                mTime: f32 = 0
            }
            11064262832037608781 = TimeBlendData {
                mTime: f32 = 0
            }
            11332972177567174182 = TimeBlendData {
                mTime: f32 = 0
            }
            11332972178102074701 = TimeBlendData {
                mTime: f32 = 0
            }
            11332972179100150347 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364254877113350 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364255402376525 = TimeBlendData {
                mTime: f32 = 0
            }
            11490697227982547007 = TimeBlendData {
                mTime: f32 = 0
            }
            11490697228480724301 = TimeBlendData {
                mTime: f32 = 0
            }
            11490697228489540963 = TimeBlendData {
                mTime: f32 = 0
            }
            11490697228797064740 = TimeBlendData {
                mTime: f32 = 0
            }
            11490697229478799947 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733634412495629 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733634831269197 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733635829344843 = TimeBlendData {
                mTime: f32 = 0
            }
            12030100289617100921 = TimeBlendData {
                mTime: f32 = 0
            }
            12030100289989688653 = TimeBlendData {
                mTime: f32 = 0
            }
            12030100290987764299 = TimeBlendData {
                mTime: f32 = 0
            }
            12030939629306149849 = TimeBlendData {
                mTime: f32 = 0
            }
            12030939629678542157 = TimeBlendData {
                mTime: f32 = 0
            }
            12030939630676617803 = TimeBlendData {
                mTime: f32 = 0
            }
            12092313462144796422 = TimeBlendData {
                mTime: f32 = 0
            }
            12092313462502899021 = TimeBlendData {
                mTime: f32 = 0
            }
            12092313463500974667 = TimeBlendData {
                mTime: f32 = 0
            }
            12153837983911058240 = TimeBlendData {
                mTime: f32 = 0
            }
            12153837984254836045 = TimeBlendData {
                mTime: f32 = 0
            }
            12153837985252911691 = TimeBlendData {
                mTime: f32 = 0
            }
            12167572168340399723 = TimeBlendData {
                mTime: f32 = 0
            }
            12167572168680979789 = TimeBlendData {
                mTime: f32 = 0
            }
            12167572168689796451 = TimeBlendData {
                mTime: f32 = 0
            }
            12167572168997320228 = TimeBlendData {
                mTime: f32 = 0
            }
            12167572169679055435 = TimeBlendData {
                mTime: f32 = 0
            }
            12302783576019615053 = TimeBlendData {
                mTime: f32 = 0
            }
            12520487346212287719 = TimeBlendData {
                mTime: f32 = 0
            }
            12520487346470698317 = TimeBlendData {
                mTime: f32 = 0
            }
            12520487347468773963 = TimeBlendData {
                mTime: f32 = 0
            }
            12895556605352228968 = TimeBlendData {
                mTime: f32 = 0
            }
            12895556605523311949 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675255205280654 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675255342808397 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675256340884043 = TimeBlendData {
                mTime: f32 = 0
            }
            13111734580131806497 = TimeBlendData {
                mTime: f32 = 0
            }
            13111734580252556621 = TimeBlendData {
                mTime: f32 = 0
            }
            13111734581250632267 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647005911895230 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647006022188365 = TimeBlendData {
                mTime: f32 = 0
            }
            13255853229984858183 = TimeBlendData {
                mTime: f32 = 0
            }
            13255853230072053069 = TimeBlendData {
                mTime: f32 = 0
            }
            13255853231070128715 = TimeBlendData {
                mTime: f32 = 0
            }
            13279411344652235330 = TimeBlendData {
                mTime: f32 = 0
            }
            13279411344733945165 = TimeBlendData {
                mTime: f32 = 0
            }
            13279411345732020811 = TimeBlendData {
                mTime: f32 = 0
            }
            13505060787473587515 = TimeBlendData {
                mTime: f32 = 0
            }
            13505060787502759245 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883339398317155 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883339407506765 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413820501325 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352414818576971 = TimeBlendData {
                mTime: f32 = 0
            }
            13668219688770387277 = TimeBlendData {
                mTime: f32 = 0
            }
            13668219688779203939 = TimeBlendData {
                mTime: f32 = 0
            }
            13668219689768462923 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674971085258061 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674971168453702 = TimeBlendData {
                mTime: f32 = 0
            }
            14110675709091953997 = TimeBlendData {
                mTime: f32 = 0
            }
            14110675709203787979 = TimeBlendData {
                mTime: f32 = 0
            }
            14182735034001702221 = TimeBlendData {
                mTime: f32 = 0
            }
            14182735034130313822 = TimeBlendData {
                mTime: f32 = 0
            }
            14182735034999777867 = TimeBlendData {
                mTime: f32 = 0
            }
            14254794358911450445 = TimeBlendData {
                mTime: f32 = 0
            }
            14254794359056839665 = TimeBlendData {
                mTime: f32 = 0
            }
            14254794359909526091 = TimeBlendData {
                mTime: f32 = 0
            }
            14326853683821198669 = TimeBlendData {
                mTime: f32 = 0
            }
            14326853683983365508 = TimeBlendData {
                mTime: f32 = 0
            }
            14326853684819274315 = TimeBlendData {
                mTime: f32 = 0
            }
            14602606879330319693 = TimeBlendData {
                mTime: f32 = 0
            }
            14602606879556690326 = TimeBlendData {
                mTime: f32 = 0
            }
            14602606880328395339 = TimeBlendData {
                mTime: f32 = 0
            }
            14623473965053033805 = TimeBlendData {
                mTime: f32 = 0
            }
            14765799521861025101 = TimeBlendData {
                mTime: f32 = 0
            }
            14765799522125391982 = TimeBlendData {
                mTime: f32 = 0
            }
            14765799522859100747 = TimeBlendData {
                mTime: f32 = 0
            }
            14899996840176434509 = TimeBlendData {
                mTime: f32 = 0
            }
            14989024253727784269 = TimeBlendData {
                mTime: f32 = 0
            }
            14989024254725859915 = TimeBlendData {
                mTime: f32 = 0
            }
            16132709916495887693 = TimeBlendData {
                mTime: f32 = 0
            }
            16132709917078513201 = TimeBlendData {
                mTime: f32 = 0
            }
            16132709917493963339 = TimeBlendData {
                mTime: f32 = 0
            }
            16887049737250323789 = TimeBlendData {
                mTime: f32 = 0
            }
            16887049738008582723 = TimeBlendData {
                mTime: f32 = 0
            }
            16887049738248399435 = TimeBlendData {
                mTime: f32 = 0
            }
            16914982941823122765 = TimeBlendData {
                mTime: f32 = 0
            }
            16959109062160072013 = TimeBlendData {
                mTime: f32 = 0
            }
            16959109062935108566 = TimeBlendData {
                mTime: f32 = 0
            }
            16959109063158147659 = TimeBlendData {
                mTime: f32 = 0
            }
            17371216860747971917 = TimeBlendData {
                mTime: f32 = 0
            }
            17371216861618959794 = TimeBlendData {
                mTime: f32 = 0
            }
            17371216861746047563 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496519167032140 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496519187412073 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496519227245174 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496519343893569 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496519400749591 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496519554605584 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496519625255919 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496519668361047 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496519690909027 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496519701320356 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496520014118653 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496520092052996 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496520522326744 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496520528887839 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496520539104363 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496520572659601 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496520589437220 = TimeBlendData {
                mTime: f32 = 5
            }
            17825496520622992458 = TimeBlendData {
                mTime: f32 = 5
            }
            17825496520639770077 = TimeBlendData {
                mTime: f32 = 5
            }
            17825496520695030005 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496520706617879 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496520806525400 = TimeBlendData {
                mTime: f32 = 0.1
            }
            17825496520856858257 = TimeBlendData {
                mTime: f32 = 0.1
            }
            17825496520949706470 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496521126954656 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496521561187755 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496521695668129 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496521773600294 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496521810323519 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496521889727245 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496521935913081 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496521936108505 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496521950398214 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496521964723008 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496521967920747 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496522050090215 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496522170973070 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496522187750689 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496522221305927 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496522226790978 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496522308500813 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496522317317475 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496522437112414 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496522453890033 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496522470667652 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496522534871446 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496522572867694 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496522624841252 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496522891126321 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496523066759747 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496523083537366 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496523179488690 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496523285258916 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496523306576459 = TimeBlendData {
                mTime: f32 = 0
            }
            17876238949570624845 = TimeBlendData {
                mTime: f32 = 0
            }
            17876238950559197340 = TimeBlendData {
                mTime: f32 = 0
            }
            17917054672324574541 = TimeBlendData {
                mTime: f32 = 0
            }
            17917054673322650187 = TimeBlendData {
                mTime: f32 = 0
            }
            18118361589079391565 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030500689604241 = TimeBlendData {
                mTime: f32 = 0.1
            }
            6247030500639271384 = TimeBlendData {
                mTime: f32 = 0.1
            }
            6463208475418848913 = TimeBlendData {
                mTime: f32 = 0.1
            }
            6463208475368516056 = TimeBlendData {
                mTime: f32 = 0.1
            }
            6391149150509100689 = TimeBlendData {
                mTime: f32 = 0.1
            }
            6391149150458767832 = TimeBlendData {
                mTime: f32 = 0.1
            }
            6030852525960359569 = TimeBlendData {
                mTime: f32 = 0.1
            }
            6030852525910026712 = TimeBlendData {
                mTime: f32 = 0.1
            }
            5958793201050611345 = TimeBlendData {
                mTime: f32 = 0.1
            }
            5958793201000278488 = TimeBlendData {
                mTime: f32 = 0.1
            }
            6174971175779856017 = TimeBlendData {
                mTime: f32 = 0.1
            }
            6174971175729523160 = TimeBlendData {
                mTime: f32 = 0.1
            }
            2432597614783524497 = TimeBlendData {
                mTime: f32 = 0.1
            }
            2432597614733191640 = TimeBlendData {
                mTime: f32 = 0.1
            }
            11831733633379626641 = TimeBlendData {
                mTime: f32 = 0.1
            }
            11831733633329293784 = TimeBlendData {
                mTime: f32 = 0.1
            }
            2291038460529766033 = TimeBlendData {
                mTime: f32 = 0.1
            }
            2291038460479433176 = TimeBlendData {
                mTime: f32 = 0.1
            }
            14602606877878677137 = TimeBlendData {
                mTime: f32 = 0.1
            }
            14602606877828344280 = TimeBlendData {
                mTime: f32 = 0.1
            }
            13630352412368858769 = TimeBlendData {
                mTime: f32 = 0.1
            }
            13630352412318525912 = TimeBlendData {
                mTime: f32 = 0.1
            }
            8581015243728252561 = TimeBlendData {
                mTime: f32 = 0.1
            }
            8581015243677919704 = TimeBlendData {
                mTime: f32 = 0.1
            }
            18118361587627749009 = TimeBlendData {
                mTime: f32 = 0.1
            }
            18118361587577416152 = TimeBlendData {
                mTime: f32 = 0.1
            }
            10387562021244792465 = TimeBlendData {
                mTime: f32 = 0.1
            }
            10387562021194459608 = TimeBlendData {
                mTime: f32 = 0.1
            }
            13279411343282302609 = TimeBlendData {
                mTime: f32 = 0.1
            }
            13279411343231969752 = TimeBlendData {
                mTime: f32 = 0.1
            }
            6750317598818332305 = TimeBlendData {
                mTime: f32 = 0.1
            }
            6750317598767999448 = TimeBlendData {
                mTime: f32 = 0.1
            }
            4110781525063265937 = TimeBlendData {
                mTime: f32 = 0.1
            }
            4110781525012933080 = TimeBlendData {
                mTime: f32 = 0.1
            }
            225378346155011729 = TimeBlendData {
                mTime: f32 = 0.1
            }
            225378346104678872 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7794375147194052241 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7794375147143719384 = TimeBlendData {
                mTime: f32 = 0.1
            }
            16132709915044245137 = TimeBlendData {
                mTime: f32 = 0.1
            }
            16132709914993912280 = TimeBlendData {
                mTime: f32 = 0.1
            }
            8555650309339377297 = TimeBlendData {
                mTime: f32 = 0.1
            }
            8555650309289044440 = TimeBlendData {
                mTime: f32 = 0.1
            }
            10470220784275189393 = TimeBlendData {
                mTime: f32 = 0.1
            }
            10470220784224856536 = TimeBlendData {
                mTime: f32 = 0.1
            }
            16887049735798681233 = TimeBlendData {
                mTime: f32 = 0.1
            }
            16887049735748348376 = TimeBlendData {
                mTime: f32 = 0.1
            }
            16959109060708429457 = TimeBlendData {
                mTime: f32 = 0.1
            }
            16959109060658096600 = TimeBlendData {
                mTime: f32 = 0.1
            }
            6744920216496664209 = TimeBlendData {
                mTime: f32 = 0.1
            }
            6744920216446331352 = TimeBlendData {
                mTime: f32 = 0.1
            }
            11332972176650432145 = TimeBlendData {
                mTime: f32 = 0.1
            }
            11332972176600099288 = TimeBlendData {
                mTime: f32 = 0.1
            }
            16914982940371480209 = TimeBlendData {
                mTime: f32 = 0.1
            }
            16914982940321147352 = TimeBlendData {
                mTime: f32 = 0.1
            }
            12153837982803193489 = TimeBlendData {
                mTime: f32 = 0.1
            }
            12153837982752860632 = TimeBlendData {
                mTime: f32 = 0.1
            }
            10998256076668956305 = TimeBlendData {
                mTime: f32 = 0.1
            }
            10998256076618623448 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7073981171694202513 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7073981171643869656 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108816677336 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417134137765521 = TimeBlendData {
                mTime: f32 = 0.1
            }
            137847200425340561 = TimeBlendData {
                mTime: f32 = 0.1
            }
            12030100288538046097 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7877028279522324113 = TimeBlendData {
                mTime: f32 = 0.1
            }
            2387881297220628113 = TimeBlendData {
                mTime: f32 = 0.1
            }
            14765799520409382545 = TimeBlendData {
                mTime: f32 = 0.1
            }
            3776056070643019409 = TimeBlendData {
                mTime: f32 = 0.1
            }
            12092313461051256465 = TimeBlendData {
                mTime: f32 = 0.1
            }
            6508400799912193681 = TimeBlendData {
                mTime: f32 = 0.1
            }
            14989024252276141713 = TimeBlendData {
                mTime: f32 = 0.1
            }
            14182735032550059665 = TimeBlendData {
                mTime: f32 = 0.1
            }
            14254794357459807889 = TimeBlendData {
                mTime: f32 = 0.1
            }
            17917054670872931985 = TimeBlendData {
                mTime: f32 = 0.1
            }
            14326853682369556113 = TimeBlendData {
                mTime: f32 = 0.1
            }
            1802462467203427985 = TimeBlendData {
                mTime: f32 = 0.1
            }
            12167572167229337233 = TimeBlendData {
                mTime: f32 = 0.1
            }
            11490697227029081745 = TimeBlendData {
                mTime: f32 = 0.1
            }
            3943776446222331537 = TimeBlendData {
                mTime: f32 = 0.1
            }
            396460212248276625 = TimeBlendData {
                mTime: f32 = 0.1
            }
            6700548058958163601 = TimeBlendData {
                mTime: f32 = 0.1
            }
            3370444848176983697 = TimeBlendData {
                mTime: f32 = 0.1
            }
            17371216859296329361 = TimeBlendData {
                mTime: f32 = 0.1
            }
            12030939628226899601 = TimeBlendData {
                mTime: f32 = 0.1
            }
            2786235695698701969 = TimeBlendData {
                mTime: f32 = 0.1
            }
            13668219687318744721 = TimeBlendData {
                mTime: f32 = 0.1
            }
            5986972889501560465 = TimeBlendData {
                mTime: f32 = 0.1
            }
            1141656008974823057 = TimeBlendData {
                mTime: f32 = 0.1
            }
            2105903345479872145 = TimeBlendData {
                mTime: f32 = 0.1
            }
            12520487345019055761 = TimeBlendData {
                mTime: f32 = 0.1
            }
            13111734578800914065 = TimeBlendData {
                mTime: f32 = 0.1
            }
            13039675253891165841 = TimeBlendData {
                mTime: f32 = 0.1
            }
            137847200375007704 = TimeBlendData {
                mTime: f32 = 0.1
            }
            12030100288487713240 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7877028279471991256 = TimeBlendData {
                mTime: f32 = 0.1
            }
            2387881297170295256 = TimeBlendData {
                mTime: f32 = 0.1
            }
            14765799520359049688 = TimeBlendData {
                mTime: f32 = 0.1
            }
            3776056070592686552 = TimeBlendData {
                mTime: f32 = 0.1
            }
            12092313461000923608 = TimeBlendData {
                mTime: f32 = 0.1
            }
            6508400799861860824 = TimeBlendData {
                mTime: f32 = 0.1
            }
            14989024252225808856 = TimeBlendData {
                mTime: f32 = 0.1
            }
            14182735032499726808 = TimeBlendData {
                mTime: f32 = 0.1
            }
            14254794357409475032 = TimeBlendData {
                mTime: f32 = 0.1
            }
            17917054670822599128 = TimeBlendData {
                mTime: f32 = 0.1
            }
            14326853682319223256 = TimeBlendData {
                mTime: f32 = 0.1
            }
            1802462467153095128 = TimeBlendData {
                mTime: f32 = 0.1
            }
            12167572167179004376 = TimeBlendData {
                mTime: f32 = 0.1
            }
            11490697226978748888 = TimeBlendData {
                mTime: f32 = 0.1
            }
            3943776446171998680 = TimeBlendData {
                mTime: f32 = 0.1
            }
            396460212197943768 = TimeBlendData {
                mTime: f32 = 0.1
            }
            6700548058907830744 = TimeBlendData {
                mTime: f32 = 0.1
            }
            3370444848126650840 = TimeBlendData {
                mTime: f32 = 0.1
            }
            17371216859245996504 = TimeBlendData {
                mTime: f32 = 0.1
            }
            12030939628176566744 = TimeBlendData {
                mTime: f32 = 0.1
            }
            2786235695648369112 = TimeBlendData {
                mTime: f32 = 0.1
            }
            13668219687268411864 = TimeBlendData {
                mTime: f32 = 0.1
            }
            5986972889451227608 = TimeBlendData {
                mTime: f32 = 0.1
            }
            1141656008924490200 = TimeBlendData {
                mTime: f32 = 0.1
            }
            2105903345429539288 = TimeBlendData {
                mTime: f32 = 0.1
            }
            12520487344968722904 = TimeBlendData {
                mTime: f32 = 0.1
            }
            13111734578750581208 = TimeBlendData {
                mTime: f32 = 0.1
            }
            13039675253840832984 = TimeBlendData {
                mTime: f32 = 0.1
            }
            13255853228620410513 = TimeBlendData {
                mTime: f32 = 0.1
            }
            13255853228570077656 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7469273464648658577 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7469273464598325720 = TimeBlendData {
                mTime: f32 = 0.1
            }
            897461253904166545 = TimeBlendData {
                mTime: f32 = 0.1
            }
            897461253853833688 = TimeBlendData {
                mTime: f32 = 0.1
            }
            10789042610453507729 = TimeBlendData {
                mTime: f32 = 0.1
            }
            10789042610403174872 = TimeBlendData {
                mTime: f32 = 0.1
            }
            10420667268385107601 = TimeBlendData {
                mTime: f32 = 0.1
            }
            10420667268334774744 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595107145089024 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108599589156 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108649922013 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108633144394 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108549256299 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108532478680 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108582811537 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595107711472292 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595109899879181 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595107678512983 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595110545023382 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417132415844352 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417133870344484 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417133920677341 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417133903899722 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417133820011627 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417133803234008 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417133853566865 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417132982227620 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135170634509 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417132949268311 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135815778710 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595109143012326 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595111363598814 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595109563631775 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595110236942914 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108716769815 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108102204932 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595107197564009 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108959858406 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595110901278257 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595109137106592 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595109582877268 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595111076911683 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595111093689302 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108715513139 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595109783752230 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595111083415389 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595109974874944 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595109705820065 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108792128613 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417134413767654 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417136634354142 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417134834387103 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135507698242 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417133987525143 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417133372960260 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417132468319337 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417134230613734 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417136172033585 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417134407861920 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417134853632596 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417136347667011 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417136364444630 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417133986268467 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135054507558 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417136354170717 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135245630272 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417134976575393 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417134062883941 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595107177184076 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595109946065017 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108979102588 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595107701060963 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595110583019630 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108024270589 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595109960550150 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108660444171 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595110634993188 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595110447264350 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595110464041969 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595110480819588 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595107564757520 = TimeBlendData {
                mTime: f32 = 0
            }
            7395595109978072683 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595109820475455 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108063321032 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595107237397110 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108705181941 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595107929831867 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595111189640626 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595109946260441 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595107793810074 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595110327469411 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108539039775 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595107410901527 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595107635407855 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595110060242151 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595110197902625 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595110181125006 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595111295410852 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595110231457863 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595108884164772 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595107354045505 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595109657108759 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7395595109571339691 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417132447939404 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135216820345 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417134249857916 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417132971816291 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135853774958 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417133295025917 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135231305478 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417133931199499 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135905748516 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135718019678 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135734797297 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135751574916 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417132835512848 = TimeBlendData {
                mTime: f32 = 0
            }
            7179417135248828011 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135091230783 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417133334076360 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417132508152438 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417133975937269 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417133200587195 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417136460395954 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135217015769 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417133064565402 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135598224739 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417133809795103 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417132681656855 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417132906163183 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135330997479 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135468657953 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135451880334 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417136566166180 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417135502213191 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417134154920100 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417132624800833 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417134927864087 = TimeBlendData {
                mTime: f32 = 0.1
            }
            7179417134842095019 = TimeBlendData {
                mTime: f32 = 0.1
            }
            14989024251338963387 = TimeBlendData {
                mTime: f32 = 0
            }
            13668219688412284678 = TimeBlendData {
                mTime: f32 = 0
            }
            13668219686476005117 = TimeBlendData {
                mTime: f32 = 0
            }
            13668219687112178699 = TimeBlendData {
                mTime: f32 = 0
            }
            13255853226898489344 = TimeBlendData {
                mTime: f32 = 0.1
            }
            13255853228713258726 = TimeBlendData {
                mTime: f32 = 0
            }
            13255853230654678577 = TimeBlendData {
                mTime: f32 = 0
            }
            13255853228890506912 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030499387351568 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208474116596240 = TimeBlendData {
                mTime: f32 = 0
            }
            6391149149206848016 = TimeBlendData {
                mTime: f32 = 0
            }
            6030852524658106896 = TimeBlendData {
                mTime: f32 = 0
            }
            5958793199748358672 = TimeBlendData {
                mTime: f32 = 0
            }
            6174971174477603344 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597613481271824 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733632077373968 = TimeBlendData {
                mTime: f32 = 0
            }
            17876238946816729616 = TimeBlendData {
                mTime: f32 = 0
            }
            2291038459227513360 = TimeBlendData {
                mTime: f32 = 0
            }
            14602606876576424464 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352411066606096 = TimeBlendData {
                mTime: f32 = 0
            }
            6858422607256199696 = TimeBlendData {
                mTime: f32 = 0
            }
            8581015242425999888 = TimeBlendData {
                mTime: f32 = 0
            }
            18118361586325496336 = TimeBlendData {
                mTime: f32 = 0
            }
            10387562019942539792 = TimeBlendData {
                mTime: f32 = 0
            }
            13279411341980049936 = TimeBlendData {
                mTime: f32 = 0
            }
            6750317597516079632 = TimeBlendData {
                mTime: f32 = 0
            }
            4110781523761013264 = TimeBlendData {
                mTime: f32 = 0
            }
            225378344852759056 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364252648481296 = TimeBlendData {
                mTime: f32 = 0
            }
            7794375145891799568 = TimeBlendData {
                mTime: f32 = 0
            }
            16132709913741992464 = TimeBlendData {
                mTime: f32 = 0
            }
            8555650308037124624 = TimeBlendData {
                mTime: f32 = 0
            }
            10470220782972936720 = TimeBlendData {
                mTime: f32 = 0
            }
            16887049734496428560 = TimeBlendData {
                mTime: f32 = 0
            }
            16959109059406176784 = TimeBlendData {
                mTime: f32 = 0
            }
            6744920215194411536 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674968331362832 = TimeBlendData {
                mTime: f32 = 0
            }
            11332972175348179472 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647003268293136 = TimeBlendData {
                mTime: f32 = 0
            }
            16914982939069227536 = TimeBlendData {
                mTime: f32 = 0
            }
            12153837981500940816 = TimeBlendData {
                mTime: f32 = 0
            }
            10998256075366703632 = TimeBlendData {
                mTime: f32 = 0
            }
            326788329507103248 = TimeBlendData {
                mTime: f32 = 0
            }
            7073981170391949840 = TimeBlendData {
                mTime: f32 = 0
            }
            137847199123087888 = TimeBlendData {
                mTime: f32 = 0
            }
            13505060784748864016 = TimeBlendData {
                mTime: f32 = 0
            }
            12030100287235793424 = TimeBlendData {
                mTime: f32 = 0
            }
            7877028278220071440 = TimeBlendData {
                mTime: f32 = 0
            }
            14899996837422539280 = TimeBlendData {
                mTime: f32 = 0
            }
            2387881295918375440 = TimeBlendData {
                mTime: f32 = 0
            }
            14623473962299138576 = TimeBlendData {
                mTime: f32 = 0
            }
            14765799519107129872 = TimeBlendData {
                mTime: f32 = 0
            }
            2771149703373627920 = TimeBlendData {
                mTime: f32 = 0
            }
            4851743315957359120 = TimeBlendData {
                mTime: f32 = 0
            }
            7100566751666217488 = TimeBlendData {
                mTime: f32 = 0
            }
            3776056069340766736 = TimeBlendData {
                mTime: f32 = 0
            }
            12092313459749003792 = TimeBlendData {
                mTime: f32 = 0
            }
            6508400798609941008 = TimeBlendData {
                mTime: f32 = 0
            }
            14989024250973889040 = TimeBlendData {
                mTime: f32 = 0
            }
            14182735031247806992 = TimeBlendData {
                mTime: f32 = 0
            }
            14254794356157555216 = TimeBlendData {
                mTime: f32 = 0
            }
            17917054669570679312 = TimeBlendData {
                mTime: f32 = 0
            }
            14326853681067303440 = TimeBlendData {
                mTime: f32 = 0
            }
            5380891099370070544 = TimeBlendData {
                mTime: f32 = 0
            }
            5618283691395752464 = TimeBlendData {
                mTime: f32 = 0
            }
            12302783573265719824 = TimeBlendData {
                mTime: f32 = 0
            }
            240639587721126416 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702299440751120 = TimeBlendData {
                mTime: f32 = 0
            }
            12167572165927084560 = TimeBlendData {
                mTime: f32 = 0
            }
            11490697225726829072 = TimeBlendData {
                mTime: f32 = 0
            }
            3943776444920078864 = TimeBlendData {
                mTime: f32 = 0
            }
            396460210946023952 = TimeBlendData {
                mTime: f32 = 0
            }
            6700548057655910928 = TimeBlendData {
                mTime: f32 = 0
            }
            3370444846874731024 = TimeBlendData {
                mTime: f32 = 0
            }
            3084207949728686608 = TimeBlendData {
                mTime: f32 = 0
            }
            17371216857994076688 = TimeBlendData {
                mTime: f32 = 0
            }
            12030939626924646928 = TimeBlendData {
                mTime: f32 = 0
            }
            2786235694396449296 = TimeBlendData {
                mTime: f32 = 0
            }
            13668219686016492048 = TimeBlendData {
                mTime: f32 = 0
            }
            5986972888199307792 = TimeBlendData {
                mTime: f32 = 0
            }
            1141656007672570384 = TimeBlendData {
                mTime: f32 = 0
            }
            2105903344177619472 = TimeBlendData {
                mTime: f32 = 0
            }
            12520487343716803088 = TimeBlendData {
                mTime: f32 = 0
            }
            13111734577498661392 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675252588913168 = TimeBlendData {
                mTime: f32 = 0
            }
            13255853227318157840 = TimeBlendData {
                mTime: f32 = 0
            }
            7469273463346405904 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883336653611536 = TimeBlendData {
                mTime: f32 = 0
            }
            897461252601913872 = TimeBlendData {
                mTime: f32 = 0
            }
            10789042609151255056 = TimeBlendData {
                mTime: f32 = 0
            }
            11064262829283713552 = TimeBlendData {
                mTime: f32 = 0
            }
            4908483089522729488 = TimeBlendData {
                mTime: f32 = 0
            }
            10420667267082854928 = TimeBlendData {
                mTime: f32 = 0
            }
        }
        ObjectPath: hash = 0x6e5ceb16
    }
}
