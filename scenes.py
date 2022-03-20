class Scene_Manager:

    def __init__(self):
        self.scenes = dict()
        self.current_scene = None

    def add_scene(self, scene_id, scene):
        self.scenes[scene_id] = scene

    def swap_scene(self, scene_id):
        self.current_scene = self.scenes[scene_id]
