from typing import List
from pandas import DataFrame
import networkx as nx

from utils import create_features_df
from ..prediction import(
    UnevenlySpacedItemsHorizontalPredictor,
    UnevenlySpacedItemsVerticalPredictor
)
from ..dto import(
    UnevenlySpacedItemsInput,
    UnevenlySpacedItemsOutput,
)

class UnevenlySpacedItemsUsecase:

    def __init__(self, horizontal_predictor: UnevenlySpacedItemsHorizontalPredictor,
                       vertical_predictor: UnevenlySpacedItemsVerticalPredictor):
        self._horizontal_predictor = horizontal_predictor
        self._vertical_predictor = vertical_predictor

    def predict(self, input: UnevenlySpacedItemsInput) -> UnevenlySpacedItemsOutput:
        features_df = create_features_df(input.input)
        if input.direction == "horizontal":
            return self._predict_horizontal(features_df)
        elif input.direction == "vertical":
            return self._predict_vertical(features_df)

    def _predict_horizontal(self, input_list: DataFrame) -> UnevenlySpacedItemsOutput:
        y = self._horizontal_predictor.predict(input_list[["diff_distance", "diff_size"]])
        input_list["is_same_group"] = y
        group = self._group_ids(input_list)
        return UnevenlySpacedItemsOutput(output=group)

    def _predict_vertical(self, input_list: DataFrame) -> UnevenlySpacedItemsOutput:
        y = self._vertical_predictor.predict(input_list[["diff_distance", "diff_size"]])
        input_list["is_same_group"] = y
        group = self._group_ids(input_list)
        return UnevenlySpacedItemsOutput(output=group)

    def _group_ids(self, df: DataFrame) -> List:
        G = nx.Graph()
        connected_groups = df[df['is_same_group']]
        if not len(connected_groups):
            res = [list(set(df["id_1"].tolist()).union(set(df["id_2"].tolist())))]
            for e in res:
                e.sort()
            return res
        for _, row in connected_groups.iterrows():
            if row['is_same_group']:
                G.add_edge(row['id_1'], row['id_2'])

        # Find connected components where 'is_same_group' is True
        result = list(nx.connected_components(G))

        # Find elements that are not in any group
        elements_without_group = list(set(df['id_1']).union(set(df['id_2'])) - set.union(*result))
        elements_without_group.sort()
        # Filter out elements without a group
        result = [list(group) for group in result if group]

        # Add elements without a group as individual elements in the result
        result.extend([[elem] for elem in elements_without_group])
        for e in result:
            e.sort()
        return result
