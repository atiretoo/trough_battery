import cadquery as cq
import math
import os

def regular_polygon_vertices(n_sides, flat_to_flat_width):
    """
    Returns (x, y) 2D vertices for a regular polygon with n_sides
    specified by its flat-to-flat distance (inradius * 2).
    Oriented so a flat edge is perpendicular to the X-axis (or centered).
    """
    r_in = flat_to_flat_width / 2.0
    r_out = r_in / math.cos(math.pi / n_sides)
    
    vertices = []
    # Rotate by half the step angle so flats are aligned with cardinal axes
    angle_offset = math.pi / n_sides
    for i in range(n_sides):
        angle = 2.0 * math.pi * i / n_sides + angle_offset
        x = r_out * math.cos(angle)
        y = r_out * math.sin(angle)
        vertices.append((x, y))
    return vertices

def create_versorium_stand():
    # --- Dimensions (Inches to mm) ---
    tier1_width = 3.5 * 25.4      # 88.9 mm (across flats)
    tier1_height = 0.75 * 25.4    # 19.05 mm
    tier1_chamfer = 3.5           # mm
    
    tier2_width = 2.5 * 25.4      # 63.5 mm (across flats)
    tier2_height = 0.75 * 25.4    # 19.05 mm
    tier2_chamfer = 3.0           # mm
    tier2_rotation = 22.5         # degrees relative to tier 1
    
    pillar_height = 2.5 * 25.4    # 63.5 mm (1:1 with middle tier width)
    pillar_base_width = 0.5 * 25.4  # 12.7 mm (1/2")
    pillar_top_width = 0.25 * 25.4  # 6.35 mm (1/4")
    pillar_rotation = 0.0         # aligned with tier 1 (or 22.5)
    
    needle_hole_diam = 1.2        # mm (for 1.15mm wire)
    needle_hole_depth = 15.0      # mm deep
    
    # 1. Tier 1 (Bottom Octagonal Base)
    t1_verts = regular_polygon_vertices(8, tier1_width)
    tier1 = (
        cq.Workplane("XY")
        .polyline(t1_verts)
        .close()
        .extrude(tier1_height)
    )
    # Apply chamfer to top outer edges of Tier 1
    tier1 = tier1.faces(">Z").edges().chamfer(tier1_chamfer)
    
    # 2. Tier 2 (Middle Octagonal Base)
    t2_verts = regular_polygon_vertices(8, tier2_width)
    tier2 = (
        cq.Workplane("XY")
        .workplane(offset=tier1_height)
        .transformed(rotate=(0, 0, tier2_rotation))
        .polyline(t2_verts)
        .close()
        .extrude(tier2_height)
    )
    # Apply chamfer to top outer edges of Tier 2
    tier2 = tier2.faces(">Z").edges().chamfer(tier2_chamfer)
    
    # 3. Tapered Octagonal Pillar (Loft from base polygon to top polygon)
    p_base_verts = regular_polygon_vertices(8, pillar_base_width)
    p_top_verts = regular_polygon_vertices(8, pillar_top_width)
    
    z_pillar_base = tier1_height + tier2_height
    z_pillar_top = z_pillar_base + pillar_height
    
    pillar = (
        cq.Workplane("XY")
        .workplane(offset=z_pillar_base)
        .transformed(rotate=(0, 0, pillar_rotation))
        .polyline(p_base_verts)
        .close()
        .workplane(offset=pillar_height)
        .polyline(p_top_verts)
        .close()
        .loft(combine=True)
    )
    
    # Combine the three wood parts into a single solid base
    stand = tier1.union(tier2).union(pillar)
    
    # 4. Needle Hole drilled along central Z axis at top of pillar
    needle_hole = (
        cq.Workplane("XY")
        .workplane(offset=z_pillar_top - needle_hole_depth)
        .circle(needle_hole_diam / 2.0)
        .extrude(needle_hole_depth + 1.0) # cut through the top face cleanly
    )
    stand = stand.cut(needle_hole)
    
    return stand

if __name__ == "__main__":
    print("Generating Elizabethan Versorium Stand...")
    stand = create_versorium_stand()
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    stl_dir = os.path.join(base_dir, "exports", "stl")
    step_dir = os.path.join(base_dir, "exports", "step")
    
    os.makedirs(stl_dir, exist_ok=True)
    os.makedirs(step_dir, exist_ok=True)
    
    stl_path = os.path.join(stl_dir, "versorium_stand.stl")
    step_path = os.path.join(step_dir, "versorium_stand.step")
    
    cq.exporters.export(stand, stl_path)
    cq.exporters.export(stand, step_path)
    print(f"Exported STL: {stl_path}")
    print(f"Exported STEP: {step_path}")
