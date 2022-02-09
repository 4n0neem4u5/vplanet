import astropy.units as u
import pytest
from benchmark import Benchmark, benchmark


@benchmark(
    {
        "log.initial.system.Age": {"value": 1.577880e14, "unit": u.sec},
        "log.initial.system.Time": {"value": 0.000000, "unit": u.sec},
        "log.initial.system.TotAngMom": {
            "value": 3.489309e41,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.initial.system.TotEnergy": {"value": -2.672381e39, "unit": u.Joule},
        "log.initial.system.PotEnergy": {"value": -2.684995e39, "unit": u.Joule},
        "log.initial.system.KinEnergy": {"value": 1.261992e37, "unit": u.Joule},
        "log.initial.system.DeltaTime": {"value": 0.000000, "unit": u.sec},
        "log.initial.Trappist1.Mass": {"value": 1.590733e29, "unit": u.kg},
        "log.initial.Trappist1.Obliquity": {"value": 0.000000, "unit": u.rad},
        "log.initial.Trappist1.PrecA": {"value": 0.000000, "unit": u.rad},
        "log.initial.Trappist1.Xobl": {"value": 0.000000},
        "log.initial.Trappist1.Yobl": {"value": 0.000000},
        "log.initial.Trappist1.Zobl": {"value": 1.000000},
        "log.initial.Trappist1.Radius": {"value": 59.171870, "unit": u.Rearth},
        "log.initial.Trappist1.RadGyra": {"value": 0.458957},
        "log.initial.Trappist1.RotAngMom": {
            "value": 3.470727e41,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.initial.Trappist1.RotKinEnergy": {"value": 1.261992e37, "unit": u.Joule},
        "log.initial.Trappist1.RotVel": {"value": 2.744560e04, "unit": u.m / u.sec},
        "log.initial.Trappist1.BodyType": {"value": 0.000000},
        "log.initial.Trappist1.RotRate": {"value": 7.272205e-05, "unit": 1 / u.sec},
        "log.initial.Trappist1.RotPer": {"value": 8.640000e04, "unit": u.sec},
        "log.initial.Trappist1.Density": {"value": 706.461927, "unit": u.kg / u.m ** 3},
        "log.initial.Trappist1.SurfEnFluxTotal": {
            "value": 0.055898,
            "unit": u.kg / u.sec ** 3,
        },
        "log.initial.Trappist1.TidalQ": {"value": 100.000000},
        "log.initial.Trappist1.ImK2": {"value": -0.005000},
        "log.initial.Trappist1.K2": {"value": 0.500000},
        "log.initial.Trappist1.K2Man": {"value": 0.010000},
        "log.initial.Trappist1.Imk2Man": {"value": 0.000000},
        "log.initial.Trappist1.TidalQMantle": {"value": 100.000000},
        "log.initial.Trappist1.HEcc": {"value": 0.000000},
        "log.initial.Trappist1.HZLimitDryRunaway": {"value": 1.935431e10, "unit": u.m},
        "log.initial.Trappist1.HZLimRecVenus": {"value": 1.741821e10, "unit": u.m},
        "log.initial.Trappist1.HZLimRunaway": {"value": 2.292402e10, "unit": u.m},
        "log.initial.Trappist1.HZLimMoistGreenhouse": {
            "value": 2.304718e10,
            "unit": u.m,
        },
        "log.initial.Trappist1.HZLimMaxGreenhouse": {"value": 4.421989e10, "unit": u.m},
        "log.initial.Trappist1.HZLimEarlyMars": {"value": 4.822633e10, "unit": u.m},
        "log.initial.Trappist1.Instellation": {
            "value": -1.000000,
            "unit": u.kg / u.sec ** 3,
        },
        "log.initial.Trappist1.KEcc": {"value": 0.000000},
        "log.initial.Trappist1.Eccentricity": {"value": -1.000000},
        "log.initial.Trappist1.OrbEnergy": {"value": 0.000000, "unit": u.Joule},
        "log.initial.Trappist1.MeanMotion": {"value": -1.000000, "unit": 1 / u.sec},
        "log.initial.Trappist1.OrbPeriod": {"value": -1.000000, "unit": u.sec},
        "log.initial.Trappist1.SemiMajorAxis": {"value": -1.000000, "unit": u.m},
        "log.initial.Trappist1.CriticalSemiMajorAxis": {
            "value": -1.000000,
            "unit": u.m,
        },
        "log.initial.Trappist1.COPP": {"value": 0.000000},
        "log.initial.Trappist1.OrbAngMom": {
            "value": 0.000000,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.initial.Trappist1.LongP": {"value": 0.000000, "unit": u.rad},
        "log.initial.Trappist1.LXUVTot": {
            "value": 7.814003e21,
            "unit": u.kg / u.sec ** 3,
        },
        "log.initial.Trappist1.TotOrbEnergy": {"value": -5.151238e33, "unit": u.Joule},
        "log.initial.Trappist1.OrbPotEnergy": {"value": -1.000000, "unit": u.Joule},
        "log.initial.Trappist1.LostEnergy": {"value": 5.562685e-309, "unit": u.Joule},
        "log.initial.Trappist1.LostAngMom": {
            "value": 5.562685e-309,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.initial.Trappist1.LockTime": {"value": -1.000000, "unit": u.sec},
        "log.initial.Trappist1.BodyDsemiDtEqtide": {"value": -1.000000},
        "log.initial.Trappist1.BodyDeccDt": {"value": -1.000000},
        "log.initial.Trappist1.DOblDtEqtide": {
            "value": 0.000000,
            "unit": u.rad / u.sec,
        },
        "log.initial.Trappist1.DRotPerDtEqtide": {"value": 3.707592e-16},
        "log.initial.Trappist1.DRotRateDtEqtide": {
            "value": -3.120644e-25,
            "unit": 1 / u.sec ** 2,
        },
        "log.initial.Trappist1.EqRotRateDiscrete": {
            "value": 5.544505e-06,
            "unit": 1 / u.sec,
        },
        "log.initial.Trappist1.EqRotPerDiscrete": {"value": 1.133228e06, "unit": u.sec},
        "log.initial.Trappist1.EqRotRateCont": {
            "value": 5.544715e-06,
            "unit": 1 / u.sec,
        },
        "log.initial.Trappist1.EqRotPerCont": {"value": 1.133184e06, "unit": u.sec},
        "log.initial.Trappist1.EqRotPer": {"value": 1.133228e06, "unit": u.sec},
        "log.initial.Trappist1.EqTidePower": {"value": 0.000000, "unit": 1 / u.sec},
        "log.initial.Trappist1.GammaRot": {"value": -1.000000, "unit": u.sec},
        "log.initial.Trappist1.GammaOrb": {"value": -1.000000, "unit": u.sec},
        "log.initial.Trappist1.OceanK2": {"value": 0.010000},
        "log.initial.Trappist1.EnvTidalQ": {"value": -1.000000},
        "log.initial.Trappist1.OceanTidalQ": {"value": -1.000000},
        "log.initial.Trappist1.TideLock": {"value": 0.000000},
        "log.initial.Trappist1.RotTimeEqtide": {"value": 2.330354e20, "unit": u.sec},
        "log.initial.Trappist1.EnvK2": {"value": 0.010000},
        "log.initial.Trappist1.OblTimeEqtide": {"value": -1.000000},
        "log.initial.Trappist1.PowerEqtide": {"value": 1.000511e17, "unit": u.W},
        "log.initial.Trappist1.SurfEnFluxEqtide": {
            "value": 0.055898,
            "unit": u.kg / u.sec ** 3,
        },
        "log.initial.Trappist1.Luminosity": {"value": 0.020317, "unit": u.LSUN},
        "log.initial.Trappist1.LXUVStellar": {"value": 2.031722e-05, "unit": u.LSUN},
        "log.initial.Trappist1.Temperature": {"value": 2958.680453, "unit": u.K},
        "log.initial.Trappist1.LXUVFrac": {"value": 0.001000},
        "log.initial.Trappist1.RossbyNumber": {"value": 0.014482},
        "log.initial.Trappist1.DRotPerDtStellar": {"value": -1.871036e-10},
        "log.initial.g.Mass": {"value": 6.808292e24, "unit": u.kg},
        "log.initial.g.Obliquity": {"value": 0.000000, "unit": u.rad},
        "log.initial.g.PrecA": {"value": 0.000000, "unit": u.rad},
        "log.initial.g.Xobl": {"value": 0.000000},
        "log.initial.g.Yobl": {"value": 0.000000},
        "log.initial.g.Zobl": {"value": 1.000000},
        "log.initial.g.Radius": {"value": 7.334815e06, "unit": u.m},
        "log.initial.g.RadGyra": {"value": 0.500000},
        "log.initial.g.RotAngMom": {
            "value": 5.077141e32,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.initial.g.RotKinEnergy": {"value": 1.407512e27, "unit": u.Joule},
        "log.initial.g.RotVel": {"value": 40.667915, "unit": u.m / u.sec},
        "log.initial.g.BodyType": {"value": 0.000000},
        "log.initial.g.RotRate": {"value": 5.544505e-06, "unit": 1 / u.sec},
        "log.initial.g.RotPer": {"value": 1.133228e06, "unit": u.sec},
        "log.initial.g.Density": {"value": 4118.907830, "unit": u.kg / u.m ** 3},
        "log.initial.g.SurfEnFluxTotal": {"value": 0.126296, "unit": u.kg / u.sec ** 3},
        "log.initial.g.TidalQ": {"value": 100.000000},
        "log.initial.g.ImK2": {"value": -0.005000},
        "log.initial.g.K2": {"value": 0.500000},
        "log.initial.g.K2Man": {"value": 0.010000},
        "log.initial.g.Imk2Man": {"value": 0.000000},
        "log.initial.g.TidalQMantle": {"value": 100.000000},
        "log.initial.g.HEcc": {"value": 0.000000},
        "log.initial.g.HZLimitDryRunaway": {"value": 1.935435e10, "unit": u.m},
        "log.initial.g.HZLimRecVenus": {"value": 1.741821e10, "unit": u.m},
        "log.initial.g.HZLimRunaway": {"value": 2.292402e10, "unit": u.m},
        "log.initial.g.HZLimMoistGreenhouse": {"value": 2.304718e10, "unit": u.m},
        "log.initial.g.HZLimMaxGreenhouse": {"value": 4.421989e10, "unit": u.m},
        "log.initial.g.HZLimEarlyMars": {"value": 4.822633e10, "unit": u.m},
        "log.initial.g.Instellation": {"value": 1.263188e04, "unit": u.kg / u.sec ** 3},
        "log.initial.g.KEcc": {"value": 0.002000},
        "log.initial.g.Eccentricity": {"value": 0.002000},
        "log.initial.g.OrbEnergy": {"value": -5.151238e33, "unit": u.Joule},
        "log.initial.g.MeanMotion": {"value": 5.544505e-06, "unit": 1 / u.sec},
        "log.initial.g.OrbPeriod": {"value": 1.133228e06, "unit": u.sec},
        "log.initial.g.SemiMajorAxis": {"value": 7.016140e09, "unit": u.m},
        "log.initial.g.CriticalSemiMajorAxis": {"value": -1.000000, "unit": u.m},
        "log.initial.g.COPP": {"value": 0.000000},
        "log.initial.g.OrbAngMom": {
            "value": 1.858138e39,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.initial.g.LongP": {"value": 0.000000, "unit": u.rad},
        "log.initial.g.LXUVTot": {"value": -1.000000, "unit": u.kg / u.sec ** 3},
        "log.initial.g.TotOrbEnergy": {"value": -5.151238e33, "unit": u.Joule},
        "log.initial.g.OrbPotEnergy": {"value": -1.030248e34, "unit": u.Joule},
        "log.initial.g.LostEnergy": {"value": 5.562685e-309, "unit": u.Joule},
        "log.initial.g.TidalRadius": {"value": 7.334815e06, "unit": u.m},
        "log.initial.g.DsemiDtEqtide": {"value": 5.562685e-309, "unit": u.m / u.sec},
        "log.initial.g.DeccDtEqtide": {"value": -9.370697e-21, "unit": 1 / u.sec},
        "log.initial.g.DMeanMotionDtEqtide": {
            "value": -4.940656e-324,
            "unit": 1 / u.sec ** 2,
        },
        "log.initial.g.DOrbPerDtEqtide": {"value": 1.347704e-312},
        "log.initial.g.EccTimeEqtide": {"value": 3.595386e305, "unit": u.sec},
        "log.initial.g.DHEccDtEqtide": {"value": 5.562685e-309, "unit": 1 / u.sec},
        "log.initial.g.DKEccDtEqtide": {"value": 5.562685e-309, "unit": 1 / u.sec},
        "log.initial.g.DXoblDtEqtide": {"value": 0.000000, "unit": 1 / u.sec},
        "log.initial.g.DYoblDtEqtide": {"value": 0.000000, "unit": 1 / u.sec},
        "log.initial.g.DZoblDtEqtide": {"value": 0.000000, "unit": 1 / u.sec},
        "log.initial.g.LockTime": {"value": 0.000000, "unit": u.sec},
        "log.initial.g.BodyDsemiDtEqtide": {"value": -1.000000},
        "log.initial.g.BodyDeccDt": {"value": -1.000000},
        "log.initial.g.DOblDtEqtide": {"value": 0.000000, "unit": u.rad / u.sec},
        "log.initial.g.DRotPerDtEqtide": {"value": -1.136943e-297},
        "log.initial.g.DRotRateDtEqtide": {
            "value": 5.562685e-309,
            "unit": 1 / u.sec ** 2,
        },
        "log.initial.g.EqRotRateDiscrete": {"value": 5.544505e-06, "unit": 1 / u.sec},
        "log.initial.g.EqRotPerDiscrete": {"value": 1.133228e06, "unit": u.sec},
        "log.initial.g.EqRotRateCont": {"value": 5.544715e-06, "unit": 1 / u.sec},
        "log.initial.g.EqRotPerCont": {"value": 1.133184e06, "unit": u.sec},
        "log.initial.g.EqRotPer": {"value": 1.133228e06, "unit": u.sec},
        "log.initial.g.EqTidePower": {"value": -0.000000, "unit": 1 / u.sec},
        "log.initial.g.GammaRot": {"value": -1.000000, "unit": u.sec},
        "log.initial.g.GammaOrb": {"value": -1.000000, "unit": u.sec},
        "log.initial.g.OceanK2": {"value": 0.010000},
        "log.initial.g.EnvTidalQ": {"value": -1.000000},
        "log.initial.g.OceanTidalQ": {"value": -1.000000},
        "log.initial.g.TideLock": {"value": 1.000000},
        "log.initial.g.RotTimeEqtide": {"value": 9.967318e302, "unit": u.sec},
        "log.initial.g.EnvK2": {"value": 0.010000},
        "log.initial.g.OblTimeEqtide": {"value": -1.000000},
        "log.initial.g.PowerEqtide": {"value": 3.499752e11, "unit": u.W},
        "log.initial.g.SurfEnFluxEqtide": {
            "value": 0.000518,
            "unit": u.kg / u.sec ** 3,
        },
        "log.initial.g.D26AlPowerDt": {"value": -1.000000},
        "log.initial.g.D26AlNumManDt": {"value": 0.000000, "unit": 1 / u.sec},
        "log.initial.g.D40KPowerDt": {"value": -1.000000},
        "log.initial.g.D40KNumManDt": {"value": -1.931840e26, "unit": 1 / u.sec},
        "log.initial.g.D232ThNumManDt": {"value": -1.086973e24, "unit": 1 / u.sec},
        "log.initial.g.D238UNumManDt": {"value": -1.606037e24, "unit": 1 / u.sec},
        "log.initial.g.D235UNumManDt": {"value": -3.521474e24, "unit": 1 / u.sec},
        "log.initial.g.RadPowerMan": {"value": 8.503439e13, "unit": u.W},
        "log.initial.g.RadPowerCore": {"value": -0.000000, "unit": u.W},
        "log.initial.g.RadPowerCrust": {"value": -0.000000, "unit": u.W},
        "log.initial.g.RadPowerTotal": {"value": 8.503439e13, "unit": u.W},
        "log.initial.g.SurfEnFluxRadTotal": {
            "value": 0.125779,
            "unit": u.kg / u.sec ** 3,
        },
        "log.initial.g.SurfWaterMass": {"value": 2.780000e21, "unit": u.kg},
        "log.initial.g.EnvelopeMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.g.OxygenMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.g.RGLimit": {"value": 2.216633e10, "unit": u.m},
        "log.initial.g.XO": {"value": 0.333333},
        "log.initial.g.EtaO": {"value": 0.908442},
        "log.initial.g.PlanetRadius": {"value": 7.334815e06, "unit": u.m},
        "log.initial.g.OxygenMantleMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.g.RadXUV": {"value": -1.000000, "unit": u.m},
        "log.initial.g.RadSolid": {"value": -1.000000, "unit": u.m},
        "log.initial.g.PresXUV": {"value": 5.000000},
        "log.initial.g.ScaleHeight": {"value": -1.000000, "unit": u.m},
        "log.initial.g.ThermTemp": {"value": 288.852751, "unit": u.K},
        "log.initial.g.AtmGasConst": {"value": 4124.000000},
        "log.initial.g.PresSurf": {"value": -1.000000, "unit": u.Pa},
        "log.initial.g.DEnvMassDt": {"value": 0.000000, "unit": u.kg / u.sec},
        "log.initial.g.FXUV": {"value": 12.631882, "unit": u.W / u.m ** 2},
        "log.initial.g.AtmXAbsEffH2O": {"value": 0.300000},
        "log.initial.g.RocheRadius": {"value": 1.701655e08, "unit": u.m},
        "log.initial.g.BondiRadius": {"value": 1.669199e08, "unit": u.m},
        "log.initial.g.HEscapeRegime": {"value": 8.000000},
        "log.initial.g.RRCriticalFlux": {"value": 40.154478, "unit": u.W / u.m ** 2},
        "log.initial.g.KTide": {"value": 0.935384},
        "log.initial.g.RGDuration": {"value": 0.00000e00, "unit": u.yr},
        "log.initial.g.WaterMassMOAtm": {"value": 2.000000, "unit": u.TO},
        "log.initial.g.PotTemp": {"value": 4000.000000, "unit": u.K},
        "log.initial.g.SurfTemp": {"value": 4000.000000, "unit": u.K},
        "log.initial.g.WaterMassSol": {"value": 0.000000, "unit": u.TO},
        "log.initial.g.SolidRadius": {"value": 0.613035, "unit": u.Rearth},
        "log.initial.g.OxygenMassMOAtm": {"value": 0.000000, "unit": u.kg},
        "log.initial.g.OxygenMassSol": {"value": 0.000000, "unit": u.kg},
        "log.initial.g.PressWaterAtm": {"value": 4.098668e05},
        "log.initial.g.PressOxygenAtm": {"value": 0.000000},
        "log.initial.g.HydrogenMassSpace": {"value": 0.000000, "unit": u.kg},
        "log.initial.g.OxygenMassSpace": {"value": 0.000000, "unit": u.kg},
        "log.initial.g.FracFe2O3Man": {"value": 0.000000},
        "log.initial.g.NetFluxAtmo": {"value": 7.191296e05},
        "log.initial.g.WaterFracMelt": {"value": 0.000490},
        "log.initial.g.RadioPower": {"value": 8.503439e13, "unit": u.W},
        "log.initial.g.TidalPower": {"value": 3.499752e11, "unit": u.W},
        "log.initial.g.HZInnerEdge": {"value": 2.216633e10, "unit": u.m},
        "log.initial.g.MeltFraction": {"value": 1.000000},
        "log.initial.g.CO2MassMOAtm": {"value": 0.000000, "unit": u.kg},
        "log.initial.g.CO2MassSol": {"value": 0.000000, "unit": u.kg},
        "log.initial.g.PressCO2Atm": {"value": 0.000000},
        "log.initial.g.CO2FracMelt": {"value": 0.000000},
        "log.final.system.Age": {"value": 1.581036e14, "unit": u.sec},
        "log.final.system.Time": {"value": 3.155760e11, "unit": u.sec},
        "log.final.system.TotAngMom": {
            "value": 3.489314e41,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.final.system.TotEnergy": {"value": -2.672379e39, "unit": u.Joule},
        "log.final.system.PotEnergy": {"value": -2.688114e39, "unit": u.Joule},
        "log.final.system.KinEnergy": {"value": 1.260909e37, "unit": u.Joule},
        "log.final.system.DeltaTime": {"value": 1.824983e06, "unit": u.sec},
        "log.final.Trappist1.Mass": {"value": 1.590733e29, "unit": u.kg},
        "log.final.Trappist1.Obliquity": {"value": 0.000000, "unit": u.rad},
        "log.final.Trappist1.PrecA": {"value": 0.000000, "unit": u.rad},
        "log.final.Trappist1.Xobl": {"value": 0.000000},
        "log.final.Trappist1.Yobl": {"value": 0.000000},
        "log.final.Trappist1.Zobl": {"value": 1.000000},
        "log.final.Trappist1.Radius": {"value": 59.103227, "unit": u.Rearth},
        "log.final.Trappist1.RadGyra": {"value": 0.458983},
        "log.final.Trappist1.RotAngMom": {
            "value": 3.465407e41,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.final.Trappist1.RotKinEnergy": {"value": 1.260909e37, "unit": u.Joule},
        "log.final.Trappist1.RotVel": {"value": 2.743230e04, "unit": u.m / u.sec},
        "log.final.Trappist1.BodyType": {"value": 0.000000},
        "log.final.Trappist1.RotRate": {"value": 7.277122e-05, "unit": 1 / u.sec},
        "log.final.Trappist1.RotPer": {"value": 8.634162e04, "unit": u.sec},
        "log.final.Trappist1.Density": {"value": 708.926273, "unit": u.kg / u.m ** 3},
        "log.final.Trappist1.SurfEnFluxTotal": {
            "value": 0.055745,
            "unit": u.kg / u.sec ** 3,
        },
        "log.final.Trappist1.TidalQ": {"value": 100.000000},
        "log.final.Trappist1.ImK2": {"value": -0.005000},
        "log.final.Trappist1.K2": {"value": 0.500000},
        "log.final.Trappist1.K2Man": {"value": 0.010000},
        "log.final.Trappist1.Imk2Man": {"value": 0.000000},
        "log.final.Trappist1.TidalQMantle": {"value": 100.000000},
        "log.final.Trappist1.HEcc": {"value": 0.000000},
        "log.final.Trappist1.HZLimitDryRunaway": {"value": 1.933388e10, "unit": u.m},
        "log.final.Trappist1.HZLimRecVenus": {"value": 1.739978e10, "unit": u.m},
        "log.final.Trappist1.HZLimRunaway": {"value": 2.289979e10, "unit": u.m},
        "log.final.Trappist1.HZLimMoistGreenhouse": {"value": 2.302279e10, "unit": u.m},
        "log.final.Trappist1.HZLimMaxGreenhouse": {"value": 4.417286e10, "unit": u.m},
        "log.final.Trappist1.HZLimEarlyMars": {"value": 4.817504e10, "unit": u.m},
        "log.final.Trappist1.Instellation": {
            "value": -1.000000,
            "unit": u.kg / u.sec ** 3,
        },
        "log.final.Trappist1.KEcc": {"value": 0.000000},
        "log.final.Trappist1.Eccentricity": {"value": -1.000000},
        "log.final.Trappist1.OrbEnergy": {"value": 0.000000, "unit": u.Joule},
        "log.final.Trappist1.MeanMotion": {"value": -1.000000, "unit": 1 / u.sec},
        "log.final.Trappist1.OrbPeriod": {"value": -1.000000, "unit": u.sec},
        "log.final.Trappist1.SemiMajorAxis": {"value": -1.000000, "unit": u.m},
        "log.final.Trappist1.CriticalSemiMajorAxis": {"value": -1.000000, "unit": u.m},
        "log.final.Trappist1.COPP": {"value": 0.000000},
        "log.final.Trappist1.OrbAngMom": {
            "value": 0.000000,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.final.Trappist1.LongP": {"value": 0.000000, "unit": u.rad},
        "log.final.Trappist1.LXUVTot": {
            "value": 7.797515e21,
            "unit": u.kg / u.sec ** 3,
        },
        "log.final.Trappist1.TotOrbEnergy": {"value": -5.151238e33, "unit": u.Joule},
        "log.final.Trappist1.OrbPotEnergy": {"value": -1.000000, "unit": u.Joule},
        "log.final.Trappist1.LostEnergy": {"value": 3.131169e36, "unit": u.Joule},
        "log.final.Trappist1.LostAngMom": {
            "value": 5.325474e38,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.final.Trappist1.LockTime": {"value": -1.000000, "unit": u.sec},
        "log.final.Trappist1.BodyDsemiDtEqtide": {"value": -1.000000},
        "log.final.Trappist1.BodyDeccDt": {"value": -1.000000},
        "log.final.Trappist1.DOblDtEqtide": {"value": 0.000000, "unit": u.rad / u.sec},
        "log.final.Trappist1.DRotPerDtEqtide": {"value": 3.689301e-16},
        "log.final.Trappist1.DRotRateDtEqtide": {
            "value": -3.109450e-25,
            "unit": 1 / u.sec ** 2,
        },
        "log.final.Trappist1.EqRotRateDiscrete": {
            "value": 5.544505e-06,
            "unit": 1 / u.sec,
        },
        "log.final.Trappist1.EqRotPerDiscrete": {"value": 1.133228e06, "unit": u.sec},
        "log.final.Trappist1.EqRotRateCont": {"value": 5.544715e-06, "unit": 1 / u.sec},
        "log.final.Trappist1.EqRotPerCont": {"value": 1.133184e06, "unit": u.sec},
        "log.final.Trappist1.EqRotPer": {"value": 1.133228e06, "unit": u.sec},
        "log.final.Trappist1.EqTidePower": {"value": 0.000000, "unit": 1 / u.sec},
        "log.final.Trappist1.GammaRot": {"value": -1.000000, "unit": u.sec},
        "log.final.Trappist1.GammaOrb": {"value": -1.000000, "unit": u.sec},
        "log.final.Trappist1.OceanK2": {"value": 0.010000},
        "log.final.Trappist1.EnvTidalQ": {"value": -1.000000},
        "log.final.Trappist1.OceanTidalQ": {"value": -1.000000},
        "log.final.Trappist1.TideLock": {"value": 0.000000},
        "log.final.Trappist1.RotTimeEqtide": {"value": 2.340324e20, "unit": u.sec},
        "log.final.Trappist1.EnvK2": {"value": 0.010000},
        "log.final.Trappist1.OblTimeEqtide": {"value": -1.000000},
        "log.final.Trappist1.PowerEqtide": {"value": 9.954496e16, "unit": u.W},
        "log.final.Trappist1.SurfEnFluxEqtide": {
            "value": 0.055745,
            "unit": u.kg / u.sec ** 3,
        },
        "log.final.Trappist1.Luminosity": {"value": 0.020274, "unit": u.LSUN},
        "log.final.Trappist1.LXUVStellar": {"value": 2.027435e-05, "unit": u.LSUN},
        "log.final.Trappist1.Temperature": {"value": 2958.826369, "unit": u.K},
        "log.final.Trappist1.LXUVFrac": {"value": 0.001000},
        "log.final.Trappist1.RossbyNumber": {"value": 0.014473},
        "log.final.Trappist1.DRotPerDtStellar": {"value": -1.829957e-10},
        "log.final.g.Mass": {"value": 6.808292e24, "unit": u.kg},
        "log.final.g.Obliquity": {"value": 0.000000, "unit": u.rad},
        "log.final.g.PrecA": {"value": 0.000000, "unit": u.rad},
        "log.final.g.Xobl": {"value": 0.000000},
        "log.final.g.Yobl": {"value": 0.000000},
        "log.final.g.Zobl": {"value": 1.000000},
        "log.final.g.Radius": {"value": 7.334815e06, "unit": u.m},
        "log.final.g.RadGyra": {"value": 0.500000},
        "log.final.g.RotAngMom": {
            "value": 5.077141e32,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.final.g.RotKinEnergy": {"value": 1.407512e27, "unit": u.Joule},
        "log.final.g.RotVel": {"value": 40.667915, "unit": u.m / u.sec},
        "log.final.g.BodyType": {"value": 0.000000},
        "log.final.g.RotRate": {"value": 5.544505e-06, "unit": 1 / u.sec},
        "log.final.g.RotPer": {"value": 1.133228e06, "unit": u.sec},
        "log.final.g.Density": {"value": 4118.907830, "unit": u.kg / u.m ** 3},
        "log.final.g.SurfEnFluxTotal": {"value": 0.126295, "unit": u.kg / u.sec ** 3},
        "log.final.g.TidalQ": {"value": 100.000000},
        "log.final.g.ImK2": {"value": -0.005000},
        "log.final.g.K2": {"value": 0.500000},
        "log.final.g.K2Man": {"value": 0.010000},
        "log.final.g.Imk2Man": {"value": 0.000000},
        "log.final.g.TidalQMantle": {"value": 100.000000},
        "log.final.g.HEcc": {"value": 1.755450e-297},
        "log.final.g.HZLimitDryRunaway": {"value": 1.933392e10, "unit": u.m},
        "log.final.g.HZLimRecVenus": {"value": 1.739978e10, "unit": u.m},
        "log.final.g.HZLimRunaway": {"value": 2.289979e10, "unit": u.m},
        "log.final.g.HZLimMoistGreenhouse": {"value": 2.302279e10, "unit": u.m},
        "log.final.g.HZLimMaxGreenhouse": {"value": 4.417286e10, "unit": u.m},
        "log.final.g.HZLimEarlyMars": {"value": 4.817504e10, "unit": u.m},
        "log.final.g.Instellation": {"value": 1.260523e04, "unit": u.kg / u.sec ** 3},
        "log.final.g.KEcc": {"value": 0.002000},
        "log.final.g.Eccentricity": {"value": 0.002000},
        "log.final.g.OrbEnergy": {"value": -5.151238e33, "unit": u.Joule},
        "log.final.g.MeanMotion": {"value": 5.544505e-06, "unit": 1 / u.sec},
        "log.final.g.OrbPeriod": {"value": 1.133228e06, "unit": u.sec},
        "log.final.g.SemiMajorAxis": {"value": 7.016140e09, "unit": u.m},
        "log.final.g.CriticalSemiMajorAxis": {"value": -1.000000, "unit": u.m},
        "log.final.g.COPP": {"value": 0.000000},
        "log.final.g.OrbAngMom": {
            "value": 1.858138e39,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.final.g.LongP": {"value": 8.777249e-295, "unit": u.rad},
        "log.final.g.LXUVTot": {"value": -1.000000, "unit": u.kg / u.sec ** 3},
        "log.final.g.TotOrbEnergy": {"value": -5.151238e33, "unit": u.Joule},
        "log.final.g.OrbPotEnergy": {"value": -1.030248e34, "unit": u.Joule},
        "log.final.g.LostEnergy": {"value": 1.104438e23, "unit": u.Joule},
        "log.final.g.TidalRadius": {"value": 7.334815e06, "unit": u.m},
        "log.final.g.DsemiDtEqtide": {"value": 5.562685e-309, "unit": u.m / u.sec},
        "log.final.g.DeccDtEqtide": {"value": -9.414760e-21, "unit": 1 / u.sec},
        "log.final.g.DMeanMotionDtEqtide": {
            "value": -4.940656e-324,
            "unit": 1 / u.sec ** 2,
        },
        "log.final.g.DOrbPerDtEqtide": {"value": 1.347704e-312},
        "log.final.g.EccTimeEqtide": {"value": 3.155760e11, "unit": u.sec},
        "log.final.g.DHEccDtEqtide": {"value": 5.562685e-309, "unit": 1 / u.sec},
        "log.final.g.DKEccDtEqtide": {"value": 5.562685e-309, "unit": 1 / u.sec},
        "log.final.g.DXoblDtEqtide": {"value": 0.000000, "unit": 1 / u.sec},
        "log.final.g.DYoblDtEqtide": {"value": 0.000000, "unit": 1 / u.sec},
        "log.final.g.DZoblDtEqtide": {"value": 0.000000, "unit": 1 / u.sec},
        "log.final.g.LockTime": {"value": 0.000000, "unit": u.sec},
        "log.final.g.BodyDsemiDtEqtide": {"value": -1.000000},
        "log.final.g.BodyDeccDt": {"value": -1.000000},
        "log.final.g.DOblDtEqtide": {"value": 0.000000, "unit": u.rad / u.sec},
        "log.final.g.DRotPerDtEqtide": {"value": -1.136943e-297},
        "log.final.g.DRotRateDtEqtide": {
            "value": 5.562685e-309,
            "unit": 1 / u.sec ** 2,
        },
        "log.final.g.EqRotRateDiscrete": {"value": 5.544505e-06, "unit": 1 / u.sec},
        "log.final.g.EqRotPerDiscrete": {"value": 1.133228e06, "unit": u.sec},
        "log.final.g.EqRotRateCont": {"value": 5.544715e-06, "unit": 1 / u.sec},
        "log.final.g.EqRotPerCont": {"value": 1.133184e06, "unit": u.sec},
        "log.final.g.EqRotPer": {"value": 1.133228e06, "unit": u.sec},
        "log.final.g.EqTidePower": {"value": -0.000000, "unit": 1 / u.sec},
        "log.final.g.GammaRot": {"value": -1.000000, "unit": u.sec},
        "log.final.g.GammaOrb": {"value": -1.000000, "unit": u.sec},
        "log.final.g.OceanK2": {"value": 0.010000},
        "log.final.g.EnvTidalQ": {"value": -1.000000},
        "log.final.g.OceanTidalQ": {"value": -1.000000},
        "log.final.g.TideLock": {"value": 1.000000},
        "log.final.g.RotTimeEqtide": {"value": 9.967318e302, "unit": u.sec},
        "log.final.g.EnvK2": {"value": 0.010000},
        "log.final.g.OblTimeEqtide": {"value": -1.000000},
        "log.final.g.PowerEqtide": {"value": 3.499752e11, "unit": u.W},
        "log.final.g.SurfEnFluxEqtide": {"value": 0.000518, "unit": u.kg / u.sec ** 3},
        "log.final.g.D26AlPowerDt": {"value": -1.000000},
        "log.final.g.D26AlNumManDt": {"value": 0.000000, "unit": 1 / u.sec},
        "log.final.g.D40KPowerDt": {"value": -1.000000},
        "log.final.g.D40KNumManDt": {"value": -1.931830e26, "unit": 1 / u.sec},
        "log.final.g.D232ThNumManDt": {"value": -1.086973e24, "unit": 1 / u.sec},
        "log.final.g.D238UNumManDt": {"value": -1.606035e24, "unit": 1 / u.sec},
        "log.final.g.D235UNumManDt": {"value": -3.521439e24, "unit": 1 / u.sec},
        "log.final.g.RadPowerMan": {"value": 8.503391e13, "unit": u.W},
        "log.final.g.RadPowerCore": {"value": -0.000000, "unit": u.W},
        "log.final.g.RadPowerCrust": {"value": -0.000000, "unit": u.W},
        "log.final.g.RadPowerTotal": {"value": 8.503391e13, "unit": u.W},
        "log.final.g.SurfEnFluxRadTotal": {
            "value": 0.125778,
            "unit": u.kg / u.sec ** 3,
        },
        "log.final.g.SurfWaterMass": {"value": 2.780000e21, "unit": u.kg},
        "log.final.g.EnvelopeMass": {"value": 0.000000, "unit": u.kg},
        "log.final.g.OxygenMass": {"value": 0.000000, "unit": u.kg},
        "log.final.g.RGLimit": {"value": 2.214290e10, "unit": u.m},
        "log.final.g.XO": {"value": 0.333333},
        "log.final.g.EtaO": {"value": 0.908264},
        "log.final.g.PlanetRadius": {"value": 7.334815e06, "unit": u.m},
        "log.final.g.OxygenMantleMass": {"value": 0.000000, "unit": u.kg},
        "log.final.g.RadXUV": {"value": -1.000000, "unit": u.m},
        "log.final.g.RadSolid": {"value": -1.000000, "unit": u.m},
        "log.final.g.PresXUV": {"value": 5.000000},
        "log.final.g.ScaleHeight": {"value": -1.000000, "unit": u.m},
        "log.final.g.ThermTemp": {"value": 288.700256, "unit": u.K},
        "log.final.g.AtmGasConst": {"value": 4124.000000},
        "log.final.g.PresSurf": {"value": -1.000000, "unit": u.Pa},
        "log.final.g.DEnvMassDt": {"value": 0.000000, "unit": u.kg / u.sec},
        "log.final.g.FXUV": {"value": 12.605228, "unit": u.W / u.m ** 2},
        "log.final.g.AtmXAbsEffH2O": {"value": 0.300000},
        "log.final.g.RocheRadius": {"value": 1.701655e08, "unit": u.m},
        "log.final.g.BondiRadius": {"value": 1.670086e08, "unit": u.m},
        "log.final.g.HEscapeRegime": {"value": 8.000000},
        "log.final.g.RRCriticalFlux": {"value": 40.154478, "unit": u.W / u.m ** 2},
        "log.final.g.KTide": {"value": 0.935384},
        "log.final.g.RGDuration": {"value": 0.00000e00, "unit": u.yr},
        "log.final.g.WaterMassMOAtm": {"value": 1.970140, "unit": u.TO},
        "log.final.g.PotTemp": {"value": 2341.642524, "unit": u.K},
        "log.final.g.SurfTemp": {"value": 4000.000000, "unit": u.K},
        "log.final.g.WaterMassSol": {"value": 0.027131, "unit": u.TO},
        "log.final.g.SolidRadius": {"value": 1.007041, "unit": u.Rearth},
        "log.final.g.OxygenMassMOAtm": {"value": 2.229468e17, "unit": u.kg},
        "log.final.g.OxygenMassSol": {"value": 8.607391e16, "unit": u.kg},
        "log.final.g.PressWaterAtm": {"value": 3.436476e06},
        "log.final.g.PressOxygenAtm": {"value": 0.000000},
        "log.final.g.HydrogenMassSpace": {"value": 4.244704e17, "unit": u.kg},
        "log.final.g.OxygenMassSpace": {"value": 3.059782e18, "unit": u.kg},
        "log.final.g.FracFe2O3Man": {"value": 1.024552e-06},
        "log.final.g.NetFluxAtmo": {"value": 1.052877e04},
        "log.final.g.WaterFracMelt": {"value": 0.002362},
        "log.final.g.RadioPower": {"value": 8.503391e13, "unit": u.W},
        "log.final.g.TidalPower": {"value": 3.499752e11, "unit": u.W},
        "log.final.g.HZInnerEdge": {"value": 2.214290e10, "unit": u.m},
        "log.final.g.MeltFraction": {"value": 0.474952},
        "log.final.g.CO2MassMOAtm": {"value": 1.755002e-297, "unit": u.kg},
        "log.final.g.CO2MassSol": {"value": 1.755002e-297, "unit": u.kg},
        "log.final.g.PressCO2Atm": {"value": 0.000000},
        "log.final.g.CO2FracMelt": {"value": 0.000000},
    }
)
class TestMagmOc_Trappist1g(Benchmark):
    pass
