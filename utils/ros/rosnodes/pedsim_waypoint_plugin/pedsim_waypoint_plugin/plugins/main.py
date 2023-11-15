from pedsim_waypoint_plugin.pedsim_waypoint_generator import OutputData, PedsimWaypointGenerator, InputData, WaypointPluginName, WaypointPlugin
import pedsim_msgs.msg
import rvo_lib
@PedsimWaypointGenerator.register(WaypointPluginName.RVO)
class Plugin_rvo_ros(WaypointPlugin):
    def __init__(self):
        self.simulator = rvo_lib.RVOSimulator
        self.agent_id_map = {}


    def callback(self, data) -> OutputData:
           def datapoint_to_vec(agent: pedsim_msgs.msg.AgentState) -> 
        return [pedsim_msgs.msg.AgentFeedback(unforce=True) for agent in data.agents]

