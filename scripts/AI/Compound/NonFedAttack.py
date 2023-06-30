# File: N (Python 1.5)

import App

def CreateAI(pShip, *lpTargets, **dKeywords):
    pAllTargetsGroup = App.ObjectGroup_ForceToGroup(lpTargets)
    sInitialTarget = pAllTargetsGroup.GetNameTuple()[0]
    
    Random = lambda fMin, fMax: App.g_kSystemWrapper.GetRandomNumber((fMax - fMin) * 1000.0) / 1000.0 - fMin
    fCloseRange = 100.0 + Random(-20, 10)
    fMidRange = 200.0 + Random(-25, 20)
    fLongRange = 350.0 + Random(-20, 10)
    pBuilderAI = App.BuilderAI_Create(pShip, 'AlertLevel Builder', __name__)
    pBuilderAI.AddAIBlock('CheckWarpBeforeDeath', 'BuilderCreate1')
    pBuilderAI.AddDependencyObject('CheckWarpBeforeDeath', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('NoSensorsEvasive', 'BuilderCreate2')
    pBuilderAI.AddAIBlock('EvadeTorps_2', 'BuilderCreate3')
    pBuilderAI.AddDependencyObject('EvadeTorps_2', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddDependencyObject('EvadeTorps_2', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('TorpRun_2', 'BuilderCreate4')
    pBuilderAI.AddDependencyObject('TorpRun_2', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('NoStopping', 'BuilderCreate5')
    pBuilderAI.AddDependency('NoStopping', 'TorpRun_2')
    pBuilderAI.AddDependencyObject('NoStopping', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('StationaryAttack', 'BuilderCreate6')
    pBuilderAI.AddDependencyObject('StationaryAttack', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('PriorityList_2', 'BuilderCreate7')
    pBuilderAI.AddDependency('PriorityList_2', 'NoStopping')
    pBuilderAI.AddDependency('PriorityList_2', 'StationaryAttack')
    pBuilderAI.AddAIBlock('FwdTorpsOrPulseReady', 'BuilderCreate8')
    pBuilderAI.AddDependency('FwdTorpsOrPulseReady', 'PriorityList_2')
    pBuilderAI.AddDependencyObject('FwdTorpsOrPulseReady', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('RearTorpRun', 'BuilderCreate9')
    pBuilderAI.AddDependencyObject('RearTorpRun', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('StillClose', 'BuilderCreate10')
    pBuilderAI.AddDependency('StillClose', 'RearTorpRun')
    pBuilderAI.AddDependencyObject('StillClose', 'fCloseRange', fCloseRange)
    pBuilderAI.AddDependencyObject('StillClose', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('SlowRearTorpRun', 'BuilderCreate11')
    pBuilderAI.AddDependencyObject('SlowRearTorpRun', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('PriorityList_3', 'BuilderCreate12')
    pBuilderAI.AddDependency('PriorityList_3', 'StillClose')
    pBuilderAI.AddDependency('PriorityList_3', 'SlowRearTorpRun')
    pBuilderAI.AddAIBlock('RearTorpsReadySortaCloseNotInterruptable', 'BuilderCreate13')
    pBuilderAI.AddDependency('RearTorpsReadySortaCloseNotInterruptable', 'PriorityList_3')
    pBuilderAI.AddDependencyObject('RearTorpsReadySortaCloseNotInterruptable', 'fCloseRange', fCloseRange)
    pBuilderAI.AddDependencyObject('RearTorpsReadySortaCloseNotInterruptable', 'fMidRange', fMidRange)
    pBuilderAI.AddDependencyObject('RearTorpsReadySortaCloseNotInterruptable', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddDependencyObject('RearTorpsReadySortaCloseNotInterruptable', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('ICOMoveAround', 'BuilderCreate14')
    pBuilderAI.AddDependencyObject('ICOMoveAround', 'dKeywords', dKeywords)
    pBuilderAI.AddDependencyObject('ICOMoveAround', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('CloseRangePriorities', 'BuilderCreate15')
    pBuilderAI.AddDependency('CloseRangePriorities', 'EvadeTorps_2')
    pBuilderAI.AddDependency('CloseRangePriorities', 'FwdTorpsOrPulseReady')
    pBuilderAI.AddDependency('CloseRangePriorities', 'RearTorpsReadySortaCloseNotInterruptable')
    pBuilderAI.AddDependency('CloseRangePriorities', 'ICOMoveAround')
    pBuilderAI.AddAIBlock('FireAll', 'BuilderCreate16')
    pBuilderAI.AddDependency('FireAll', 'CloseRangePriorities')
    pBuilderAI.AddDependencyObject('FireAll', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddDependencyObject('FireAll', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('CloseRange', 'BuilderCreate17')
    pBuilderAI.AddDependency('CloseRange', 'FireAll')
    pBuilderAI.AddDependencyObject('CloseRange', 'fCloseRange', fCloseRange)
    pBuilderAI.AddDependencyObject('CloseRange', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('EvadeTorps_3', 'BuilderCreate18')
    pBuilderAI.AddDependencyObject('EvadeTorps_3', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddDependencyObject('EvadeTorps_3', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('TorpRun', 'BuilderCreate19')
    pBuilderAI.AddDependencyObject('TorpRun', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('FwdTorpsOrPulseReady_2', 'BuilderCreate20')
    pBuilderAI.AddDependency('FwdTorpsOrPulseReady_2', 'TorpRun')
    pBuilderAI.AddDependencyObject('FwdTorpsOrPulseReady_2', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('ICO_ShieldBiasMoveIn', 'BuilderCreate21')
    pBuilderAI.AddDependencyObject('ICO_ShieldBiasMoveIn', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('FwdShieldsLow', 'BuilderCreate22')
    pBuilderAI.AddDependency('FwdShieldsLow', 'ICO_ShieldBiasMoveIn')
    pBuilderAI.AddDependencyObject('FwdShieldsLow', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('Follow', 'BuilderCreate23')
    pBuilderAI.AddDependencyObject('Follow', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('MidRangePriorities', 'BuilderCreate24')
    pBuilderAI.AddDependency('MidRangePriorities', 'EvadeTorps_3')
    pBuilderAI.AddDependency('MidRangePriorities', 'FwdTorpsOrPulseReady_2')
    pBuilderAI.AddDependency('MidRangePriorities', 'FwdShieldsLow')
    pBuilderAI.AddDependency('MidRangePriorities', 'Follow')
    pBuilderAI.AddAIBlock('FireAll2', 'BuilderCreate25')
    pBuilderAI.AddDependency('FireAll2', 'MidRangePriorities')
    pBuilderAI.AddDependencyObject('FireAll2', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddDependencyObject('FireAll2', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('MidRange', 'BuilderCreate26')
    pBuilderAI.AddDependency('MidRange', 'FireAll2')
    pBuilderAI.AddDependencyObject('MidRange', 'fMidRange', fMidRange)
    pBuilderAI.AddDependencyObject('MidRange', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('EvadeTorps', 'BuilderCreate27')
    pBuilderAI.AddDependencyObject('EvadeTorps', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddDependencyObject('EvadeTorps', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('MoveIn', 'BuilderCreate28')
    pBuilderAI.AddDependencyObject('MoveIn', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('LongRangePriorities', 'BuilderCreate29')
    pBuilderAI.AddDependency('LongRangePriorities', 'EvadeTorps')
    pBuilderAI.AddDependency('LongRangePriorities', 'MoveIn')
    pBuilderAI.AddAIBlock('FirePulseOnly', 'BuilderCreate30')
    pBuilderAI.AddDependency('FirePulseOnly', 'LongRangePriorities')
    pBuilderAI.AddDependencyObject('FirePulseOnly', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddDependencyObject('FirePulseOnly', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('LongRange', 'BuilderCreate31')
    pBuilderAI.AddDependency('LongRange', 'FirePulseOnly')
    pBuilderAI.AddDependencyObject('LongRange', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('InterceptTarget', 'BuilderCreate32')
    pBuilderAI.AddDependencyObject('InterceptTarget', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('PriorityList', 'BuilderCreate33')
    pBuilderAI.AddDependency('PriorityList', 'CloseRange')
    pBuilderAI.AddDependency('PriorityList', 'MidRange')
    pBuilderAI.AddDependency('PriorityList', 'LongRange')
    pBuilderAI.AddDependency('PriorityList', 'InterceptTarget')
    pBuilderAI.AddAIBlock('SelectTarget', 'BuilderCreate34')
    pBuilderAI.AddDependency('SelectTarget', 'PriorityList')
    pBuilderAI.AddDependencyObject('SelectTarget', 'pAllTargetsGroup', pAllTargetsGroup)
    pBuilderAI.AddDependencyObject('SelectTarget', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('FollowTargetThroughWarp', 'BuilderCreate35')
    pBuilderAI.AddDependency('FollowTargetThroughWarp', 'SelectTarget')
    pBuilderAI.AddDependencyObject('FollowTargetThroughWarp', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddDependencyObject('FollowTargetThroughWarp', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('FollowThroughWarpFlag', 'BuilderCreate36')
    pBuilderAI.AddDependency('FollowThroughWarpFlag', 'FollowTargetThroughWarp')
    pBuilderAI.AddDependencyObject('FollowThroughWarpFlag', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('FleeAttackOrFollow', 'BuilderCreate37')
    pBuilderAI.AddDependency('FleeAttackOrFollow', 'CheckWarpBeforeDeath')
    pBuilderAI.AddDependency('FleeAttackOrFollow', 'NoSensorsEvasive')
    pBuilderAI.AddDependency('FleeAttackOrFollow', 'SelectTarget')
    pBuilderAI.AddDependency('FleeAttackOrFollow', 'FollowThroughWarpFlag')
    pBuilderAI.AddAIBlock('PowerManagement', 'BuilderCreate38')
    pBuilderAI.AddDependency('PowerManagement', 'FleeAttackOrFollow')
    pBuilderAI.AddDependencyObject('PowerManagement', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('AlertLevel', 'BuilderCreate39')
    pBuilderAI.AddDependency('AlertLevel', 'PowerManagement')
    return pBuilderAI


def BuilderCreate1(pShip, dKeywords):
    import AI.Compound.Parts.WarpBeforeDeath
    pCheckWarpBeforeDeath = AI.Compound.Parts.WarpBeforeDeath.CreateAI(pShip, dKeywords)
    return pCheckWarpBeforeDeath


def BuilderCreate2(pShip):
    import AI.Compound.Parts.NoSensorsEvasive
    pNoSensorsEvasive = AI.Compound.Parts.NoSensorsEvasive.CreateAI(pShip)
    return pNoSensorsEvasive


def BuilderCreate3(pShip, sInitialTarget, dKeywords):
    import AI.Compound.Parts.EvadeTorps
    pEvadeTorps_2 = AI.Compound.Parts.EvadeTorps.CreateAI(pShip, sInitialTarget, dKeywords)
    return pEvadeTorps_2


def BuilderCreate4(pShip, sInitialTarget):
    pTorpRun_2 = App.PlainAI_Create(pShip, 'TorpRun_2')
    pTorpRun_2.SetScriptModule('TorpedoRun')
    pTorpRun_2.SetInterruptable(1)
    pScript = pTorpRun_2.GetScriptInstance()
    pScript.SetTargetObjectName(sInitialTarget)
    pScript.SetPerpendicularMovementAdjustment(0.5)
    return pTorpRun_2


def BuilderCreate5(pShip, pTorpRun_2, dKeywords):
    pFlagSet = App.ConditionScript_Create('Conditions.ConditionFlagSet', 'ConditionFlagSet', 'NeverSitStill', dKeywords)
    
    def EvalFunc(bFlagSet):
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bFlagSet:
            return ACTIVE
        
        return DONE

    pNoStopping = App.ConditionalAI_Create(pShip, 'NoStopping')
    pNoStopping.SetInterruptable(1)
    pNoStopping.SetContainedAI(pTorpRun_2)
    pNoStopping.AddCondition(pFlagSet)
    pNoStopping.SetEvaluationFunction(EvalFunc)
    return pNoStopping


def BuilderCreate6(pShip, sInitialTarget):
    pStationaryAttack = App.PlainAI_Create(pShip, 'StationaryAttack')
    pStationaryAttack.SetScriptModule('StationaryAttack')
    pStationaryAttack.SetInterruptable(1)
    pScript = pStationaryAttack.GetScriptInstance()
    pScript.SetTargetObjectName(sInitialTarget)
    return pStationaryAttack


def BuilderCreate7(pShip, pNoStopping, pStationaryAttack):
    pPriorityList_2 = App.PriorityListAI_Create(pShip, 'PriorityList_2')
    pPriorityList_2.SetInterruptable(1)
    pPriorityList_2.AddAI(pNoStopping, 1)
    pPriorityList_2.AddAI(pStationaryAttack, 2)
    return pPriorityList_2


def BuilderCreate8(pShip, pPriorityList_2, dKeywords):
    pTorpsReady = App.ConditionScript_Create('Conditions.ConditionTorpsReady', 'ConditionTorpsReady', pShip.GetName(), App.TGPoint3_GetModelForward())
    pPulseReady = App.ConditionScript_Create('Conditions.ConditionPulseReady', 'ConditionPulseReady', pShip.GetName(), App.TGPoint3_GetModelForward())
    pAggroPulse = App.ConditionScript_Create('Conditions.ConditionFlagSet', 'ConditionFlagSet', 'AggressivePulseWeapons', dKeywords)
    pUsingTorps = App.ConditionScript_Create('Conditions.ConditionUsingWeapon', 'ConditionUsingWeapon', App.CT_TORPEDO_SYSTEM)
    
    def EvalFunc(bTorpsReady, bPulseReady, bAggroPulse, bUsingTorps):
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bUsingTorps and bTorpsReady and bAggroPulse and bPulseReady:
            return ACTIVE
        
        return DORMANT

    pFwdTorpsOrPulseReady = App.ConditionalAI_Create(pShip, 'FwdTorpsOrPulseReady')
    pFwdTorpsOrPulseReady.SetInterruptable(1)
    pFwdTorpsOrPulseReady.SetContainedAI(pPriorityList_2)
    pFwdTorpsOrPulseReady.AddCondition(pTorpsReady)
    pFwdTorpsOrPulseReady.AddCondition(pPulseReady)
    pFwdTorpsOrPulseReady.AddCondition(pAggroPulse)
    pFwdTorpsOrPulseReady.AddCondition(pUsingTorps)
    pFwdTorpsOrPulseReady.SetEvaluationFunction(EvalFunc)
    return pFwdTorpsOrPulseReady


def BuilderCreate9(pShip, sInitialTarget):
    pRearTorpRun = App.PlainAI_Create(pShip, 'RearTorpRun')
    pRearTorpRun.SetScriptModule('TorpedoRun')
    pRearTorpRun.SetInterruptable(1)
    pScript = pRearTorpRun.GetScriptInstance()
    pScript.SetTargetObjectName(sInitialTarget)
    pScript.SetPerpendicularMovementAdjustment(0.3)
    pScript.SetTorpDirection(App.TGPoint3_GetModelBackward())
    return pRearTorpRun


def BuilderCreate10(pShip, pRearTorpRun, fCloseRange, sInitialTarget):
    pInRange = App.ConditionScript_Create('Conditions.ConditionInRange', 'ConditionInRange', fCloseRange, sInitialTarget, pShip.GetName())
    
    def EvalFunc(bInRange):
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bInRange:
            return ACTIVE
        
        return DORMANT

    pStillClose = App.ConditionalAI_Create(pShip, 'StillClose')
    pStillClose.SetInterruptable(1)
    pStillClose.SetContainedAI(pRearTorpRun)
    pStillClose.AddCondition(pInRange)
    pStillClose.SetEvaluationFunction(EvalFunc)
    return pStillClose


def BuilderCreate11(pShip, sInitialTarget):
    pSlowRearTorpRun = App.PlainAI_Create(pShip, 'SlowRearTorpRun')
    pSlowRearTorpRun.SetScriptModule('TorpedoRun')
    pSlowRearTorpRun.SetInterruptable(1)
    pScript = pSlowRearTorpRun.GetScriptInstance()
    pScript.SetTargetObjectName(sInitialTarget)
    pScript.SetPerpendicularMovementAdjustment(0.0)
    pScript.SetTorpDirection(App.TGPoint3_GetModelBackward())
    return pSlowRearTorpRun


def BuilderCreate12(pShip, pStillClose, pSlowRearTorpRun):
    pPriorityList_3 = App.PriorityListAI_Create(pShip, 'PriorityList_3')
    pPriorityList_3.SetInterruptable(1)
    pPriorityList_3.AddAI(pStillClose, 1)
    pPriorityList_3.AddAI(pSlowRearTorpRun, 2)
    return pPriorityList_3


def BuilderCreate13(pShip, pPriorityList_3, fCloseRange, fMidRange, sInitialTarget, dKeywords):
    pFlagSet = App.ConditionScript_Create('Conditions.ConditionFlagSet', 'ConditionFlagSet', 'UseRearTorps', dKeywords)
    pReady = App.ConditionScript_Create('Conditions.ConditionTorpsReady', 'ConditionTorpsReady', pShip.GetName(), App.TGPoint3_GetModelBackward())
    pSomewhatClose = App.ConditionScript_Create('Conditions.ConditionInRange', 'ConditionInRange', (fCloseRange + fMidRange) / 2.0, sInitialTarget, pShip.GetName())
    pUsingTorps = App.ConditionScript_Create('Conditions.ConditionUsingWeapon', 'ConditionUsingWeapon', App.CT_TORPEDO_SYSTEM)
    
    def EvalFunc(bFlagSet, bReady, bSomewhatClose, bUsingTorps):
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if not bFlagSet:
            return DONE
        
        if bUsingTorps and bReady and bSomewhatClose:
            return ACTIVE
        
        return DORMANT

    pRearTorpsReadySortaCloseNotInterruptable = App.ConditionalAI_Create(pShip, 'RearTorpsReadySortaCloseNotInterruptable')
    pRearTorpsReadySortaCloseNotInterruptable.SetInterruptable(0)
    pRearTorpsReadySortaCloseNotInterruptable.SetContainedAI(pPriorityList_3)
    pRearTorpsReadySortaCloseNotInterruptable.AddCondition(pFlagSet)
    pRearTorpsReadySortaCloseNotInterruptable.AddCondition(pReady)
    pRearTorpsReadySortaCloseNotInterruptable.AddCondition(pSomewhatClose)
    pRearTorpsReadySortaCloseNotInterruptable.AddCondition(pUsingTorps)
    pRearTorpsReadySortaCloseNotInterruptable.SetEvaluationFunction(EvalFunc)
    return pRearTorpsReadySortaCloseNotInterruptable


def BuilderCreate14(pShip, dKeywords, sInitialTarget):
    import AI.Compound.Parts.ICOMove
    pICOMoveAround = AI.Compound.Parts.ICOMove.CreateAI(pShip, sInitialTarget, dKeywords)
    return pICOMoveAround


def BuilderCreate15(pShip, pEvadeTorps_2, pFwdTorpsOrPulseReady, pRearTorpsReadySortaCloseNotInterruptable, pICOMoveAround):
    pCloseRangePriorities = App.PriorityListAI_Create(pShip, 'CloseRangePriorities')
    pCloseRangePriorities.SetInterruptable(1)
    pCloseRangePriorities.AddAI(pEvadeTorps_2, 1)
    pCloseRangePriorities.AddAI(pFwdTorpsOrPulseReady, 2)
    pCloseRangePriorities.AddAI(pRearTorpsReadySortaCloseNotInterruptable, 3)
    pCloseRangePriorities.AddAI(pICOMoveAround, 4)
    return pCloseRangePriorities


def BuilderCreate16(pShip, pCloseRangePriorities, sInitialTarget, dKeywords):
    import AI.Preprocessors
    pFireScript = apply(AI.Preprocessors.FireScript, (sInitialTarget,), dKeywords)
    for pSystem in [
        pShip.GetTorpedoSystem(),
        pShip.GetPhaserSystem(),
        pShip.GetPulseWeaponSystem()]:
        if not App.IsNull(pSystem):
            pFireScript.AddWeaponSystem(pSystem)
        
    
    pFireAll = App.PreprocessingAI_Create(pShip, 'FireAll')
    pFireAll.SetInterruptable(1)
    pFireAll.SetPreprocessingMethod(pFireScript, 'Update')
    pFireAll.SetContainedAI(pCloseRangePriorities)
    return pFireAll


def BuilderCreate17(pShip, pFireAll, fCloseRange, sInitialTarget):
    pInRange = App.ConditionScript_Create('Conditions.ConditionInRange', 'ConditionInRange', fCloseRange, sInitialTarget, pShip.GetName())
    
    def EvalFunc(bInRange):
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bInRange:
            return ACTIVE
        
        return DORMANT

    pCloseRange = App.ConditionalAI_Create(pShip, 'CloseRange')
    pCloseRange.SetInterruptable(1)
    pCloseRange.SetContainedAI(pFireAll)
    pCloseRange.AddCondition(pInRange)
    pCloseRange.SetEvaluationFunction(EvalFunc)
    return pCloseRange


def BuilderCreate18(pShip, sInitialTarget, dKeywords):
    import AI.Compound.Parts.EvadeTorps
    pEvadeTorps_3 = AI.Compound.Parts.EvadeTorps.CreateAI(pShip, sInitialTarget, dKeywords)
    return pEvadeTorps_3


def BuilderCreate19(pShip, sInitialTarget):
    pTorpRun = App.PlainAI_Create(pShip, 'TorpRun')
    pTorpRun.SetScriptModule('TorpedoRun')
    pTorpRun.SetInterruptable(1)
    pScript = pTorpRun.GetScriptInstance()
    pScript.SetTargetObjectName(sInitialTarget)
    pScript.SetPerpendicularMovementAdjustment(0.9)
    return pTorpRun


def BuilderCreate20(pShip, pTorpRun, dKeywords):
    pTorpsReady = App.ConditionScript_Create('Conditions.ConditionTorpsReady', 'ConditionTorpsReady', pShip.GetName(), App.TGPoint3_GetModelForward())
    pPulseReady = App.ConditionScript_Create('Conditions.ConditionPulseReady', 'ConditionPulseReady', pShip.GetName(), App.TGPoint3_GetModelForward())
    pAggroPulse = App.ConditionScript_Create('Conditions.ConditionFlagSet', 'ConditionFlagSet', 'AggressivePulseWeapons', dKeywords)
    pUsingTorps = App.ConditionScript_Create('Conditions.ConditionUsingWeapon', 'ConditionUsingWeapon', App.CT_TORPEDO_SYSTEM)
    
    def EvalFunc(bTorpsReady, bPulseReady, bAggroPulse, bUsingTorps):
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bUsingTorps and bTorpsReady and bAggroPulse and bPulseReady:
            return ACTIVE
        
        return DORMANT

    pFwdTorpsOrPulseReady_2 = App.ConditionalAI_Create(pShip, 'FwdTorpsOrPulseReady_2')
    pFwdTorpsOrPulseReady_2.SetInterruptable(1)
    pFwdTorpsOrPulseReady_2.SetContainedAI(pTorpRun)
    pFwdTorpsOrPulseReady_2.AddCondition(pTorpsReady)
    pFwdTorpsOrPulseReady_2.AddCondition(pPulseReady)
    pFwdTorpsOrPulseReady_2.AddCondition(pAggroPulse)
    pFwdTorpsOrPulseReady_2.AddCondition(pUsingTorps)
    pFwdTorpsOrPulseReady_2.SetEvaluationFunction(EvalFunc)
    return pFwdTorpsOrPulseReady_2


def BuilderCreate21(pShip, sInitialTarget):
    pICO_ShieldBiasMoveIn = App.PlainAI_Create(pShip, 'ICO_ShieldBiasMoveIn')
    pICO_ShieldBiasMoveIn.SetScriptModule('IntelligentCircleObject')
    pICO_ShieldBiasMoveIn.SetInterruptable(1)
    pScript = pICO_ShieldBiasMoveIn.GetScriptInstance()
    pScript.SetFollowObjectName(sInitialTarget)
    pScript.SetShieldAndWeaponImportance(1.0, 0.0)
    pScript.SetForwardBias(0.5)
    return pICO_ShieldBiasMoveIn


def BuilderCreate22(pShip, pICO_ShieldBiasMoveIn, dKeywords):
    pShieldLow = App.ConditionScript_Create('Conditions.ConditionSingleShieldBelow', 'ConditionSingleShieldBelow', pShip.GetName(), 0.25, App.ShieldClass.FRONT_SHIELDS)
    pSmartShields = App.ConditionScript_Create('Conditions.ConditionFlagSet', 'ConditionFlagSet', 'SmartShields', dKeywords)
    
    def EvalFunc(bShieldLow, bSmartShields):
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if not bSmartShields:
            return DONE
        
        if bShieldLow:
            return ACTIVE
        
        return DORMANT

    pFwdShieldsLow = App.ConditionalAI_Create(pShip, 'FwdShieldsLow')
    pFwdShieldsLow.SetInterruptable(1)
    pFwdShieldsLow.SetContainedAI(pICO_ShieldBiasMoveIn)
    pFwdShieldsLow.AddCondition(pShieldLow)
    pFwdShieldsLow.AddCondition(pSmartShields)
    pFwdShieldsLow.SetEvaluationFunction(EvalFunc)
    return pFwdShieldsLow


def BuilderCreate23(pShip, sInitialTarget):
    pFollow = App.PlainAI_Create(pShip, 'Follow')
    pFollow.SetScriptModule('FollowObject')
    pFollow.SetInterruptable(1)
    pScript = pFollow.GetScriptInstance()
    pScript.SetFollowObjectName(sInitialTarget)
    return pFollow


def BuilderCreate24(pShip, pEvadeTorps_3, pFwdTorpsOrPulseReady_2, pFwdShieldsLow, pFollow):
    pMidRangePriorities = App.PriorityListAI_Create(pShip, 'MidRangePriorities')
    pMidRangePriorities.SetInterruptable(1)
    pMidRangePriorities.AddAI(pEvadeTorps_3, 1)
    pMidRangePriorities.AddAI(pFwdTorpsOrPulseReady_2, 2)
    pMidRangePriorities.AddAI(pFwdShieldsLow, 3)
    pMidRangePriorities.AddAI(pFollow, 4)
    return pMidRangePriorities


def BuilderCreate25(pShip, pMidRangePriorities, sInitialTarget, dKeywords):
    import AI.Preprocessors
    pFireScript = apply(AI.Preprocessors.FireScript, (sInitialTarget,), dKeywords)
    for pSystem in [
        pShip.GetTorpedoSystem(),
        pShip.GetPhaserSystem(),
        pShip.GetPulseWeaponSystem()]:
        if not App.IsNull(pSystem):
            pFireScript.AddWeaponSystem(pSystem)
        
    
    pFireAll2 = App.PreprocessingAI_Create(pShip, 'FireAll2')
    pFireAll2.SetInterruptable(1)
    pFireAll2.SetPreprocessingMethod(pFireScript, 'Update')
    pFireAll2.SetContainedAI(pMidRangePriorities)
    return pFireAll2


def BuilderCreate26(pShip, pFireAll2, fMidRange, sInitialTarget):
    pInRange = App.ConditionScript_Create('Conditions.ConditionInRange', 'ConditionInRange', fMidRange, sInitialTarget, pShip.GetName())
    
    def EvalFunc(bInRange):
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bInRange:
            return ACTIVE
        
        return DORMANT

    pMidRange = App.ConditionalAI_Create(pShip, 'MidRange')
    pMidRange.SetInterruptable(1)
    pMidRange.SetContainedAI(pFireAll2)
    pMidRange.AddCondition(pInRange)
    pMidRange.SetEvaluationFunction(EvalFunc)
    return pMidRange


def BuilderCreate27(pShip, sInitialTarget, dKeywords):
    import AI.Compound.Parts.EvadeTorps
    pEvadeTorps = AI.Compound.Parts.EvadeTorps.CreateAI(pShip, sInitialTarget, dKeywords)
    return pEvadeTorps


def BuilderCreate28(pShip, sInitialTarget):
    pMoveIn = App.PlainAI_Create(pShip, 'MoveIn')
    pMoveIn.SetScriptModule('Intercept')
    pMoveIn.SetInterruptable(1)
    pScript = pMoveIn.GetScriptInstance()
    pScript.SetTargetObjectName(sInitialTarget)
    pScript.SetInterceptDistance(0)
    return pMoveIn


def BuilderCreate29(pShip, pEvadeTorps, pMoveIn):
    pLongRangePriorities = App.PriorityListAI_Create(pShip, 'LongRangePriorities')
    pLongRangePriorities.SetInterruptable(1)
    pLongRangePriorities.AddAI(pEvadeTorps, 1)
    pLongRangePriorities.AddAI(pMoveIn, 2)
    return pLongRangePriorities


def BuilderCreate30(pShip, pLongRangePriorities, sInitialTarget, dKeywords):
    import AI.Preprocessors
    pFireScript = apply(AI.Preprocessors.FireScript, (sInitialTarget,), dKeywords)
    for pSystem in [
        pShip.GetPulseWeaponSystem()]:
        if not App.IsNull(pSystem):
            pFireScript.AddWeaponSystem(pSystem)
        
    
    pFirePulseOnly = App.PreprocessingAI_Create(pShip, 'FirePulseOnly')
    pFirePulseOnly.SetInterruptable(1)
    pFirePulseOnly.SetPreprocessingMethod(pFireScript, 'Update')
    pFirePulseOnly.SetContainedAI(pLongRangePriorities)
    return pFirePulseOnly


def BuilderCreate31(pShip, pFirePulseOnly, sInitialTarget):
    pInRange = App.ConditionScript_Create('Conditions.ConditionInRange', 'ConditionInRange', 350.0, sInitialTarget, pShip.GetName())
    
    def EvalFunc(bInRange):
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bInRange:
            return ACTIVE
        
        return DORMANT

    pLongRange = App.ConditionalAI_Create(pShip, 'LongRange')
    pLongRange.SetInterruptable(1)
    pLongRange.SetContainedAI(pFirePulseOnly)
    pLongRange.AddCondition(pInRange)
    pLongRange.SetEvaluationFunction(EvalFunc)
    return pLongRange


def BuilderCreate32(pShip, sInitialTarget):
    pInterceptTarget = App.PlainAI_Create(pShip, 'InterceptTarget')
    pInterceptTarget.SetScriptModule('Intercept')
    pInterceptTarget.SetInterruptable(1)
    pScript = pInterceptTarget.GetScriptInstance()
    pScript.SetTargetObjectName(sInitialTarget)
    return pInterceptTarget


def BuilderCreate33(pShip, pCloseRange, pMidRange, pLongRange, pInterceptTarget):
    pPriorityList = App.PriorityListAI_Create(pShip, 'PriorityList')
    pPriorityList.SetInterruptable(1)
    pPriorityList.AddAI(pCloseRange, 1)
    pPriorityList.AddAI(pMidRange, 2)
    pPriorityList.AddAI(pLongRange, 3)
    pPriorityList.AddAI(pInterceptTarget, 4)
    return pPriorityList


def BuilderCreate34(pShip, pPriorityList, pAllTargetsGroup, sInitialTarget):
    import AI.Preprocessors
    pSelectionPreprocess = AI.Preprocessors.SelectTarget(pAllTargetsGroup)
    pSelectionPreprocess.ForceCurrentTargetString(sInitialTarget)
    pSelectTarget = App.PreprocessingAI_Create(pShip, 'SelectTarget')
    pSelectTarget.SetInterruptable(1)
    pSelectTarget.SetPreprocessingMethod(pSelectionPreprocess, 'Update')
    pSelectTarget.SetContainedAI(pPriorityList)
    return pSelectTarget


def BuilderCreate35(pShip, pSelectTarget, sInitialTarget, dKeywords):
    import AI.Compound.FollowThroughWarp
    pFollowTargetThroughWarp = AI.Compound.FollowThroughWarp.CreateAI(pShip, sInitialTarget, Keywords = dKeywords)
    pSelectTarget.GetPreprocessingInstance().AddSetTargetTree(pFollowTargetThroughWarp)
    return pFollowTargetThroughWarp


def BuilderCreate36(pShip, pFollowTargetThroughWarp, dKeywords):
    pFlagSet = App.ConditionScript_Create('Conditions.ConditionFlagSet', 'ConditionFlagSet', 'FollowTargetThroughWarp', dKeywords)
    
    def EvalFunc(bFlagSet):
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bFlagSet:
            return ACTIVE
        
        return DONE

    pFollowThroughWarpFlag = App.ConditionalAI_Create(pShip, 'FollowThroughWarpFlag')
    pFollowThroughWarpFlag.SetInterruptable(1)
    pFollowThroughWarpFlag.SetContainedAI(pFollowTargetThroughWarp)
    pFollowThroughWarpFlag.AddCondition(pFlagSet)
    pFollowThroughWarpFlag.SetEvaluationFunction(EvalFunc)
    return pFollowThroughWarpFlag


def BuilderCreate37(pShip, pCheckWarpBeforeDeath, pNoSensorsEvasive, pSelectTarget, pFollowThroughWarpFlag):
    pFleeAttackOrFollow = App.PriorityListAI_Create(pShip, 'FleeAttackOrFollow')
    pFleeAttackOrFollow.SetInterruptable(1)
    pFleeAttackOrFollow.AddAI(pCheckWarpBeforeDeath, 1)
    pFleeAttackOrFollow.AddAI(pNoSensorsEvasive, 2)
    pFleeAttackOrFollow.AddAI(pSelectTarget, 3)
    pFleeAttackOrFollow.AddAI(pFollowThroughWarpFlag, 4)
    return pFleeAttackOrFollow


def BuilderCreate38(pShip, pFleeAttackOrFollow, dKeywords):
    import AI.Preprocessors
    pPowerManager = AI.Preprocessors.ManagePower(0)
    pPowerManagement = App.PreprocessingAI_Create(pShip, 'PowerManagement')
    pPowerManagement.SetInterruptable(1)
    pPowerManagement.SetPreprocessingMethod(pPowerManager, 'Update')
    pPowerManagement.SetContainedAI(pFleeAttackOrFollow)
    return pPowerManagement


def BuilderCreate39(pShip, pPowerManagement):
    import AI.Preprocessors
    pScript = AI.Preprocessors.AlertLevel(App.ShipClass.RED_ALERT)
    pAlertLevel = App.PreprocessingAI_Create(pShip, 'AlertLevel')
    pAlertLevel.SetInterruptable(1)
    pAlertLevel.SetPreprocessingMethod(pScript, 'Update')
    pAlertLevel.SetContainedAI(pPowerManagement)
    return pAlertLevel
    return pAlertLevel

