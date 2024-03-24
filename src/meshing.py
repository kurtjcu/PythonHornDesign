# Import modules:
import gmsh


def join_coords_to_lines(coords, lc=1e-2):
    points = []
    lines = []
    print(f"num coords: {len(coords)}")
    for coord in coords:
        points.append(gmsh.model.geo.addPoint(coord[0], coord[1], coord[2], lc))
    for i in range(len(points) - 1):
        lines.append(gmsh.model.geo.addLine(points[i], points[i + 1]))
    return {"points": points, "lines": lines}


def create_mesh_from_sections(horn_sections):
    gmsh.initialize()
    lc = 0
    mesh_sections = {}
    num_layers = len(horn_sections)

    # create sections
    for i, section in enumerate(horn_sections):
        # Create points in each section and then create lines from them
        mesh_sections[f"layer_{i}"] = join_coords_to_lines(section, lc)
        print(f"layer_{i} num points: {mesh_sections[f'layer_{i}']['points']}")
        
        # create spine lines for loop generation
        if i > 0:
            mesh_sections[f"spine_lines_layer{i-1}"] = []
            for j, point in enumerate(mesh_sections[f"layer_{i-1}"]["points"]):
                mesh_sections[f"spine_lines_layer{i-1}"].append(
                    gmsh.model.geo.addLine(
                        point, mesh_sections[f"layer_{i}"]["points"][j]
                    )
                )

    # Create the surface loops 
    face_loops = []
    for i in range(num_layers - 1):
        for j in range(len(mesh_sections[f"layer_{i}"]["lines"])):
            print(f" i = {i}, j = {j}")
            l1 = mesh_sections[f"layer_{i}"]["lines"][j]
            l2 = mesh_sections[f"spine_lines_layer{i}"][j + 1]
            l3 = -mesh_sections[f"layer_{i + 1}"]["lines"][j]
            l4 = -mesh_sections[f"spine_lines_layer{i}"][j]
            # print(f"l1: {l1}, l2: {l2}, l3: {l3}, l4: {l4}")
            face_loops.append(gmsh.model.geo.addCurveLoop([l1, l2, l3, l4]))
    
    # Create planar surfaces        
    for loop in face_loops:
        gmsh.model.geo.addPlaneSurface([loop])
        
    # Create the relevant Gmsh data structures
    # from Gmsh model.
    gmsh.model.geo.synchronize()

    # Generate mesh:
    gmsh.model.mesh.generate()
    # Write mesh data:
    gmsh.write("GFG.msh")

    gmsh.fltk.run()
    gmsh.finalize()

    return None


def main():
    # Initialize gmsh:
    gmsh.initialize()
    # Add your code here


if __name__ == "__main__":
    main()
