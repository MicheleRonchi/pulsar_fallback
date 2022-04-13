import numpy as np

# Unit conversions.

KPC_TO_PC = 1000.	# Convert from [kpc] to [pc].
KPC_TO_KM = 3.08567758e16  # Convert from [kpc] to [km].
KPC_TO_CM = 3.08567758e21  # Convert from [kpc] to [cm].
YR_TO_S = 3600 * 24 * 365  # Convert from [yr] to [s].
DEG_TO_MAS = 3600000  # Convert [deg] to [mas].
DEG_TO_RAD = np.pi/180  # Convert [deg] to [rad].
MJY_TO_ERG = 1.e-26 # Convert [mJy] to [erg cm^-2 s^-1 Hz^-1].
JY_TO_ERG = 1.e-23 # Convert [Jy] to [erg cm^-2 s^-1 Hz^-1].

# Physical constants.

M_SUN = 2.0e33  # Sun mass [g].
G = 6.67e-8  # Gravitational constant [cm^3 g^-1 s^-2].
G_KPC_YR = G / (KPC_TO_CM ** 3) * YR_TO_S ** 2	# Gravitational constant [kpc^3 g^-1 yr^-2].
C = 2.99792458e10   # Speed of light [cm/s]
E = 4.80320425e-10  # Electric charge in [statC] = [cm^(3/2)g^(1/2)/s].
M_E = 9.10938356e-28  # Electron's mass in [g].
M_P = 1.67262192369e-24	 # Proton mass in [g].
SIGMA_T = 8. * np.pi / 3. * (E ** 2 / (M_E * C ** 2)) ** 2  # Thompson cross section in [cm^2].
