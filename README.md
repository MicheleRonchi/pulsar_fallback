# Long period pulsars as possible outcomes of supernova fallback

This repository provides some Jupyter notebooks and related files to recreate the results and plots of [Ronchi et al. (2022)](https://arxiv.org/abs/2201.11704). Please cite Ronchi et al. (2022) when using this material.

## Description

The Jupyter notebook `spindown_dipolar_Bdecay.ipynb` contains the code to study the spin-period evolution of pulsars spinning down due to dipolar losses alone in the presence of magnetic field decay. If the magnetic field dissipates in the neutron star crust, pulsars should be unable to reach very long spin periods. 
As discussed in Ronchi et al. (2022), a more promising scenario to explain the observation of pulsars with periods much larger than 10 s is a neutron star interacting with a supernova fallback disk for a period of 10<sup>3</sup> - 10<sup>4</sup> yr after its birth. The Jupyter notebook `propeller_parameter_search_Bdecay.ipynb` contains the code to perform a parameter study of the spin-period evolution of pulsars interacting with a supernova fallback disk.
In addition, we study the cases of two recently discovered periodic radio sources, the pulsar MTP0013 (Caleb et al. 2022 in press)(P = 75.9 s) and the radio transient GLEAM-X J162759.5-523504.3 ([Hurley-Walker et al. 2022](https://www.nature.com/articles/s41586-021-04272-x)) (P = 1091 s), in light of the fallback scenario. 
The Jupyter notebook `gleam_mtp_evolution_example.ipynb` shows an example of the evolution of the spin-period, spin-down power and disk X-ray luminosity for these peculiar sources.

The file `plot_settings.py` contains some settings for the layout of the plots; 
the file `constants.py` contains some physical constants relevant for this study;
the files `atnf_catalog_full_08-02-2022.csv` and `magnetars_08-02-2022.csv` contain the data of the observed pulsars and magnetars from the ATNF Pulsar Catalog (https://www.atnf.csiro.au/research/pulsar/psrcat/; [Manchester et al. 2005](https://ui.adsabs.harvard.edu/abs/2005AJ....129.1993M/abstract)) and the Magnetar Outburst Online Catalogue (http://magnetars.ice.csic.es/; [Coti Zelati et al.
2018](https://ui.adsabs.harvard.edu/abs/2018MNRAS.474..961C/abstract)), respectively.

We also provide the environment file that has been used to create our results. It can be installed by running `conda env create -f environment.yaml`
and has been tested under Linux. Please contact the author if you have any problems.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
