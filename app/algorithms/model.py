from controller import controller


class mainModel:
    def runModel(self):
        chain_name = 'polygons'
        newController = controller(chain_name)
        # newController.getDistance()
        newController.mst()
        pass


if __name__ == '__main__':
    newMainModel = mainModel()
    newMainModel.runModel()