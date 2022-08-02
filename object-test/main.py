def main():
    test_data = TestObject("unchanged string")
    container = ContainerObject(test_data)
    # print test_data.data from container
    print(container.get_data())
    container.set_data("changed string from inside container")
    # print new data
    print(container.get_data())
    # check if data changed from inside container changes outer object
    print(test_data.get_data())
    # it does


class TestObject:
    def __init__(self, data) -> None:
        self.data = data

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


class ContainerObject:
    def __init__(self, data: TestObject) -> None:
        self.data = data

    def get_data(self):
        return self.data.get_data()

    def set_data(self, data: TestObject):
        self.data.set_data(data)


if __name__ == "__main__":
    main()
