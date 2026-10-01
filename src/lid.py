import cadquery as cq
import os
import math

def create_lid():
    # Box outer dimensions: 93.6 L x 105.5 W
    outer_length = 93.6
    outer_width = 105.5
    
    lid_thickness = 2.0
    inset_depth = 2.5      # Engages 2.5 mm into the 5.0 mm top freeboard
    clearance_tip = 0.15   # 0.15 mm clearance per side at bottom tip (86.9 x 97.2 mm)
    
    # Box inner dimensions: 87.2 L x 97.5 W
    inner_length = 87.2
    inner_width = 97.5
    
    # Calculate draft angle so inset flares out from tip (86.9 x 97.2) to shoulder (87.2 x 97.5)
    draft_angle = math.degrees(math.atan(clearance_tip / inset_depth)) # ~3.43°
    
    lid = (
        cq.Workplane("XY")
        .box(outer_length, outer_width, lid_thickness)
        .edges("|Z")
        .fillet(2.5)
    )
    
    # Extrude tapered inset plug from shoulder (87.2 x 97.5) narrowing down to tip (86.9 x 97.2)
    lid = (
        lid.faces("<Z")
        .workplane()
        .rect(inner_length, inner_width)
        .extrude(inset_depth, taper=draft_angle)
    )
    
    slit_width_y = 20.0  # Reduced to center 20 mm to preserve end walls of inset and stop end-to-end slop
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
