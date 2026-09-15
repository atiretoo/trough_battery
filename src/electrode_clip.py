import cadquery as cq
import os

def create_clip():
    length = 90.0
    
    # We will draw the profile on the XY plane and extrude along the Z axis.
    # X will be the width across the wall, Y will be the height.
    # Z=0 is the bottom of the legs (near electrolyte)
    # Z=4 is the inner top of the U (rests on the wall)
    # Z=6 is the outer top of the clip
    
    pts = [
        (1.7, 0.0),    # Outer bottom right
        (2.6, 6.0),    # Outer top right
        (-2.6, 6.0),   # Outer top left
        (-1.7, 0.0),   # Outer bottom left
        (-0.9, 0.0),   # Inner bottom left (gap = 1.8mm -> x=0.9)
        (-1.5, 4.0),   # Inner top left (gap = 3.0mm -> x=1.5)
        (1.5, 4.0),    # Inner top right
        (0.9, 0.0)     # Inner bottom right
    ]
    
    clip = (
        cq.Workplane("XY")
        .polyline(pts)
        .close()
        .extrude(length)
    )
    
    # Chamfer the inner bottom corners to help it slide onto the metal plates
    clip = clip.edges(cq.selectors.NearestToPointSelector((0.9, 0.0, length/2))).chamfer(0.3)
    clip = clip.edges(cq.selectors.NearestToPointSelector((-0.9, 0.0, length/2))).chamfer(0.3)
    
    # Chamfer the outer top corners for a finished look
    clip = clip.edges(cq.selectors.NearestToPointSelector((2.6, 6.0, length/2))).chamfer(0.5)
    clip = clip.edges(cq.selectors.NearestToPointSelector((-2.6, 6.0, length/2))).chamfer(0.5)

    return clip

if __name__ == "__main__":
    print("Generating electrode clip model...")
    clip = create_clip()
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    stl_dir = os.path.join(base_dir, "exports", "stl")
    step_dir = os.path.join(base_dir, "exports", "step")
    
    os.makedirs(stl_dir, exist_ok=True)
    os.makedirs(step_dir, exist_ok=True)
    
    cq.exporters.export(clip, os.path.join(stl_dir, "electrode_clip.stl"))
    cq.exporters.export(clip, os.path.join(step_dir, "electrode_clip.step"))
    print("Export complete.")
