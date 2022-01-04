from __future__ import annotations
from abc import ABC, abstractmethod


class Factory:

    def __init__(self, product: Product) -> None:
        self.product = product

    def repair(self, defective):
        if defective:
            print("Sent for repair (defect detected)")
            self.product.fix()

    def add_buttons(self, buttons):
        print("Added buttons")
        self.product.set_buttons(self.product.get_buttons() + buttons)

    def put_buttons(self, buttons):
        print("Buttons removed")
        self.product.set_buttons(self.product.get_buttons() - buttons)

    def add_zippers(self, zippers):
        print("Added zippers")
        self.product.set_zippers(self.product.get_zippers() + zippers)

    def put_zippers(self, zippers):
        print("Removed zippers")
        self.product.set_zippers(self.product.get_zippers() - zippers)


class Product(ABC):

    @abstractmethod
    def fix(self) -> None:
        pass

    @abstractmethod
    def get_buttons(self) -> int:
        pass

    @abstractmethod
    def set_buttons(self, buttons: int) -> None:
        pass

    @abstractmethod
    def get_zippers(self) -> int:
        pass

    @abstractmethod
    def set_zippers(self, zippers: int) -> None:
        pass


class Jacket(Product):

    def __init__(self) -> None:
        self.defective = False
        self.buttons = 3
        self.zippers = 0

    def fix(self) -> None:
        self.defective = True

    def get_buttons(self) -> int:
        return self.buttons

    def set_buttons(self, buttons: int) -> None:
        if buttons < 0:
            self.buttons = 0
        else:
            self.buttons = buttons

    def get_zippers(self) -> int:
        return self.zippers

    def set_zippers(self, zippers: int) -> None:
        if zippers < 0:
            self.zippers = 0
        else:
            self.zippers = zippers


class Coat(Product):

    def __init__(self) -> None:
        self.defective = False
        self.buttons = 5
        self.zippers = 2
        self.insulated = False

    def fix(self) -> None:
        self.defective = True

    def get_buttons(self) -> int:
        return self.buttons

    def set_buttons(self, buttons: int) -> None:
        if buttons < 0:
            self.buttons = 0
        else:
            self.buttons = buttons

    def get_zippers(self) -> int:
        return self.zippers

    def set_zippers(self, zippers: int) -> None:
        if zippers < 0:
            self.zippers = 0
        else:
            self.zippers = zippers

    def insulate(self):
        self.insulated = True


class Dress(Product):

    def __init__(self) -> None:
        self.defective = False
        self.buttons = 1
        self.zippers = 1

    def fix(self) -> None:
        self.defective = True

    def get_buttons(self) -> int:
        return self.buttons

    def set_buttons(self, buttons: int) -> None:
        if buttons < 0:
            self.buttons = 0
        else:
            self.buttons = buttons

    def get_zippers(self) -> int:
        return self.zippers

    def set_zippers(self, zippers: int) -> None:
        if zippers < 0:
            self.zippers = 0
        else:
            self.zippers = zippers


class Jeans(Product):

    def __init__(self) -> None:
        self.defective = False
        self.buttons = 1
        self.zippers = 1

    def fix(self) -> None:
        self.defective = True

    def get_buttons(self) -> int:
        return self.buttons

    def set_buttons(self, buttons: int) -> None:
        if buttons < 0:
            self.buttons = 0
        else:
            self.buttons = buttons

    def get_zippers(self) -> int:
        return self.zippers

    def set_zippers(self, zippers: int) -> None:
        if zippers < 0:
            self.zippers = 0
        else:
            self.zippers = zippers


class Wallet(Product):

    def __init__(self) -> None:
        self.defective = False
        self.buttons = 0
        self.zippers = 1

    def fix(self) -> None:
        self.defective = True

    def get_buttons(self) -> int:
        return self.buttons

    def set_buttons(self, buttons: int) -> None:
        if buttons < 0:
            self.buttons = 0
        else:
            self.buttons = buttons

    def get_zippers(self) -> int:
        return self.zippers

    def set_zippers(self, zippers: int) -> None:
        if zippers < 0:
            self.zippers = 0
        else:
            self.zippers = zippers


def client_code(factory: Factory) -> None:

    factory.repair(True)
    factory.add_buttons(True)


if __name__ == "__main__":

    new_jeans = Jeans()
    new_factory = Factory(new_jeans)

    print("jeans defective:", new_jeans.defective)
    print("jeans buttons:", new_jeans.buttons)
    print("jeans zippers:", new_jeans.zippers)

    print("\n")
    client_code(new_factory)
    print("\n")

    print("jeans defective:", new_jeans.defective)
    print("jeans buttons:", new_jeans.buttons)
    print("jeans zippers:", new_jeans.zippers)

    print("\n")

    new_coat = Coat()
    new_factory = Factory(new_coat)

    print("coat defective:", new_coat.defective)
    print("coat buttons:", new_coat.buttons)
    print("coat zippers:", new_coat.zippers)
    print("coat insulated:", new_coat.insulated)

    print("\n")
    client_code(new_factory)
    print("\n")

    print("coat defective:", new_coat.defective)
    print("coat buttons:", new_coat.buttons)
    print("coat zippers:", new_coat.zippers)
    print("coat insulated:", new_coat.insulated)
