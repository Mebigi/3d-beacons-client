# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.result_segments import ResultSegments  # noqa: F401,E501
from swagger_server import util


class ResultChains(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, chain_id: str=None, segments: List[ResultSegments]=None):  # noqa: E501
        """ResultChains - a model defined in Swagger

        :param chain_id: The chain_id of this ResultChains.  # noqa: E501
        :type chain_id: str
        :param segments: The segments of this ResultChains.  # noqa: E501
        :type segments: List[ResultSegments]
        """
        self.swagger_types = {
            'chain_id': str,
            'segments': List[ResultSegments]
        }

        self.attribute_map = {
            'chain_id': 'chain_id',
            'segments': 'segments'
        }
        self._chain_id = chain_id
        self._segments = segments

    @classmethod
    def from_dict(cls, dikt) -> 'ResultChains':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The result_chains of this ResultChains.  # noqa: E501
        :rtype: ResultChains
        """
        return util.deserialize_model(dikt, cls)

    @property
    def chain_id(self) -> str:
        """Gets the chain_id of this ResultChains.


        :return: The chain_id of this ResultChains.
        :rtype: str
        """
        return self._chain_id

    @chain_id.setter
    def chain_id(self, chain_id: str):
        """Sets the chain_id of this ResultChains.


        :param chain_id: The chain_id of this ResultChains.
        :type chain_id: str
        """

        self._chain_id = chain_id

    @property
    def segments(self) -> List[ResultSegments]:
        """Gets the segments of this ResultChains.


        :return: The segments of this ResultChains.
        :rtype: List[ResultSegments]
        """
        return self._segments

    @segments.setter
    def segments(self, segments: List[ResultSegments]):
        """Sets the segments of this ResultChains.


        :param segments: The segments of this ResultChains.
        :type segments: List[ResultSegments]
        """

        self._segments = segments