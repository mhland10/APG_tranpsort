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
Model128p = Prime.Model.GetByName("Model128")
TopoData129p = Model128p.GetTopoData()
UndoStack135p = Model128p.GetUndoStack()
AssemblyData138p = Model128p.GetAssemblyData()
ControlData136p = Model128p.GetControlData()
ConnectorData131p = Model128p.GetConnectorData()
MaterialPointManager137p = Model128p.GetMaterialPointData()
Part1p = Model128p.GetPart(1)

params = Prime.GlobalSizingParams()
params.min = 1.07e-05
params.max = 0.001
params.growthRate = 1.2
Model128p.SetGlobalSizingParams(params)

type = Prime.SizingType_Curvature
SizeControl146p = ControlData136p.CreateSizeControl(type)

SizeControl146p.GetSizingType()

params = Prime.CurvatureSizingParams()
params.min = 1.07e-05
params.max = 0.001
params.growthRate = 1.2
params.normalAngle = 18
params.useCadCurvature = True
params.clearCurvatureNoise = False
params.aggressiveCurvatureNoise = False
params.enableGeodesicDiffusion = False
params.noiseGradient = 5
params.useTensorCurvature = False
params.aspectRatioSkewed = 0.1
params.aspectRatioDegenerated = 0.001
SizeControl146p.SetCurvatureSizingParams(params)

scope = Prime.ScopeDefinition()
scope.usePartIfNoLabelsOrZones = True
scope.entityType = Prime.ScopeEntity_EdgeZonelets
scope.evaluationType = Prime.ScopeEvaluationType_IDs
scope.expressionType = Prime.ScopeExpressionType_NamePattern
scope.evaluationOption = Prime.ScopeEvaluationOptions_GeomAndMesh
scope.partExpression.Set("*")
scope.labelExpression.Set("*")
scope.zoneExpression.Set("*")
scope.parts.Set([2])
scope.partFaceZonelets.Set([])
scope.partEdgeZonelets.Set([8 , 10 , 9 , 8 , 7 , 6 , 5 , 4 , 3])
scope.partTopoFaces.Set([])
scope.partTopoEdges.Set([])
scope.partVolumes.Set([])
SizeControl146p.SetScope(scope)

type = Prime.SizingType_Curvature
SizeControl147p = ControlData136p.CreateSizeControl(type)

SizeControl147p.GetSizingType()

params = Prime.CurvatureSizingParams()
params.min = 1.07e-05
params.max = 0.001
params.growthRate = 1.2
params.normalAngle = 18
params.useCadCurvature = True
params.clearCurvatureNoise = False
params.aggressiveCurvatureNoise = False
params.enableGeodesicDiffusion = False
params.noiseGradient = 5
params.useTensorCurvature = False
params.aspectRatioSkewed = 0.1
params.aspectRatioDegenerated = 0.001
SizeControl147p.SetCurvatureSizingParams(params)

scope = Prime.ScopeDefinition()
scope.usePartIfNoLabelsOrZones = True
scope.entityType = Prime.ScopeEntity_FaceZonelets
scope.evaluationType = Prime.ScopeEvaluationType_IDs
scope.expressionType = Prime.ScopeExpressionType_NamePattern
scope.evaluationOption = Prime.ScopeEvaluationOptions_GeomAndMesh
scope.partExpression.Set("*")
scope.labelExpression.Set("*")
scope.zoneExpression.Set("*")
scope.parts.Set([2])
scope.partFaceZonelets.Set([1 , 2])
scope.partEdgeZonelets.Set([])
scope.partTopoFaces.Set([])
scope.partTopoEdges.Set([])
scope.partVolumes.Set([])
SizeControl147p.SetScope(scope)

type = Prime.SizingType_Proximity
SizeControl148p = ControlData136p.CreateSizeControl(type)

SizeControl148p.GetSizingType()

params = Prime.ProximitySizingParams()
params.min = 1.07e-05
params.max = 0.001
params.growthRate = 1.2
params.elementsPerGap = 1
params.ignoreSelfProximity = True
params.ignoreOrientation = False
params.sizingProximityType = Prime.SizingProximityType_FaceFace
params.minRelativeGap = 0.2
SizeControl148p.SetProximitySizingParams(params)

