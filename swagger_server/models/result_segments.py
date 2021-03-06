# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.result_residues import ResultResidues  # noqa: F401,E501
from swagger_server.models.result_seqres import ResultSeqres  # noqa: F401,E501
from swagger_server.models.result_template import ResultTemplate  # noqa: F401,E501
from swagger_server.models.result_uniprot import ResultUniprot  # noqa: F401,E501
from swagger_server import util


class ResultSegments(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, template: ResultTemplate=None, seqres: ResultSeqres=None, uniprot: ResultUniprot=None, residues: List[ResultResidues]=None):  # noqa: E501
        """ResultSegments - a model defined in Swagger

        :param template: The template of this ResultSegments.  # noqa: E501
        :type template: ResultTemplate
        :param seqres: The seqres of this ResultSegments.  # noqa: E501
        :type seqres: ResultSeqres
        :param uniprot: The uniprot of this ResultSegments.  # noqa: E501
        :type uniprot: ResultUniprot
        :param residues: The residues of this ResultSegments.  # noqa: E501
        :type residues: List[ResultResidues]
        """
        self.swagger_types = {
            'template': ResultTemplate,
            'seqres': ResultSeqres,
            'uniprot': ResultUniprot,
            'residues': List[ResultResidues]
        }

        self.attribute_map = {
            'template': 'template',
            'seqres': 'seqres',
            'uniprot': 'uniprot',
            'residues': 'residues'
        }
        self._template = template
        self._seqres = seqres
        self._uniprot = uniprot
        self._residues = residues

    @classmethod
    def from_dict(cls, dikt) -> 'ResultSegments':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The result_segments of this ResultSegments.  # noqa: E501
        :rtype: ResultSegments
        """
        return util.deserialize_model(dikt, cls)

    @property
    def template(self) -> ResultTemplate:
        """Gets the template of this ResultSegments.


        :return: The template of this ResultSegments.
        :rtype: ResultTemplate
        """
        return self._template

    @template.setter
    def template(self, template: ResultTemplate):
        """Sets the template of this ResultSegments.


        :param template: The template of this ResultSegments.
        :type template: ResultTemplate
        """

        self._template = template

    @property
    def seqres(self) -> ResultSeqres:
        """Gets the seqres of this ResultSegments.


        :return: The seqres of this ResultSegments.
        :rtype: ResultSeqres
        """
        return self._seqres

    @seqres.setter
    def seqres(self, seqres: ResultSeqres):
        """Sets the seqres of this ResultSegments.


        :param seqres: The seqres of this ResultSegments.
        :type seqres: ResultSeqres
        """

        self._seqres = seqres

    @property
    def uniprot(self) -> ResultUniprot:
        """Gets the uniprot of this ResultSegments.


        :return: The uniprot of this ResultSegments.
        :rtype: ResultUniprot
        """
        return self._uniprot

    @uniprot.setter
    def uniprot(self, uniprot: ResultUniprot):
        """Sets the uniprot of this ResultSegments.


        :param uniprot: The uniprot of this ResultSegments.
        :type uniprot: ResultUniprot
        """

        self._uniprot = uniprot

    @property
    def residues(self) -> List[ResultResidues]:
        """Gets the residues of this ResultSegments.


        :return: The residues of this ResultSegments.
        :rtype: List[ResultResidues]
        """
        return self._residues

    @residues.setter
    def residues(self, residues: List[ResultResidues]):
        """Sets the residues of this ResultSegments.


        :param residues: The residues of this ResultSegments.
        :type residues: List[ResultResidues]
        """

        self._residues = residues
