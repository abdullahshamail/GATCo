import numpy as np

from utils import polymer_surface_plane, perpendicular_distance

polymer_atoms_1 =  np.loadtxt(r"C:\Users\mhanowar\Downloads\nitrogen 0-800k\nitrogen200k-0.txt")
polymer_atoms_2 =  np.loadtxt(r"C:\Users\mhanowar\Downloads\nitrogen 0-800k\nitrogen200k-0.txt")

polymer_atoms = np.concatenate((polymer_atoms_1 , polymer_atoms_2), axis = 0)

polymer_atoms = polymer_atoms.reshape(polymer_atoms.shape[0], polymer_atoms.shape[1] // 3 , 3)

center_of_mass_traj = np.loadtxt(r"C:\Users\mhanowar\Downloads\RFL1_Center of Mass trajectory_0-200K.txt", delimiter=",")

center_of_mass_traj = center_of_mass_traj.reshape(center_of_mass_traj.shape[0], center_of_mass_traj.shape[1] // 3 , 3)


# Total time frame = 200,000

init_frame = 0
final_frame = 200000
total_frame = np.arange(init_frame, final_frame, dtype=int)

polymer_plane_constant = polymer_surface_plane (polymer_atoms)

perpendicular_distance = perpendicular_distance (center_of_mass_traj, total_frame, polymer_plane_constant)

# perpendicular_threshold is selected -5 A below polymer plane surface to 5 A above

for perpendicular_threshold in np.arange (-5, 5):
    
    timeframes = total_frame [perpendicular_distance < perpendicular_threshold]
    
    np.savetxt(r"C:\Users\mhanowar\Desktop\molecules closer than %dA to plane.csv"%perpendicular_threshold, timeframes, delimiter=",")
    