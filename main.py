import sys
import traci  # noqa

traci.start(["sumo-gui", "-c", "/location/map.sumo.cfg",
            "--emission-output", "emission"], port=7911)
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()
traci.close()
sys.exit()
