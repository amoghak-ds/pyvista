"""Utilities routines."""
# flake8: noqa: F401

from .arrays import (
    FieldAssociation,
    array_from_vtkmatrix,
    cell_array,
    convert_array,
    convert_string_array,
    field_array,
    get_array,
    get_array_association,
    get_vtk_type,
    parse_field_choice,
    point_array,
    raise_has_duplicates,
    raise_not_matching,
    row_array,
    set_default_active_scalars,
    set_default_active_vectors,
    vtk_bit_array_to_char,
    vtk_id_list_to_array,
    vtkmatrix_from_array,
)
from .cells import create_mixed_cells, get_mixed_cells, ncells_from_cells, numpy_to_idarr
from .features import (
    cartesian_to_spherical,
    create_grid,
    grid_from_sph_coords,
    merge,
    perlin_noise,
    sample_function,
    spherical_to_cartesian,
    transform_vectors_sph_to_cart,
    voxelize,
)
from .fileio import (
    from_meshio,
    get_ext,
    is_meshio_mesh,
    read,
    read_exodus,
    read_legacy,
    read_meshio,
    read_plot3d,
    read_texture,
    save_meshio,
    set_pickle_format,
    set_vtkwriter_mode,
)
from .geometric_objects import (
    NORMALS,
    Arrow,
    Box,
    Circle,
    CircularArc,
    CircularArcFromNormal,
    Cone,
    Cube,
    Cylinder,
    CylinderStructured,
    Disc,
    Dodecahedron,
    Ellipse,
    Icosahedron,
    Icosphere,
    Line,
    MultipleLines,
    Octahedron,
    Plane,
    PlatonicSolid,
    Polygon,
    Pyramid,
    Quadrilateral,
    Rectangle,
    Sphere,
    Superquadric,
    Tetrahedron,
    Text3D,
    Triangle,
    Tube,
    Wavelet,
    translate,
)
from .geometric_sources import ConeSource, CylinderSource, MultipleLinesSource
from .helpers import axis_rotation, generate_plane, is_inside_bounds, is_pyvista_dataset, wrap
from .misc import (
    AnnotatedIntEnum,
    abstract_class,
    assert_empty_kwargs,
    check_valid_vector,
    conditional_decorator,
    has_module,
    threaded,
    try_callback,
)
from .observers import (
    Observer,
    ProgressMonitor,
    VtkErrorCatcher,
    send_errors_to_logging,
    set_error_output_file,
)
from .parametric_objects import (
    KochanekSpline,
    ParametricBohemianDome,
    ParametricBour,
    ParametricBoy,
    ParametricCatalanMinimal,
    ParametricConicSpiral,
    ParametricCrossCap,
    ParametricDini,
    ParametricEllipsoid,
    ParametricEnneper,
    ParametricFigure8Klein,
    ParametricHenneberg,
    ParametricKlein,
    ParametricKuen,
    ParametricMobius,
    ParametricPluckerConoid,
    ParametricPseudosphere,
    ParametricRandomHills,
    ParametricRoman,
    ParametricSuperEllipsoid,
    ParametricSuperToroid,
    ParametricTorus,
    Spline,
    parametric_keywords,
    surface_from_para,
)
from .points import (
    fit_plane_to_points,
    line_segments_from_points,
    lines_from_points,
    make_tri_mesh,
    vector_poly_data,
    vtk_points,
)
from .reader import (
    AVSucdReader,
    BaseReader,
    BinaryMarchingCubesReader,
    BMPReader,
    BYUReader,
    CGNSReader,
    DEMReader,
    DICOMReader,
    EnSightReader,
    FacetReader,
    FluentReader,
    GIFReader,
    GLTFReader,
    HDFReader,
    HDRReader,
    JPEGReader,
    MetaImageReader,
    MFIXReader,
    MultiBlockPlot3DReader,
    NIFTIReader,
    NRRDReader,
    OBJReader,
    OpenFOAMReader,
    Plot3DFunctionEnum,
    Plot3DMetaReader,
    PLYReader,
    PNGReader,
    PNMReader,
    PointCellDataSelection,
    POpenFOAMReader,
    PTSReader,
    PVDDataSet,
    PVDReader,
    SegYReader,
    SLCReader,
    STLReader,
    TecplotReader,
    TIFFReader,
    TimeReader,
    VTKDataSetReader,
    VTKPDataSetReader,
    XdmfReader,
    XMLImageDataReader,
    XMLMultiBlockDataReader,
    XMLPImageDataReader,
    XMLPolyDataReader,
    XMLPRectilinearGridReader,
    XMLPUnstructuredGridReader,
    XMLRectilinearGridReader,
    XMLStructuredGridReader,
    XMLUnstructuredGridReader,
    get_reader,
)
