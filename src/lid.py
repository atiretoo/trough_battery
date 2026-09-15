import cadquery as cq
import os

def create_lid():
    outer_length = 92.0
    outer_width = 103.5 # Updated outer width based on 97.5mm inner width
    
    lid_thickness = 2.0
    inset_depth = 1.0
    
    # Inset dims (0.5 mm gap on all sides)
    # Box inner dimensions: 86.0 L x 97.5 W
    inset_length = 85.0
    inset_width = 96.5
    
    lid = cq.Workplane("XY").box(outer_length, outer_width, lid_thickness)
    
    lid = (
        lid.faces("<Z")
        .workplane()
        .rect(inset_length, inset_width)
        .extrude(inset_depth)
    )
    
    slit_width_y = 101.5 # Updated to match 101.5mm groove width
    slit_thickness_x = 1.0
    
    lid = (
        lid.faces(">Z")
        .workplane()
        .pushPoints([(-42.75, 0), (42.75, 0)])
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
