import graphene

from .services import AuthorServices, LabelServices, PublisherServices


class GenericType(graphene.ObjectType):
    id = graphene.UUID()
    name = graphene.String()
    last_update = graphene.DateTime()


class GenericResponse(graphene.ObjectType):
    has_next = graphene.Boolean()
    data = graphene.List(GenericType)


class Query(graphene.ObjectType):
    # author
    author_by_name = graphene.Field(GenericType, name=graphene.String(required=True))

    @staticmethod
    def resolve_author_by_name(self, info, name):
        return AuthorServices.get_by_name(name=name)

    author_by_uuid = graphene.Field(GenericType, uuid=graphene.UUID(required=True))

    @staticmethod
    def resolve_author_by_uuid(self, info, uuid):
        return AuthorServices.get_by_id(uid=uuid)

    author_get_all = graphene.Field(GenericResponse, first=graphene.Int(), limit=graphene.Int())

    @staticmethod
    def resolve_author_get_all(self, info, first=0, limit=20):
        authors = AuthorServices.get_all()[first: first + limit]
        return {
            'has_next': len(authors) == limit,
            'data': authors
        }

    # label
    label_by_name = graphene.Field(GenericType, name=graphene.String(required=True))

    @staticmethod
    def resolve_label_by_name(self, info, name):
        return LabelServices.get_by_name(name=name)

    label_by_uuid = graphene.Field(GenericType, uuid=graphene.UUID(required=True))

    @staticmethod
    def resolve_label_by_uuid(self, info, uuid):
        return LabelServices.get_by_id(uid=uuid)

    label_get_all = graphene.Field(GenericResponse, first=graphene.Int(), limit=graphene.Int())

    @staticmethod
    def resolve_label_get_all(self, info, first=0, limit=20):
        labels = LabelServices.get_all()[first: first + limit]
        return {
            'has_next': len(labels) == limit,
            'data': labels
        }

    # publisher
    publisher_by_name = graphene.Field(GenericType, name=graphene.String(required=True))

    @staticmethod
    def resolve_publisher_by_name(self, info, name):
        return PublisherServices.get_by_name(name=name)

    publisher_by_uuid = graphene.Field(GenericType, publisher_uuid=graphene.UUID())

    @staticmethod
    def resolve_publisher_by_uuid(self, info, publisher_uuid):
        return PublisherServices.get_by_id(uid=publisher_uuid)

    publisher_get_all = graphene.Field(GenericResponse, first=graphene.Int(), limit=graphene.Int())

    @staticmethod
    def resolve_publisher_get_all(self, info, first=0, limit=20):
        publishers = PublisherServices.get_all()[first: first + limit]
        return {
            'has_next': len(publishers) == limit,
            'data': publishers
        }