scope = Prime.ScopeDefinition()
scope.usePartIfNoLabelsOrZones = True
scope.entityType = Prime.ScopeEntity_EdgeZonelets
scope.evaluationType = Prime.ScopeEvaluationType_IDs
scope.expressionType = Prime.ScopeExpressionType_NamePattern
scope.evaluationOption = Prime.ScopeEvaluationOptions_GeomAndMesh
scope.partExpression.Set("*")
scope.labelExpression.Set("*")
scope.zoneExpression.Set("*")
scope.parts.Set([2])
scope.partFaceZonelets.Set([])
scope.partEdgeZonelets.Set([8 , 10 , 9 , 8 , 7 , 6 , 5 , 4 , 3])
scope.partTopoFaces.Set([])
scope.partTopoEdges.Set([])
scope.partVolumes.Set([])
SizeControl148p.SetScope(scope)

model = Prime.Model.GetByName("Model128")
SizeField149p = PrimeSizeField.SizeField.New(model)
SizeField149p.Register("SizeField149")

size_control_ids = [2 , 3 , 4 , 5]
volumetric_sizefield_params = PrimeSizeField.VolumetricSizeFieldComputeParams()
volumetric_sizefield_params.enableMultiThreading = False
volumetric_sizefield_params.enablePeriodicity = False
volumetric_sizefield_params.periodicParams = PrimeSizeField.SFPeriodicParams()
volumetric_sizefield_params.periodicParams.axis.Set([])
volumetric_sizefield_params.periodicParams.angle = 0
volumetric_sizefield_params.periodicParams.center.Set([])
SizeField149p.ComputeVolumetric(size_control_ids, volumetric_sizefield_params)

FileIO150p = PrimeIO.FileIO.New(Prime.Model.GetByName("Model128"))
FileIO150p.Register("FileIO150")

file_name = "C:\Users\mtthl\OneDrive\Documents\Education\Masters Thesis\git\APG_tranpsort\Patrick_CFD\Geometry\FM_DESKTOP-1N5CMU3_15948\2D_inletsection.sf"
FileIO150p.ExportFluentMeshingSizeField(file_name)

model = Prime.Model.GetByName("Model128")
part_id = 2
Surfer151p = PrimeSurfer.Surfer.New(model, part_id)
Surfer151p.Register("Surfer151")

Surfer151p.InitializeSurferParams()

topo_faces = [2]
params = PrimeSurfer.SurferParams()
params.minAngle = 40
params.maxAngle = 150
params.cornerAngle = 20
params.sizeFieldType = PrimeSurfer.SizeFieldType_Volumetric
params.directionFieldType = PrimeSurfer.DirectionFieldType_Unknown
params.nRetriesOnFailed = 1
params.improveFailed = True
params.minSize = 1.07e-05
params.maxSize = 0.001
params.growthRate = 1.2
params.frontIntersectionTolerance = 0.2
params.constantSize = -1
params.minSizeDeviation = 0.5
params.maxSizeDeviation = 0.2
params.minTriInnerAngle = 30
params.maxTriInnerAngle = 120
params.minQuadInnerAngle = 30
params.maxQuadInnerAngle = 150
params.maxQuadWarpAngle = 20
params.minimizeNumTriangles = 0
params.improveQuads = 1
params.remeshBlocks = 1
params.maxSurferFaces = 1000000
params.useAdvFrontLocalRecon = False
params.remeshNonmanifoldZonelet = True
params.absoluteDistanceTolerance = 0
params.generateQuads = False
params.cleanupQuads = False
params.generateRightAngleTriangles = False
params.fixedCount = 0
params.minCount = -1
params.maxCount = -1
params.nSmoothingIterations = 5
params.nSwappingIterations = 1
params.preserveFreeBoundary = False
params.preserveSharedBoundary = False
params.unisotropicFront = False
params.edgeBiasingType = PrimeSurfer.EdgeBiasingType_Forward
params.firstSpacing.Set([0.000000 , 0.000000 , 0.000000 , 0.000000])
params.lastSpacing.Set([0.000000 , 0.000000 , 0.000000 , 0.000000])
params.biasGrowthRate.Set([-1.000000 , -1.000000 , -1.000000 , -1.000000])
params.sagControl = False
params.maxSag = 1.000000
params.maxSagAngle = -1.000000
params.sagSmoothing = True
params.preserveHardNodes = False
params.returnRemeshedEdges = False
params.separateSelfIntersections = PrimeSurfer.SepSelfIntersectionType_None
params.updateMidsurfThickness = False
params.improveMethod = PrimeSurfer.ImproveMethodType_Method3
params.alignEdgeMesh = True
params.traceEdges = True
params.checkNonManifolds = False
params.avoidCornerTriangles = False
params.voronoiSeedAngle = 0.500000
params.postImproveExplicitRemeshedPatch = False
params.enableRobustMode = False
params.validateSurferInput = False
params.surferCheckFeatureLoss = False
params.smoothSizeTransition = False
params.advancedSurferSetup = PrimeSurfer.AdvancedSurferSetup_None
params.projectOnGeometry = False
params.enableMultiThreading = True
params.memoryOptimizedMultiThreading = False
params.alignTriEdgeMesh = True
Surfer151p.MeshTopoFaces(topo_faces, params)

