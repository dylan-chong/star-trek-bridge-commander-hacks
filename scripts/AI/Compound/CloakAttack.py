# File: C (Python 1.5)

import App

def CreateAI(pShip, *lpTargets, **dKeywords):
    
    try:
        dKeywords = dKeywords['Keywords']
    except:
        pass

    pAllTargetsGroup = App.ObjectGroup_ForceToGroup(lpTargets)
    sInitialTarget = pAllTargetsGroup.GetNameTuple()[0]
    pBuilderAI = App.BuilderAI_Create(pShip, 'AlertLevel Builder', __name__)
    pBuilderAI.AddAIBlock('WarpBeforeDeath', 'BuilderCreate1')
    pBuilderAI.AddDependencyObject('WarpBeforeDeath', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('NoSensorsEvasive', 'BuilderCreate2')
    pBuilderAI.AddAIBlock('EvadeIncomingTorps', 'BuilderCreate3')
    pBuilderAI.AddDependencyObject('EvadeIncomingTorps', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('Intercept', 'BuilderCreate4')
    pBuilderAI.AddDependencyObject('Intercept', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('WayTooFar', 'BuilderCreate5')
    pBuilderAI.AddDependency('WayTooFar', 'Intercept')
    pBuilderAI.AddDependencyObject('WayTooFar', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('EvadeTorps', 'BuilderCreate6')
    pBuilderAI.AddDependencyObject('EvadeTorps', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddDependencyObject('EvadeTorps', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('Torprun', 'BuilderCreate7')
    pBuilderAI.AddDependencyObject('Torprun', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('PriorityList', 'BuilderCreate8')
    pBuilderAI.AddDependency('PriorityList', 'EvadeTorps')
    pBuilderAI.AddDependency('PriorityList', 'Torprun')
    pBuilderAI.AddAIBlock('FarEnough_TimeNotPassed', 'BuilderCreate9')
    pBuilderAI.AddDependency('FarEnough_TimeNotPassed', 'PriorityList')
    pBuilderAI.AddDependencyObject('FarEnough_TimeNotPassed', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('RearTorpRun', 'BuilderCreate10')
    pBuilderAI.AddDependencyObject('RearTorpRun', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('RearTorpsReady', 'BuilderCreate11')
    pBuilderAI.AddDependency('RearTorpsReady', 'RearTorpRun')
    pBuilderAI.AddDependencyObject('RearTorpsReady', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('EvadeTorps_2_2', 'BuilderCreate12')
    pBuilderAI.AddDependencyObject('EvadeTorps_2_2', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddDependencyObject('EvadeTorps_2_2', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('Flee_2', 'BuilderCreate13')
    pBuilderAI.AddDependencyObject('Flee_2', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('PriorityList_4_2', 'BuilderCreate14')
    pBuilderAI.AddDependency('PriorityList_4_2', 'EvadeTorps_2_2')
    pBuilderAI.AddDependency('PriorityList_4_2', 'Flee_2')
    pBuilderAI.AddAIBlock('NeedPower_OrTimeShort', 'BuilderCreate15')
    pBuilderAI.AddDependency('NeedPower_OrTimeShort', 'PriorityList_4_2')
    pBuilderAI.AddAIBlock('EvadeTorps_2', 'BuilderCreate16')
    pBuilderAI.AddDependencyObject('EvadeTorps_2', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddDependencyObject('EvadeTorps_2', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('Flee', 'BuilderCreate17')
    pBuilderAI.AddDependencyObject('Flee', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('PriorityList_4', 'BuilderCreate18')
    pBuilderAI.AddDependency('PriorityList_4', 'EvadeTorps_2')
    pBuilderAI.AddDependency('PriorityList_4', 'Flee')
    pBuilderAI.AddAIBlock('ShortTime', 'BuilderCreate19')
    pBuilderAI.AddDependency('ShortTime', 'PriorityList_4')
    pBuilderAI.AddAIBlock('FaceTarget', 'BuilderCreate20')
    pBuilderAI.AddDependencyObject('FaceTarget', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('PriorityList_5', 'BuilderCreate21')
    pBuilderAI.AddDependency('PriorityList_5', 'ShortTime')
    pBuilderAI.AddDependency('PriorityList_5', 'FaceTarget')
    pBuilderAI.AddAIBlock('Cloak', 'BuilderCreate22')
    pBuilderAI.AddDependency('Cloak', 'PriorityList_5')
    pBuilderAI.AddAIBlock('Sequence', 'BuilderCreate23')
    pBuilderAI.AddDependency('Sequence', 'NeedPower_OrTimeShort')
    pBuilderAI.AddDependency('Sequence', 'Cloak')
    pBuilderAI.AddAIBlock('PriorityList_3', 'BuilderCreate24')
    pBuilderAI.AddDependency('PriorityList_3', 'RearTorpsReady')
    pBuilderAI.AddDependency('PriorityList_3', 'Sequence')
    pBuilderAI.AddAIBlock('TooClose_ShortTime', 'BuilderCreate25')
    pBuilderAI.AddDependency('TooClose_ShortTime', 'PriorityList_3')
    pBuilderAI.AddDependencyObject('TooClose_ShortTime', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('OuterSequence', 'BuilderCreate26')
    pBuilderAI.AddDependency('OuterSequence', 'FarEnough_TimeNotPassed')
    pBuilderAI.AddDependency('OuterSequence', 'TooClose_ShortTime')
    pBuilderAI.AddAIBlock('PriorityList_2', 'BuilderCreate27')
    pBuilderAI.AddDependency('PriorityList_2', 'EvadeIncomingTorps')
    pBuilderAI.AddDependency('PriorityList_2', 'WayTooFar')
    pBuilderAI.AddDependency('PriorityList_2', 'OuterSequence')
    pBuilderAI.AddAIBlock('Fire', 'BuilderCreate28')
    pBuilderAI.AddDependency('Fire', 'PriorityList_2')
    pBuilderAI.AddDependencyObject('Fire', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddDependencyObject('Fire', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('SelectTarget', 'BuilderCreate29')
    pBuilderAI.AddDependency('SelectTarget', 'Fire')
    pBuilderAI.AddDependencyObject('SelectTarget', 'pAllTargetsGroup', pAllTargetsGroup)
    pBuilderAI.AddDependencyObject('SelectTarget', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('FollowTargetThroughWarp', 'BuilderCreate30')
    pBuilderAI.AddDependency('FollowTargetThroughWarp', 'SelectTarget')
    pBuilderAI.AddDependencyObject('FollowTargetThroughWarp', 'dKeywords', dKeywords)
    pBuilderAI.AddDependencyObject('FollowTargetThroughWarp', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('FollowThroughWarpFlag', 'BuilderCreate31')
    pBuilderAI.AddDependency('FollowThroughWarpFlag', 'FollowTargetThroughWarp')
    pBuilderAI.AddDependencyObject('FollowThroughWarpFlag', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('FleeAttackOrFollow', 'BuilderCreate32')
    pBuilderAI.AddDependency('FleeAttackOrFollow', 'WarpBeforeDeath')
    pBuilderAI.AddDependency('FleeAttackOrFollow', 'NoSensorsEvasive')
    pBuilderAI.AddDependency('FleeAttackOrFollow', 'SelectTarget')
    pBuilderAI.AddDependency('FleeAttackOrFollow', 'FollowThroughWarpFlag')
    pBuilderAI.AddAIBlock('PowerManagement', 'BuilderCreate33')
    pBuilderAI.AddDependency('PowerManagement', 'FleeAttackOrFollow')
    pBuilderAI.AddAIBlock('AlertLevel', 'BuilderCreate34')
    pBuilderAI.AddDependency('AlertLevel', 'PowerManagement')
    return pBuilderAI


def BuilderCreate1(pShip, dKeywords):
    import AI.Compound.Parts.WarpBeforeDeath
    pWarpBeforeDeath = AI.Compound.Parts.WarpBeforeDeath.CreateAI(pShip, dKeywords)
    return pWarpBeforeDeath


def BuilderCreate2(pShip):
    import AI.Compound.Parts.NoSensorsEvasive
    pNoSensorsEvasive = AI.Compound.Parts.NoSensorsEvasive.CreateAI(pShip)
    return pNoSensorsEvasive


def BuilderCreate3(pShip, dKeywords):
    import AI.Compound.Parts.EvadeTorps
    pEvadeIncomingTorps = AI.Compound.Parts.EvadeTorps.CreateAI(pShip, None, dKeywords)
    return pEvadeIncomingTorps


def BuilderCreate4(pShip, sInitialTarget):
    pIntercept = App.PlainAI_Create(pShip, 'Intercept')
    pIntercept.SetScriptModule('Intercept')
    pIntercept.SetInterruptable(1)
    pScript = pIntercept.GetScriptInstance()
    pScript.SetTargetObjectName(sInitialTarget)
    pScript.SetAddObjectRadius(1)
    return pIntercept


def BuilderCreate5(pShip, pIntercept, sInitialTarget):
    pNear = App.ConditionScript_Create('Conditions.ConditionInRange', 'ConditionInRange', 200.0, sInitialTarget, pShip.GetName())
    
    def EvalFunc(bNear):
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bNear:
            return DORMANT
        
        return ACTIVE

    pWayTooFar = App.ConditionalAI_Create(pShip, 'WayTooFar')
    pWayTooFar.SetInterruptable(1)
    pWayTooFar.SetContainedAI(pIntercept)
    pWayTooFar.AddCondition(pNear)
    pWayTooFar.SetEvaluationFunction(EvalFunc)
    return pWayTooFar


def BuilderCreate6(pShip, sInitialTarget, dKeywords):
    import AI.Compound.Parts.EvadeTorps
    pEvadeTorps = AI.Compound.Parts.EvadeTorps.CreateAI(pShip, sInitialTarget, dKeywords)
    return pEvadeTorps


def BuilderCreate7(pShip, sInitialTarget):
    pTorprun = App.PlainAI_Create(pShip, 'Torprun')
    pTorprun.SetScriptModule('TorpedoRun')
    pTorprun.SetInterruptable(1)
    pScript = pTorprun.GetScriptInstance()
    pScript.SetTargetObjectName(sInitialTarget)
    pScript.SetPerpendicularMovementAdjustment(0.3)
    return pTorprun


def BuilderCreate8(pShip, pEvadeTorps, pTorprun):
    pPriorityList = App.PriorityListAI_Create(pShip, 'PriorityList')
    pPriorityList.SetInterruptable(1)
    pPriorityList.AddAI(pEvadeTorps, 1)
    pPriorityList.AddAI(pTorprun, 2)
    return pPriorityList


def BuilderCreate9(pShip, pPriorityList, sInitialTarget):
    pInRange = App.ConditionScript_Create('Conditions.ConditionInRange', 'ConditionInRange', 50, sInitialTarget, pShip.GetName())
    pTimePassed = App.ConditionScript_Create('Conditions.ConditionTimer', 'ConditionTimer', 15.0)
    
    def EvalFunc(bInRange, bTimePassed):
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if not bTimePassed:
            return ACTIVE
        
        if bInRange:
            return DONE
        
        return ACTIVE

    pFarEnough_TimeNotPassed = App.ConditionalAI_Create(pShip, 'FarEnough_TimeNotPassed')
    pFarEnough_TimeNotPassed.SetInterruptable(1)
    pFarEnough_TimeNotPassed.SetContainedAI(pPriorityList)
    pFarEnough_TimeNotPassed.AddCondition(pInRange)
    pFarEnough_TimeNotPassed.AddCondition(pTimePassed)
    pFarEnough_TimeNotPassed.SetEvaluationFunction(EvalFunc)
    return pFarEnough_TimeNotPassed


def BuilderCreate10(pShip, sInitialTarget):
    pRearTorpRun = App.PlainAI_Create(pShip, 'RearTorpRun')
    pRearTorpRun.SetScriptModule('TorpedoRun')
    pRearTorpRun.SetInterruptable(1)
    pScript = pRearTorpRun.GetScriptInstance()
    pScript.SetTargetObjectName(sInitialTarget)
    pScript.SetTorpDirection(App.TGPoint3_GetModelBackward())
    return pRearTorpRun


def BuilderCreate11(pShip, pRearTorpRun, dKeywords):
    pReady = App.ConditionScript_Create('Conditions.ConditionTorpsReady', 'ConditionTorpsReady', pShip.GetName(), App.TGPoint3_GetModelBackward())
    pInUse = App.ConditionScript_Create('Conditions.ConditionUsingWeapon', 'ConditionUsingWeapon', App.CT_TORPEDO_SYSTEM)
    p = App.ConditionScript_Create('Conditions.ConditionFlagSet', 'ConditionFlagSet', 'UseRearTorps', dKeywords)
    
    def EvalFunc(bReady, bInUse, b):
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bReady and bInUse:
            return ACTIVE
        
        return DORMANT

    pRearTorpsReady = App.ConditionalAI_Create(pShip, 'RearTorpsReady')
    pRearTorpsReady.SetInterruptable(1)
    pRearTorpsReady.SetContainedAI(pRearTorpRun)
    pRearTorpsReady.AddCondition(pReady)
    pRearTorpsReady.AddCondition(pInUse)
    pRearTorpsReady.AddCondition(p)
    pRearTorpsReady.SetEvaluationFunction(EvalFunc)
    return pRearTorpsReady


def BuilderCreate12(pShip, sInitialTarget, dKeywords):
    import AI.Compound.Parts.EvadeTorps
    pEvadeTorps_2_2 = AI.Compound.Parts.EvadeTorps.CreateAI(pShip, sInitialTarget, dKeywords)
    return pEvadeTorps_2_2


def BuilderCreate13(pShip, sInitialTarget):
    pFlee_2 = App.PlainAI_Create(pShip, 'Flee_2')
    pFlee_2.SetScriptModule('Flee')
    pFlee_2.SetInterruptable(1)
    pScript = pFlee_2.GetScriptInstance()
    pScript.SetFleeFromGroup(sInitialTarget)
    return pFlee_2


def BuilderCreate14(pShip, pEvadeTorps_2_2, pFlee_2):
    pPriorityList_4_2 = App.PriorityListAI_Create(pShip, 'PriorityList_4_2')
    pPriorityList_4_2.SetInterruptable(1)
    pPriorityList_4_2.AddAI(pEvadeTorps_2_2, 1)
    pPriorityList_4_2.AddAI(pFlee_2, 2)
    return pPriorityList_4_2


def BuilderCreate15(pShip, pPriorityList_4_2):
    pPowerLow = App.ConditionScript_Create('Conditions.ConditionPowerBelow', 'ConditionPowerBelow', pShip, 1, 0.8)
    pTimePassed = App.ConditionScript_Create('Conditions.ConditionTimer', 'ConditionTimer', 55.0)
    
    def EvalFunc(bPowerLow, bTimePassed):
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bTimePassed:
            return ACTIVE
        
        if bPowerLow:
            return ACTIVE
        
        return DONE

    pNeedPower_OrTimeShort = App.ConditionalAI_Create(pShip, 'NeedPower_OrTimeShort')
    pNeedPower_OrTimeShort.SetInterruptable(1)
    pNeedPower_OrTimeShort.SetContainedAI(pPriorityList_4_2)
    pNeedPower_OrTimeShort.AddCondition(pPowerLow)
    pNeedPower_OrTimeShort.AddCondition(pTimePassed)
    pNeedPower_OrTimeShort.SetEvaluationFunction(EvalFunc)
    return pNeedPower_OrTimeShort


def BuilderCreate16(pShip, sInitialTarget, dKeywords):
    import AI.Compound.Parts.EvadeTorps
    pEvadeTorps_2 = AI.Compound.Parts.EvadeTorps.CreateAI(pShip, sInitialTarget, dKeywords)
    return pEvadeTorps_2


def BuilderCreate17(pShip, sInitialTarget):
    pFlee = App.PlainAI_Create(pShip, 'Flee')
    pFlee.SetScriptModule('Flee')
    pFlee.SetInterruptable(1)
    pScript = pFlee.GetScriptInstance()
    pScript.SetFleeFromGroup(sInitialTarget)
    return pFlee


def BuilderCreate18(pShip, pEvadeTorps_2, pFlee):
    pPriorityList_4 = App.PriorityListAI_Create(pShip, 'PriorityList_4')
    pPriorityList_4.SetInterruptable(1)
    pPriorityList_4.AddAI(pEvadeTorps_2, 1)
    pPriorityList_4.AddAI(pFlee, 2)
    return pPriorityList_4


def BuilderCreate19(pShip, pPriorityList_4):
    pTimePassed = App.ConditionScript_Create('Conditions.ConditionTimer', 'ConditionTimer', 30.0)
    
    def EvalFunc(bTimePassed):
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bTimePassed:
            return DORMANT
        
        return ACTIVE

    pShortTime = App.ConditionalAI_Create(pShip, 'ShortTime')
    pShortTime.SetInterruptable(1)
    pShortTime.SetContainedAI(pPriorityList_4)
    pShortTime.AddCondition(pTimePassed)
    pShortTime.SetEvaluationFunction(EvalFunc)
    return pShortTime


def BuilderCreate20(pShip, sInitialTarget):
    pFaceTarget = App.PlainAI_Create(pShip, 'FaceTarget')
    pFaceTarget.SetScriptModule('TurnToOrientation')
    pFaceTarget.SetInterruptable(1)
    pScript = pFaceTarget.GetScriptInstance()
    pScript.SetObjectName(sInitialTarget)
    return pFaceTarget


def BuilderCreate21(pShip, pShortTime, pFaceTarget):
    pPriorityList_5 = App.PriorityListAI_Create(pShip, 'PriorityList_5')
    pPriorityList_5.SetInterruptable(1)
    pPriorityList_5.AddAI(pShortTime, 1)
    pPriorityList_5.AddAI(pFaceTarget, 2)
    return pPriorityList_5


def BuilderCreate22(pShip, pPriorityList_5):
    import AI.Preprocessors
    pScript = AI.Preprocessors.CloakShip(1)
    pCloak = App.PreprocessingAI_Create(pShip, 'Cloak')
    pCloak.SetInterruptable(1)
    pCloak.SetPreprocessingMethod(pScript, 'Update')
    pCloak.SetContainedAI(pPriorityList_5)
    return pCloak


def BuilderCreate23(pShip, pNeedPower_OrTimeShort, pCloak):
    pSequence = App.SequenceAI_Create(pShip, 'Sequence')
    pSequence.SetInterruptable(1)
    pSequence.SetLoopCount(-1)
    pSequence.SetResetIfInterrupted(1)
    pSequence.SetDoubleCheckAllDone(0)
    pSequence.SetSkipDormant(0)
    pSequence.AddAI(pNeedPower_OrTimeShort)
    pSequence.AddAI(pCloak)
    return pSequence


def BuilderCreate24(pShip, pRearTorpsReady, pSequence):
    pPriorityList_3 = App.PriorityListAI_Create(pShip, 'PriorityList_3')
    pPriorityList_3.SetInterruptable(1)
    pPriorityList_3.AddAI(pRearTorpsReady, 1)
    pPriorityList_3.AddAI(pSequence, 2)
    return pPriorityList_3


def BuilderCreate25(pShip, pPriorityList_3, sInitialTarget):
    pInRange = App.ConditionScript_Create('Conditions.ConditionInRange', 'ConditionInRange', 100, sInitialTarget, pShip.GetName())
    pTimePassed = App.ConditionScript_Create('Conditions.ConditionTimer', 'ConditionTimer', 60.0)
    
    def EvalFunc(bInRange, bTimePassed):
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bTimePassed:
            return DONE
        
        if bInRange:
            return ACTIVE
        
        return DONE

    pTooClose_ShortTime = App.ConditionalAI_Create(pShip, 'TooClose_ShortTime')
    pTooClose_ShortTime.SetInterruptable(1)
    pTooClose_ShortTime.SetContainedAI(pPriorityList_3)
    pTooClose_ShortTime.AddCondition(pInRange)
    pTooClose_ShortTime.AddCondition(pTimePassed)
    pTooClose_ShortTime.SetEvaluationFunction(EvalFunc)
    return pTooClose_ShortTime


def BuilderCreate26(pShip, pFarEnough_TimeNotPassed, pTooClose_ShortTime):
    pOuterSequence = App.SequenceAI_Create(pShip, 'OuterSequence')
    pOuterSequence.SetInterruptable(1)
    pOuterSequence.SetLoopCount(-1)
    pOuterSequence.SetResetIfInterrupted(1)
    pOuterSequence.SetDoubleCheckAllDone(1)
    pOuterSequence.SetSkipDormant(0)
    pOuterSequence.AddAI(pFarEnough_TimeNotPassed)
    pOuterSequence.AddAI(pTooClose_ShortTime)
    return pOuterSequence


def BuilderCreate27(pShip, pEvadeIncomingTorps, pWayTooFar, pOuterSequence):
    pPriorityList_2 = App.PriorityListAI_Create(pShip, 'PriorityList_2')
    pPriorityList_2.SetInterruptable(1)
    pPriorityList_2.AddAI(pEvadeIncomingTorps, 1)
    pPriorityList_2.AddAI(pWayTooFar, 2)
    pPriorityList_2.AddAI(pOuterSequence, 3)
    return pPriorityList_2


def BuilderCreate28(pShip, pPriorityList_2, sInitialTarget, dKeywords):
    import AI.Preprocessors
    pFiringPreprocess = apply(AI.Preprocessors.FireScript, (sInitialTarget,), dKeywords)
    for pSystem in [
        pShip.GetTorpedoSystem(),
        pShip.GetPhaserSystem(),
        pShip.GetPulseWeaponSystem()]:
        if pSystem != None:
            pFiringPreprocess.AddWeaponSystem(pSystem)
        
    
    pFire = App.PreprocessingAI_Create(pShip, 'Fire')
    pFire.SetInterruptable(1)
    pFire.SetPreprocessingMethod(pFiringPreprocess, 'Update')
    pFire.SetContainedAI(pPriorityList_2)
    return pFire


def BuilderCreate29(pShip, pFire, pAllTargetsGroup, sInitialTarget):
    import AI.Preprocessors
    pSelectionPreprocess = AI.Preprocessors.SelectTarget(pAllTargetsGroup)
    pSelectTarget = App.PreprocessingAI_Create(pShip, 'SelectTarget')
    pSelectTarget.SetInterruptable(1)
    pSelectTarget.SetPreprocessingMethod(pSelectionPreprocess, 'Update')
    pSelectTarget.SetContainedAI(pFire)
    return pSelectTarget


def BuilderCreate30(pShip, pSelectTarget, dKeywords, sInitialTarget):
    import AI.Compound.FollowThroughWarp
    pFollowTargetThroughWarp = AI.Compound.FollowThroughWarp.CreateAI(pShip, sInitialTarget, Keywords = dKeywords)
    pSelectTarget.GetPreprocessingInstance().AddSetTargetTree(pFollowTargetThroughWarp)
    return pFollowTargetThroughWarp


def BuilderCreate31(pShip, pFollowTargetThroughWarp, dKeywords):
    pFollow = App.ConditionScript_Create('Conditions.ConditionFlagSet', 'ConditionFlagSet', 'FollowTargetThroughWarp', dKeywords)
    
    def EvalFunc(bFollow):
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bFollow:
            return ACTIVE
        
        return DONE

    pFollowThroughWarpFlag = App.ConditionalAI_Create(pShip, 'FollowThroughWarpFlag')
    pFollowThroughWarpFlag.SetInterruptable(1)
    pFollowThroughWarpFlag.SetContainedAI(pFollowTargetThroughWarp)
    pFollowThroughWarpFlag.AddCondition(pFollow)
    pFollowThroughWarpFlag.SetEvaluationFunction(EvalFunc)
    return pFollowThroughWarpFlag


def BuilderCreate32(pShip, pWarpBeforeDeath, pNoSensorsEvasive, pSelectTarget, pFollowThroughWarpFlag):
    pFleeAttackOrFollow = App.PriorityListAI_Create(pShip, 'FleeAttackOrFollow')
    pFleeAttackOrFollow.SetInterruptable(1)
    pFleeAttackOrFollow.AddAI(pWarpBeforeDeath, 1)
    pFleeAttackOrFollow.AddAI(pNoSensorsEvasive, 2)
    pFleeAttackOrFollow.AddAI(pSelectTarget, 3)
    pFleeAttackOrFollow.AddAI(pFollowThroughWarpFlag, 4)
    return pFleeAttackOrFollow


def BuilderCreate33(pShip, pFleeAttackOrFollow):
    import AI.Preprocessors
    pScript = AI.Preprocessors.ManagePower(1)
    pPowerManagement = App.PreprocessingAI_Create(pShip, 'PowerManagement')
    pPowerManagement.SetInterruptable(1)
    pPowerManagement.SetPreprocessingMethod(pScript, 'Update')
    pPowerManagement.SetContainedAI(pFleeAttackOrFollow)
    return pPowerManagement


def BuilderCreate34(pShip, pPowerManagement):
    import AI.Preprocessors
    pScript = AI.Preprocessors.AlertLevel(App.ShipClass.RED_ALERT)
    pAlertLevel = App.PreprocessingAI_Create(pShip, 'AlertLevel')
    pAlertLevel.SetInterruptable(1)
    pAlertLevel.SetPreprocessingMethod(pScript, 'Update')
    pAlertLevel.SetContainedAI(pPowerManagement)
    return pAlertLevel
    return pAlertLevel

