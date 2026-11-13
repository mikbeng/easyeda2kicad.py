"""EasyEDA layer 99 (component body outline) becomes an F.Fab outline, not a courtyard."""

from easyeda2kicad.easyeda.parameters_easyeda import EeFootprintSolidRegion
from easyeda2kicad.kicad.export_kicad_footprint import _convert_solid_region
from easyeda2kicad.kicad.parameters_kicad_footprint import KI_LAYERS


def test_layer_99_maps_to_fab():
    assert KI_LAYERS[99] == "F.Fab"


def test_layer_99_region_is_an_unfilled_fab_outline():
    region = EeFootprintSolidRegion(layer_id=99, path="M 0 0 L 10 0 L 10 10 L 0 10 Z", region_type="solid")
    ki = _convert_solid_region(region, 0, 0)
    assert ki is not None
    assert ki.layer == "F.Fab"
    assert ki.outline_only


def test_assembly_layer_region_stays_filled():
    region = EeFootprintSolidRegion(layer_id=13, path="M 0 0 L 10 0 L 10 10 L 0 10 Z", region_type="solid")
    ki = _convert_solid_region(region, 0, 0)
    assert ki.layer == "F.Fab"
    assert not ki.outline_only