ShellBLControl164p = ControlData136p.CreateShellBLControl()

entities = Prime.ScopeDefinition()
entities.usePartIfNoLabelsOrZones = True
entities.entityType = Prime.ScopeEntity_EdgeZonelets
entities.evaluationType = Prime.ScopeEvaluationType_IDs
entities.expressionType = Prime.ScopeExpressionType_NamePattern
entities.evaluationOption = Prime.ScopeEvaluationOptions_GeomAndMesh
entities.partExpression.Set("*")
entities.labelExpression.Set("*")
entities.zoneExpression.Set("*")
entities.parts.Set([2])
entities.partFaceZonelets.Set([])
entities.partEdgeZonelets.Set([5 , 35 , 34 , 33 , 32 , 31])
entities.partTopoFaces.Set([])
entities.partTopoEdges.Set([])
entities.partVolumes.Set([])
ShellBLControl164p.SetEdgeScope(entities)

entities = Prime.ScopeDefinition()
entities.usePartIfNoLabelsOrZones = True
entities.entityType = Prime.ScopeEntity_FaceZonelets
entities.evaluationType = Prime.ScopeEvaluationType_IDs
entities.expressionType = Prime.ScopeExpressionType_NamePattern
entities.evaluationOption = Prime.ScopeEvaluationOptions_GeomAndMesh
entities.partExpression.Set("*")
entities.labelExpression.Set("*")
entities.zoneExpression.Set("*")
entities.parts.Set([2])
entities.partFaceZonelets.Set([1 , 56])
entities.partEdgeZonelets.Set([])
entities.partTopoFaces.Set([])
entities.partTopoEdges.Set([])
entities.partVolumes.Set([])
ShellBLControl164p.SetSurfaceScope(entities)

ShellBLControl164p.InitializeGrowthParams()

shellbl_control_growth_params = Prime.ShellBLControlGrowthParams()
shellbl_control_growth_params.nLayers = 25
shellbl_control_growth_params.offsetType = Prime.ShellBLOffsetType_Uniform
shellbl_control_growth_params.growthRate = 1.200000
shellbl_control_growth_params.gapFactor = 0.200000
shellbl_control_growth_params.firstHeight = 0.000001
shellbl_control_growth_params.maxHeight = 0.012000
shellbl_control_growth_params.firstAspectRatio = 5.000000
shellbl_control_growth_params.lastAspectRatio = 2.500000
shellbl_control_growth_params.minAspectRatio = 0.010000
shellbl_control_growth_params.maxAspectRatio = 100.000000
shellbl_control_growth_params.maxProjectionAngle = 135.000000
shellbl_control_growth_params.exposeSide = True
shellbl_control_growth_params.maxOrthogonalAngleDevation = 60.000000
shellbl_control_growth_params.nOrthogonalLayers = 3
ShellBLControl164p.SetGrowthParams(shellbl_control_growth_params)

ShellBLControl165p = ControlData136p.CreateShellBLControl()

entities = Prime.ScopeDefinition()
entities.usePartIfNoLabelsOrZones = True
entities.entityType = Prime.ScopeEntity_EdgeZonelets
entities.evaluationType = Prime.ScopeEvaluationType_IDs
entities.expressionType = Prime.ScopeExpressionType_NamePattern
entities.evaluationOption = Prime.ScopeEvaluationOptions_GeomAndMesh
entities.partExpression.Set("*")
entities.labelExpression.Set("*")
entities.zoneExpression.Set("*")
entities.parts.Set([2])
entities.partFaceZonelets.Set([])
entities.partEdgeZonelets.Set([6 , 31 , 34 , 33 , 32 , 35 , 37])
entities.partTopoFaces.Set([])
entities.partTopoEdges.Set([])
entities.partVolumes.Set([])
ShellBLControl165p.SetEdgeScope(entities)

entities = Prime.ScopeDefinition()
entities.usePartIfNoLabelsOrZones = True
entities.entityType = Prime.ScopeEntity_FaceZonelets
entities.evaluationType = Prime.ScopeEvaluationType_IDs
entities.expressionType = Prime.ScopeExpressionType_NamePattern
entities.evaluationOption = Prime.ScopeEvaluationOptions_GeomAndMesh
entities.partExpression.Set("*")
entities.labelExpression.Set("*")
entities.zoneExpression.Set("*")
entities.parts.Set([2])
entities.partFaceZonelets.Set([1 , 56])
entities.partEdgeZonelets.Set([])
entities.partTopoFaces.Set([])
entities.partTopoEdges.Set([])
entities.partVolumes.Set([])
ShellBLControl165p.SetSurfaceScope(entities)

