import cadquery as cq
import os

def create_trough_battery():
    num_cells = 4
    
    inner_width = 97.5          
    
    groove_depth_sides = 2.0    
    groove_depth_bottom = 2.0   
    groove_thickness = 0.5      
    
    # Wall and floor dimensions optimized for 0.4 mm nozzle and 0.25 mm layer height
    floor_thickness = 4.0               # 16 layers @ 0.25 mm (leaves 2.0 mm under groove)
    side_wall_thickness = 4.0           # 10 perimeters @ 0.4 mm (leaves 2.0 mm behind groove)
    end_wall_thickness = 3.2            # 8 perimeters @ 0.4 mm (smallest multiple >= 3.0 mm)
    internal_wall_thickness = 2.4       # 6 perimeters @ 0.4 mm (smallest even multiple >= 2.0 mm)
    
    internal_wall_height = 102.0 
    top_cut_height = 5.0                # 5.0 mm clearance/freeboard below top rim
    box_height = floor_thickness + internal_wall_height + top_cut_height # 111.0 mm
    cell_length = 20.0          
    
    # Electrolyte fill line ridge parameters
    electrolyte_level = 98.0
    ridge_z_top = floor_thickness + electrolyte_level # 102.0
    ridge_width = 0.4       # 1 perimeter line width
    ridge_height = 1.12     # 4 layers of 0.28mm
    ridge_length = 10.0
    ridge_embed = 0.1       # embed slightly into wall for clean boolean union
    
    # --- Derived Dimensions ---
    groove_cut_width = inner_width + (2 * groove_depth_sides)  # 101.5 mm
    outer_width = inner_width + (2 * side_wall_thickness)      # 105.5 mm
    
    inner_length = (num_cells * cell_length) + ((num_cells - 1) * internal_wall_thickness) # 87.2 mm
    outer_length = inner_length + (2 * end_wall_thickness)     # 93.6 mm
    
    # 1. Base solid block with outside vertical and build-plate fillets
    trough = (
        cq.Workplane("XY")
        .box(outer_length, outer_width, box_height)
        .translate((0, 0, box_height / 2))
        .edges("|Z or <Z")
        .fillet(2.5)
    )
    
    # 2. Top Cutout (freeboard)
    top_cut_z_center = box_height - (top_cut_height / 2) # 108.5
    
    top_cutout = (
        cq.Workplane("XY")
        .box(inner_length, inner_width, top_cut_height)
        .translate((0, 0, top_cut_z_center))
    )
    trough = trough.cut(top_cutout)
    
    # 3. Cells and grooves
    start_x = -inner_length / 2 
    
    for i in range(num_cells):
        cell_x_start = start_x + i * (cell_length + internal_wall_thickness)
        cell_center_x = cell_x_start + cell_length / 2
        
        # Cell inner cavity
        cell_z_center = floor_thickness + (internal_wall_height / 2)
        cell_cutout = (
            cq.Workplane("XY")
            .box(cell_length, inner_width, internal_wall_height)
            .translate((cell_center_x, 0, cell_z_center))
        )
        trough = trough.cut(cell_cutout)
        
        # Grooves
        groove_cut_height = box_height - (floor_thickness - groove_depth_bottom)
        groove_z_center = (floor_thickness - groove_depth_bottom) + (groove_cut_height / 2)
        
        left_groove_x = cell_x_start + (groove_thickness / 2)
        left_groove = (
            cq.Workplane("XY")
            .box(groove_thickness, groove_cut_width, groove_cut_height)
            .translate((left_groove_x, 0, groove_z_center))
        )
        
        right_groove_x = cell_x_start + cell_length - (groove_thickness / 2)
        right_groove = (
            cq.Workplane("XY")
            .box(groove_thickness, groove_cut_width, groove_cut_height)
            .translate((right_groove_x, 0, groove_z_center))
        )
        
        trough = trough.cut(left_groove).cut(right_groove)
        
        # Electrolyte Level Ridges (10mm long, centered)
        # Right wall ridge (Y > 0)
        right_ridge_pts = [
            (ridge_embed, 0), 
            (-ridge_width, 0), 
            (0, -ridge_height), 
            (ridge_embed, -ridge_height)
        ]
        right_ridge = (
            cq.Workplane("YZ")
            .polyline(right_ridge_pts).close()
            .extrude(ridge_length / 2, both=True)
            .translate((cell_center_x, inner_width / 2, ridge_z_top))
        )
        
        # Left wall ridge (Y < 0)
        left_ridge_pts = [
            (-ridge_embed, 0), 
            (ridge_width, 0), 
            (0, -ridge_height), 
            (-ridge_embed, -ridge_height)
        ]
        left_ridge = (
            cq.Workplane("YZ")
            .polyline(left_ridge_pts).close()
            .extrude(ridge_length / 2, both=True)
            .translate((cell_center_x, -inner_width / 2, ridge_z_top))
        )
        
        trough = trough.union(right_ridge).union(left_ridge)
        
    # 4. Fold Clearance Notches
    notch_length = internal_wall_thickness + (2 * groove_thickness) + 1.0 # 4.4 mm
    
    for i in range(1, num_cells):
        wall_x_center = start_x + i * (cell_length + internal_wall_thickness) - (internal_wall_thickness / 2)
        
        notch_cutout = (
            cq.Workplane("XY")
            .box(notch_length, groove_cut_width, top_cut_height)
            .translate((wall_x_center, 0, top_cut_z_center))
        )
        trough = trough.cut(notch_cutout)
        
    return trough

if __name__ == "__main__":
    print("Generating the historical 4-cell trough battery model...")
    battery = create_trough_battery()
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    stl_dir = os.path.join(base_dir, "exports", "stl")
    step_dir = os.path.join(base_dir, "exports", "step")
    
    cq.exporters.export(battery, os.path.join(stl_dir, "trough_battery_4_cell.stl"))
    cq.exporters.export(battery, os.path.join(step_dir, "trough_battery_4_cell.step"))
    print("Export complete.")
