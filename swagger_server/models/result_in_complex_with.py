# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.result_interacting_pdb_residues import ResultInteractingPDBResidues  # noqa: F401,E501
from swagger_server import util


class ResultInComplexWith(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, chain_id: str=None, description: str=None, interacting_pdb_residues: List[ResultInteractingPDBResidues]=None):  # noqa: E501
        """ResultInComplexWith - a model defined in Swagger

        :param chain_id: The chain_id of this ResultInComplexWith.  # noqa: E501
        :type chain_id: str
        :param description: The description of this ResultInComplexWith.  # noqa: E501
        :type description: str
        :param interacting_pdb_residues: The interacting_pdb_residues of this ResultInComplexWith.  # noqa: E501
        :type interacting_pdb_residues: List[ResultInteractingPDBResidues]
        """
        self.swagger_types = {
            'chain_id': str,
            'description': str,
            'interacting_pdb_residues': List[ResultInteractingPDBResidues]
        }

        self.attribute_map = {
            'chain_id': 'chain_id',
            'description': 'description',
            'interacting_pdb_residues': 'interacting_PDB_residues'
        }
        self._chain_id = chain_id
        self._description = description
        self._interacting_pdb_residues = interacting_pdb_residues

    @classmethod
    def from_dict(cls, dikt) -> 'ResultInComplexWith':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The result_in_complex_with of this ResultInComplexWith.  # noqa: E501
        :rtype: ResultInComplexWith
        """
        return util.deserialize_model(dikt, cls)

    @property
    def chain_id(self) -> str:
        """Gets the chain_id of this ResultInComplexWith.


        :return: The chain_id of this ResultInComplexWith.
        :rtype: str
        """
        return self._chain_id

    @chain_id.setter
    def chain_id(self, chain_id: str):
        """Sets the chain_id of this ResultInComplexWith.


        :param chain_id: The chain_id of this ResultInComplexWith.
        :type chain_id: str
        """

        self._chain_id = chain_id

    @property
    def description(self) -> str:
        """Gets the description of this ResultInComplexWith.


        :return: The description of this ResultInComplexWith.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this ResultInComplexWith.


        :param description: The description of this ResultInComplexWith.
        :type description: str
        """

        self._description = description

    @property
    def interacting_pdb_residues(self) -> List[ResultInteractingPDBResidues]:
        """Gets the interacting_pdb_residues of this ResultInComplexWith.


        :return: The interacting_pdb_residues of this ResultInComplexWith.
        :rtype: List[ResultInteractingPDBResidues]
        """
        return self._interacting_pdb_residues

    @interacting_pdb_residues.setter
    def interacting_pdb_residues(self, interacting_pdb_residues: List[ResultInteractingPDBResidues]):
        """Sets the interacting_pdb_residues of this ResultInComplexWith.


        :param interacting_pdb_residues: The interacting_pdb_residues of this ResultInComplexWith.
        :type interacting_pdb_residues: List[ResultInteractingPDBResidues]
        """

        self._interacting_pdb_residues = interacting_pdb_residues