ShellBLControl165p.InitializeGrowthParams()

shellbl_control_growth_params = Prime.ShellBLControlGrowthParams()
shellbl_control_growth_params.nLayers = 10
shellbl_control_growth_params.offsetType = Prime.ShellBLOffsetType_Uniform
shellbl_control_growth_params.growthRate = 1.200000
shellbl_control_growth_params.gapFactor = 0.200000
shellbl_control_growth_params.firstHeight = 0.000001
shellbl_control_growth_params.maxHeight = 0.009600
shellbl_control_growth_params.firstAspectRatio = 5.000000
shellbl_control_growth_params.lastAspectRatio = 2.500000
shellbl_control_growth_params.minAspectRatio = 0.010000
shellbl_control_growth_params.maxAspectRatio = 100.000000
shellbl_control_growth_params.maxProjectionAngle = 135.000000
shellbl_control_growth_params.exposeSide = True
shellbl_control_growth_params.maxOrthogonalAngleDevation = 60.000000
shellbl_control_growth_params.nOrthogonalLayers = 3
ShellBLControl165p.SetGrowthParams(shellbl_control_growth_params)

model = Prime.Model.GetByName("Model128")
part_id = 2
Surfer166p = PrimeSurfer.Surfer.New(model, part_id)
Surfer166p.Register("Surfer166")

part_id = 2
shellbl_control_ids = [6 , 7]
shellbl_params = PrimeSurfer.ShellBLParams()
shellbl_params.localRemeshTarget = True
shellbl_params.localRemeshAdjacent = True
shellbl_params.remeshGrowthRate = 1.200000
shellbl_params.refineStretchedQuads = False
shellbl_params.splitQuads = False
shellbl_params.maxFaceSkew = 0.900000
shellbl_params.projectOnGeometry_Beta = False
shellbl_params.projectionMethod = PrimeSurfer.ShellBLProjectionMethod_Post
shellbl_params.stairstepGradient = 1
shellbl_params.enableMultiThreading = False
shellbl_params.adjacentSideHeightFactor = 3.000000
shellbl_params.maxFaceSkewnessForTri = 0.900000
shellbl_params.minWidthBaseRatioForQuad = 0.200000
Surfer166p.CreateShellBLUsingControls(part_id, shellbl_control_ids, shellbl_params)

model = Prime.Model.GetByName("Model128")
SurfaceSearch167p = PrimeSurfaceTools.SurfaceSearch.New(model)
SurfaceSearch167p.Register("SurfaceSearch167")

part_id = 2
face_zonelets = [56]
register_id = 28
params = PrimeSurfaceTools.SearchByQualityParams()
params.qualityLimit = 0.000000
params.faceQualityMeasure = PrimeSurfaceTools.FaceQualityMeasure_Skewness
params.generateTraversalClusters = False
SurfaceSearch167p.SearchZoneletsByQuality(part_id, face_zonelets, register_id, params)

model = Prime.Model.GetByName("Model128")
part_id = 2
Surfer168p = PrimeSurfer.Surfer.New(model, part_id)
Surfer168p.Register("Surfer168")

Surfer168p.InitializeLocalSurferParams()

topo_faces = [2]
register_id = 28
local_surfer_params = PrimeSurfer.LocalSurferParams()
local_surfer_params.minAngle = 40.000000
local_surfer_params.maxAngle = 179.500000
local_surfer_params.cornerAngle = 20.000000
local_surfer_params.sizeFieldType = PrimeSurfer.SizeFieldType_Volumetric
local_surfer_params.minSize = 0.000001
local_surfer_params.maxSize = 0.001000
local_surfer_params.growthRate = 1.200000
local_surfer_params.constantSize = 0.001000
local_surfer_params.freezeQuads = True
local_surfer_params.freezeSharedZoneletBoundary = False
local_surfer_params.smoothBoundary = False
local_surfer_params.nRings = 4
local_surfer_params.generateQuads = True
local_surfer_params.nSmoothingIterations = 5
local_surfer_params.nSwappingIterations = 1
local_surfer_params.smoothSizeTransition = True
local_surfer_params.projectOnGeometry = False
Surfer168p.MeshTopoFacesLocally(topo_faces, register_id, local_surfer_params)

params = Prime.DeleteTopoEntitiesParams()
params.deleteGeomZonelets = False
params.deleteMeshZonelets = False
Part140p.DeleteTopoEntities(params)

graphics = PrimeApp.Graphics.Get()
graphics.UseModel(model)
