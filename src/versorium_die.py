import cadquery as cq
import os

def create_die():
    # --- Parameters ---
    # Base Block (Bottom mold)
    base_length = 114.0
    base_width = 16.0
    base_height = 10.0
    
    # Pocket in Base Block (for perfect alignment of the press)
    # Provides 0.25mm clearance all around so the press block slides in easily
    pocket_length = 110.5
    pocket_width = 12.5
    pocket_depth = 5.0
    
    # Press Block (Top mold)
    press_length = 110.0
    press_width = 12.0
    press_height = 5.0  # Just the main rectangular body thickness
    
    # V-Groove & Ridge (90 degree V, wide enough for a 3mm strip to fold)
    v_width = 8.0
    v_depth = 4.0
    
    # Dimple & Hole for the versorium pivot cup
    hole_diam = 0.8
    hole_depth = 0.56 # 2 layers of 0.28mm
    
    dimple_diam = 0.6
    dimple_length = 0.4 # Sticks out 0.4mm from the V tip
    
    # --- 1. Base Block ---
    # Flat on the bed (Z=0). Pocket and V-groove face UP.
    base = (
        cq.Workplane("XY")
        .box(base_length, base_width, base_height)
        .translate((0, 0, base_height / 2))
    )
    
    # Pocket cut
    pocket_z_center = base_height - (pocket_depth / 2) # Z = 7.5
    pocket = (
        cq.Workplane("XY")
        .box(pocket_length, pocket_width, pocket_depth)
        .translate((0, 0, pocket_z_center))
    )
    base = base.cut(pocket)
    
    # V-groove cut (Pocket floor is Z=5.0, goes down to Z=1.0)
    v_groove_pts = [(0, 1.0), (-v_width/2, 5.0), (v_width/2, 5.0)]
    v_groove = (
        cq.Workplane("YZ")
        .polyline(v_groove_pts).close()
        .extrude(pocket_length, both=True)
    )
    base = base.cut(v_groove)
    
    # Hole cut at the bottom of the V (Center X=0, Y=0)
    # Bottom of V is Z=1.0, hole goes down to Z=0.44
    hole_z_center = 0.44 + 1.0 # 1.44 (using a 2.0 tall cylinder)
    hole_cutout = (
        cq.Workplane("XY")
        .cylinder(2.0, hole_diam / 2)
        .translate((0, 0, hole_z_center))
    )
    base = base.cut(hole_cutout)
    
    # --- 2. Press Block ---
    # Flat on the bed (Z=0). V-ridge faces UP for easy printing.
    press = (
        cq.Workplane("XY")
        .box(press_length, press_width, press_height)
        .translate((0, 0, press_height / 2))
    )
    
    # V-ridge (Sits on the main body at Z=5.0, goes up to Z=9.0)
    v_ridge_pts = [(0, 9.0), (-v_width/2, 5.0), (v_width/2, 5.0)]
    v_ridge = (
        cq.Workplane("YZ")
        .polyline(v_ridge_pts).close()
        .extrude(press_length / 2, both=True)
    )
    press = press.union(v_ridge)
    
    # Dimple (Sphere sticking out 0.4mm from Z=9.0)
    # Using a sphere creates a much better pivot cup than a flat cylinder!
    dimple_z_center = 9.0 + dimple_length - (dimple_diam / 2) # 9.1
    dimple_solid = (
        cq.Workplane("XY")
        .sphere(dimple_diam / 2)
        .translate((0, 0, dimple_z_center))
    )
    press = press.union(dimple_solid)
    
    return base, press

if __name__ == "__main__":
    print("Generating versorium die press models...")
    base, press = create_die()
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    stl_dir = os.path.join(base_dir, "exports", "stl")
    step_dir = os.path.join(base_dir, "exports", "step")
    
    os.makedirs(stl_dir, exist_ok=True)
    os.makedirs(step_dir, exist_ok=True)
    
    # Exporting
    cq.exporters.export(base, os.path.join(stl_dir, "versorium_die_base.stl"))
    cq.exporters.export(press, os.path.join(stl_dir, "versorium_die_press.stl"))
    
    cq.exporters.export(base, os.path.join(step_dir, "versorium_die_base.step"))
    cq.exporters.export(press, os.path.join(step_dir, "versorium_die_press.step"))
    print("Export complete.")
