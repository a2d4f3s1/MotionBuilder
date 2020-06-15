from pyfbsdk import FBSystem,FBPlotOptions,FBFindModelByLabelName,FBRotationFilter,FBTime,FBTimeMode

#FPS
lFPS = FBTime(0,0,0,1,0, FBTimeMode().kFBTimeMode60Frames)

# plotOptionを設定する
lOptions = FBPlotOptions()

lOptions.PlotLockedProperties = False
lOptions.ConstantKeyReducerKeepOneKey = True
lOptions.PlotAllTakes = False
lOptions.PlotOnFrame = True
lOptions.PlotPeriod = lFPS
lOptions.PlotTranslationOnRootOnly = True
lOptions.PreciseTimeDiscontinuities = False
lOptions.RotationFilterToApply = FBRotationFilter.kFBRotationFilterUnroll
lOptions.UseConstantKeyReducer = False

## plotOptionを設定する
FBSystem().CurrentTake.PlotTakeOnSelected( lOptions )
