from typing import Optional

from brandfolder.resource import Resource
from brandfolder.resource_container import ResourceContainer
from brandfolder.asset import Asset
from brandfolder.collection import Collection
from brandfolder.section import Section


class Brandfolder(Resource):

    def __init__(self, client, data):
        super().__init__(client, data, 'Brandfolder', 'brandfolders')

        self.assets = ResourceContainer(client, Asset, 'assets', parent=self)
        self.collections = ResourceContainer(client, Collection, 'collections', parent=self, include=True)
        self.sections = ResourceContainer(client, Section, 'sections', parent=self, include=True)

    def __repr__(self):
        return f'<{self.resource_name} {self.attributes["slug"]}>'

    def create_asset(self, attachments_data, section_key, **attributes):
        data = {
          'data': {
            'attributes': [
              {
                **attributes,
                'attachments': attachments_data
              }
            ]
          },
          'section_key': section_key
        }

        res = self.client.post(f'/{self.resource_type}/{self.id}/assets', json=data)
        return Asset(self.client, res['data'][0])

    def create_collection(self, **attributes):
        data = {
          'data': {
            'attributes': attributes
          }
        }

        res = self.client.post(f'/{self.resource_type}/{self.id}/collections', json=data)
        return Collection(self.client, res['data'])

    def create_section(self, **attributes):
        data = {
            'data': {
                'attributes': attributes
            }
        }

        res = self.client.post(f'/{self.resource_type}/{self.id}/sections', json=data)
        return Section(self.client, res['data'])
