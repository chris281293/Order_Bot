# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.


class BookingDetails:
    def __init__(
        # self,
        # destination: str = None,
        # origin: str = None,
        # travel_date: str = None,
        #     unsupported_airports=None,
        self,
        food: str = None,
        count: str = None,
        adj: str = None,
            unsupported_airports=None,
    ):
        if unsupported_airports is None:
            unsupported_airports = []
        self.food = food
        self.count = count
        self.adj = adj
        self.unsupported_airports = unsupported_airports
