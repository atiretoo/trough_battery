import cadquery as cq
import os

def create_lid():
    # Box outer dimensions: 93.6 L x 105.5 W
    outer_length = 93.6
    outer_width = 105.5
    
    lid_thickness = 2.0
    inset_depth = 1.0
    
    # Inset dims (0.5 mm gap on all sides)
    # Box inner dimensions: 87.2 L x 97.5 W
    inset_length = 86.2
    inset_width = 96.5
    
    lid = (
        cq.Workplane("XY")
        .box(outer_length, outer_width, lid_thickness)
        .edges("|Z")
        .fillet(2.5)
    )
    
    lid = (
        lid.faces("<Z")
        .workplane()
        .rect(inset_length, inset_width)
        .extrude(inset_depth)
    )
    
    slit_width_y = 101.5 # Matches 101.5mm groove width
    slit_thickness_x = 1.0
    
    # Slit centers aligned with outer electrode grooves at +/- 43.35 mm
    lid = (
        lid.faces(">Z")
        .workplane()
        .pushPoints([(-43.35, 0), (43.35, 0)])
        .rect(slit_thickness_x, slit_width_y)
        .cutThruAll()
    )
    
    return lid

if __name__ == "__main__":
    lid = create_lid()
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    stl_dir = os.path.join(base_dir, "exports", "stl")
    step_dir = os.path.join(base_dir, "exports", "step")
    
    cq.exporters.export(lid, os.path.join(stl_dir, "lid.stl"))
    cq.exporters.export(lid, os.path.join(step_dir, "lid.step"))
