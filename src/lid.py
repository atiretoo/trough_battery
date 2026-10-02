import cadquery as cq
import os
import math

def create_lid():
    # Box outer dimensions: 93.6 L x 105.5 W
    outer_length = 93.6
    outer_width = 105.5
    
    lid_thickness = 2.0
    inset_depth = 2.5      # Total depth into the 5.0 mm top freeboard
    band_height = 0.50     # 2 layers @ 0.25 mm: straight collar at nominal zero clearance
    taper_height = inset_depth - band_height # 2.0 mm: tapered lead-in
    clearance_tip = 0.15   # 0.15 mm clearance per side at bottom tip (86.9 x 97.2 mm)
    
    # Box inner dimensions: 87.2 L x 97.5 W
    inner_length = 87.2
    inner_width = 97.5
    
    # Calculate draft angle so taper narrows from collar (87.2 x 97.5) down to tip (86.9 x 97.2)
    draft_angle = math.degrees(math.atan(clearance_tip / taper_height)) # ~4.29°
    
    lid = (
        cq.Workplane("XY")
        .box(outer_length, outer_width, lid_thickness)
        .edges("|Z")
        .fillet(2.5)
    )
    
    # 1. Straight collar at nominal zero clearance for top 2 layers (0.5 mm)
    lid = (
        lid.faces("<Z")
        .workplane()
        .rect(inner_length, inner_width)
        .extrude(band_height)
    )
    
    # 2. Tapered plug below collar narrowing down to 0.15 mm clearance at tip
    lid = (
        lid.faces("<Z")
        .workplane()
        .rect(inner_length, inner_width)
        .extrude(taper_height, taper=draft_angle)
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
