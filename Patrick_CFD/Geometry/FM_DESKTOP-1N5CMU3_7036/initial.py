import Prime
import PrimeApp
import PrimeScaffolder
import PrimeSlicer
import PrimeMorpher
import PrimeMatchMorph
import PrimeSurfer
import PrimeSizeField
import PrimeAutoMesh
import PrimeVolumeMeshTool
import PrimeSurfaceTools
import PrimeIO
import PrimeWeldMesher
import PrimeVTComposer
import PrimeVolumeSweeper
import PrimeVerticalizer
import PrimeFeature
import PrimeMorphFieldManager
import PrimeMeshToTopo
import PrimeMeshAssociator
model = Prime.Model.Get()
graphics = PrimeApp.Graphics.Get()
graphics.UseModel(model)
Model13p = Prime.Model.GetByName("Model13")
TopoData14p = Model13p.GetTopoData()
UndoStack20p = Model13p.GetUndoStack()
AssemblyData23p = Model13p.GetAssemblyData()
ControlData21p = Model13p.GetControlData()
ConnectorData16p = Model13p.GetConnectorData()
MaterialPointManager22p = Model13p.GetMaterialPointData()
Part1p = Model13p.GetPart(1)

params = Prime.GlobalSizingParams()
params.min = 0.1
params.max = 1
params.growthRate = 1.2
Model13p.SetGlobalSizingParams(params)

graphics = PrimeApp.Graphics.Get()
graphics.UseModel(model)
