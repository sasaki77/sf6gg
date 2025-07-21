import sgqlc.types
import sgqlc.types.relay


ggschema = sgqlc.types.Schema()


# Unexport Node/PageInfo, let schema re-declare them
ggschema -= sgqlc.types.relay.Node
ggschema -= sgqlc.types.relay.PageInfo


__docformat__ = 'markdown'


########################################################################
# Scalars and Enumerations
########################################################################
class ActivityState(sgqlc.types.Enum):
    '''Represents the state of an activity

    Enumeration Choices:

    * `ACTIVE`: Activity is active or in progress
    * `CALLED`: Activity, like a set, has been called to start
    * `COMPLETED`: Activity is done
    * `CREATED`: Activity is created
    * `INVALID`: Activity is invalid
    * `QUEUED`: Activity is queued to run
    * `READY`: Activity is ready to be started
    '''
    __schema__ = ggschema
    __choices__ = ('ACTIVE', 'CALLED', 'COMPLETED', 'CREATED', 'INVALID', 'QUEUED', 'READY')


class AuthorizationType(sgqlc.types.Enum):
    '''Represents the name of the third-party service (e.g Twitter) for
    OAuth

    Enumeration Choices:

    * `BATTLENET`
    * `DISCORD`
    * `EPIC`
    * `MIXER`
    * `RIOT`
    * `STEAM`
    * `TWITCH`
    * `TWITTER`
    * `XBOX`
    '''
    __schema__ = ggschema
    __choices__ = ('BATTLENET', 'DISCORD', 'EPIC', 'MIXER', 'RIOT', 'STEAM', 'TWITCH', 'TWITTER', 'XBOX')


Boolean = sgqlc.types.Boolean

class BracketType(sgqlc.types.Enum):
    '''The type of Bracket format that a Phase is configured with.

    Enumeration Choices:

    * `CIRCUIT`
    * `CUSTOM_SCHEDULE`
    * `DOUBLE_ELIMINATION`
    * `ELIMINATION_ROUNDS`
    * `EXHIBITION`
    * `MATCHMAKING`
    * `RACE`
    * `ROUND_ROBIN`
    * `SINGLE_ELIMINATION`
    * `SWISS`
    '''
    __schema__ = ggschema
    __choices__ = ('CIRCUIT', 'CUSTOM_SCHEDULE', 'DOUBLE_ELIMINATION', 'ELIMINATION_ROUNDS', 'EXHIBITION', 'MATCHMAKING', 'RACE', 'ROUND_ROBIN', 'SINGLE_ELIMINATION', 'SWISS')


class Comparator(sgqlc.types.Enum):
    '''Comparison operator

    Enumeration Choices:

    * `EQUAL`
    * `GREATER_THAN`
    * `GREATER_THAN_OR_EQUAL`
    * `LESS_THAN`
    * `LESS_THAN_OR_EQUAL`
    '''
    __schema__ = ggschema
    __choices__ = ('EQUAL', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'LESS_THAN', 'LESS_THAN_OR_EQUAL')


Float = sgqlc.types.Float

class GameSelectionType(sgqlc.types.Enum):
    '''The type of selection i.e. is it for a character or something else

    Enumeration Choices:

    * `CHARACTER`: Character selection
    '''
    __schema__ = ggschema
    __choices__ = ('CHARACTER',)


ID = sgqlc.types.ID

Int = sgqlc.types.Int

class JSON(sgqlc.types.Scalar):
    '''The `JSON` scalar type represents JSON values as specified by
    [ECMA-404](http://www.ecma-
    international.org/publications/files/ECMA-ST/ECMA-404.pdf).
    '''
    __schema__ = ggschema


class MatchConfigVerificationMethod(sgqlc.types.Enum):
    '''Different options available for verifying player-reported match
    results

    Enumeration Choices:

    * `ANY`
    * `MIXER`
    * `STREAM_ME`
    * `TWITCH`
    * `YOUTUBE`
    '''
    __schema__ = ggschema
    __choices__ = ('ANY', 'MIXER', 'STREAM_ME', 'TWITCH', 'YOUTUBE')


class RaceLimitMode(sgqlc.types.Enum):
    '''Enforces limits on the amount of allowable Race submissions

    Enumeration Choices:

    * `BEST_ALL`
    * `FIRST_ALL`
    * `PLAYTIME`
    '''
    __schema__ = ggschema
    __choices__ = ('BEST_ALL', 'FIRST_ALL', 'PLAYTIME')


class RaceType(sgqlc.types.Enum):
    '''Race type

    Enumeration Choices:

    * `GOALS`
    * `TIMED`
    '''
    __schema__ = ggschema
    __choices__ = ('GOALS', 'TIMED')


class SetSortType(sgqlc.types.Enum):
    '''Different sort type configurations used when displaying multiple
    sets

    Enumeration Choices:

    * `CALL_ORDER`: Sets are sorted in the suggested order that they
      be called to be played. The order of completed sets is reversed.
    * `MAGIC`: Sets are sorted by relevancy dependent on the state and
      progress of the event.
    * `NONE`: Sets will not be sorted.
    * `RECENT`: Sets are sorted in the order that they were started.
    * `ROUND`: Sets sorted by round and identifier
    * `STANDARD`: Deprecated. This is equivalent to CALL_ORDER
    '''
    __schema__ = ggschema
    __choices__ = ('CALL_ORDER', 'MAGIC', 'NONE', 'RECENT', 'ROUND', 'STANDARD')


class SocialConnectionType(sgqlc.types.Enum):
    '''Represents the name of the third-party social service (e.g
    Twitter) for OAuth

    Enumeration Choices:

    * `DISCORD`
    * `MIXER`
    * `TWITCH`
    * `TWITTER`
    * `XBOX`
    '''
    __schema__ = ggschema
    __choices__ = ('DISCORD', 'MIXER', 'TWITCH', 'TWITTER', 'XBOX')


class StreamSource(sgqlc.types.Enum):
    '''Represents the source of a stream

    Enumeration Choices:

    * `HITBOX`: Stream is on smashcast.tv channel
    * `MIXER`: Stream is on a mixer.com channel
    * `STREAMME`: Stream is on a stream.me channel
    * `TWITCH`: Stream is on twitch.tv channel
    * `YOUTUBE`: Stream is on a youtube.com channel
    '''
    __schema__ = ggschema
    __choices__ = ('HITBOX', 'MIXER', 'STREAMME', 'TWITCH', 'YOUTUBE')


class StreamType(sgqlc.types.Enum):
    '''Represents the type of stream service

    Enumeration Choices:

    * `MIXER`
    * `TWITCH`
    * `YOUTUBE`
    '''
    __schema__ = ggschema
    __choices__ = ('MIXER', 'TWITCH', 'YOUTUBE')


String = sgqlc.types.String

class TeamMemberStatus(sgqlc.types.Enum):
    '''Membership status of a team member

    Enumeration Choices:

    * `ACCEPTED`
    * `ALUM`
    * `HIATUS`
    * `INVITED`
    * `OPEN_SPOT`
    * `REQUEST`
    * `UNKNOWN`
    '''
    __schema__ = ggschema
    __choices__ = ('ACCEPTED', 'ALUM', 'HIATUS', 'INVITED', 'OPEN_SPOT', 'REQUEST', 'UNKNOWN')


class TeamMemberType(sgqlc.types.Enum):
    '''Membership type of a team member

    Enumeration Choices:

    * `PLAYER`
    * `STAFF`
    '''
    __schema__ = ggschema
    __choices__ = ('PLAYER', 'STAFF')


class Timestamp(sgqlc.types.Scalar):
    '''Represents a Unix Timestamp. Supports up to 53 bit int values,
    as that is JavaScript's internal memory allocation for integer
    values.
    '''
    __schema__ = ggschema


class TournamentPaginationSort(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `computedUpdatedAt`
    * `endAt`
    * `eventRegistrationClosesAt`
    * `startAt`
    '''
    __schema__ = ggschema
    __choices__ = ('computedUpdatedAt', 'endAt', 'eventRegistrationClosesAt', 'startAt')



########################################################################
# Input Objects
########################################################################
class BracketSetGameDataInput(sgqlc.types.Input):
    '''Game specific H2H set data such as character, stage, and stock
    info
    '''
    __schema__ = ggschema
    __field_names__ = ('winner_id', 'game_num', 'entrant1_score', 'entrant2_score', 'stage_id', 'selections')
    winner_id = sgqlc.types.Field(ID, graphql_name='winnerId')
    '''Entrant ID of game winner'''

    game_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='gameNum')
    '''Game number'''

    entrant1_score = sgqlc.types.Field(Int, graphql_name='entrant1Score')
    '''Score for entrant 1 (if applicable). For smash, this is stocks
    remaining.
    '''

    entrant2_score = sgqlc.types.Field(Int, graphql_name='entrant2Score')
    '''Score for entrant 2 (if applicable). For smash, this is stocks
    remaining.
    '''

    stage_id = sgqlc.types.Field(ID, graphql_name='stageId')
    '''ID of the stage that was played for this game (if applicable)'''

    selections = sgqlc.types.Field(sgqlc.types.list_of('BracketSetGameSelectionInput'), graphql_name='selections')
    '''List of selections for the game, typically character selections.'''



class BracketSetGameSelectionInput(sgqlc.types.Input):
    '''Game specific H2H selections made by the entrants, such as
    character info
    '''
    __schema__ = ggschema
    __field_names__ = ('entrant_id', 'character_id')
    entrant_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='entrantId')
    '''Entrant ID that made selection'''

    character_id = sgqlc.types.Field(Int, graphql_name='characterId')
    '''Character selected by this entrant for this game.'''



class EventEntrantPageQuery(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('page', 'per_page', 'sort_by', 'filter')
    page = sgqlc.types.Field(Int, graphql_name='page')

    per_page = sgqlc.types.Field(Int, graphql_name='perPage')

    sort_by = sgqlc.types.Field(String, graphql_name='sortBy')

    filter = sgqlc.types.Field('EventEntrantPageQueryFilter', graphql_name='filter')



class EventEntrantPageQueryFilter(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(String, graphql_name='name')



class EventFilter(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('videogame_id', 'type', 'published', 'id', 'ids', 'slug', 'fantasy_event_id', 'fantasy_roster_hash')
    videogame_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='videogameId')

    type = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='type')

    published = sgqlc.types.Field(Boolean, graphql_name='published')

    id = sgqlc.types.Field(ID, graphql_name='id')

    ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='ids')

    slug = sgqlc.types.Field(String, graphql_name='slug')

    fantasy_event_id = sgqlc.types.Field(ID, graphql_name='fantasyEventId')

    fantasy_roster_hash = sgqlc.types.Field(String, graphql_name='fantasyRosterHash')



class EventOwnersQuery(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('page', 'per_page', 'sort_by')
    page = sgqlc.types.Field(Int, graphql_name='page')

    per_page = sgqlc.types.Field(Int, graphql_name='perPage')
    '''How many nodes to return for the page. Maximum value of 512'''

    sort_by = sgqlc.types.Field(String, graphql_name='sortBy')



class LeagueEventsFilter(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('search', 'point_mapping_group_ids', 'tier_ids', 'user_id', 'upcoming', 'league_entrant_id')
    search = sgqlc.types.Field('PaginationSearchType', graphql_name='search')

    point_mapping_group_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='pointMappingGroupIds')

    tier_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tierIds')

    user_id = sgqlc.types.Field(ID, graphql_name='userId')

    upcoming = sgqlc.types.Field(Boolean, graphql_name='upcoming')

    league_entrant_id = sgqlc.types.Field(ID, graphql_name='leagueEntrantId')



class LeagueEventsQuery(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('page', 'per_page', 'sort_by', 'filter')
    page = sgqlc.types.Field(Int, graphql_name='page')

    per_page = sgqlc.types.Field(Int, graphql_name='perPage')
    '''How many nodes to return for the page. Maximum value of 512'''

    sort_by = sgqlc.types.Field(String, graphql_name='sortBy')

    filter = sgqlc.types.Field(LeagueEventsFilter, graphql_name='filter')



class LeaguePageFilter(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('id', 'ids', 'owner_id', 'after_date', 'before_date', 'computed_updated_at', 'name', 'is_featured', 'has_banner_images', 'active_shops', 'past', 'published', 'publicly_searchable', 'upcoming', 'videogame_ids')
    id = sgqlc.types.Field(ID, graphql_name='id')

    ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='ids')

    owner_id = sgqlc.types.Field(ID, graphql_name='ownerId')
    '''ID of the user that owns this league.'''

    after_date = sgqlc.types.Field(Timestamp, graphql_name='afterDate')

    before_date = sgqlc.types.Field(Timestamp, graphql_name='beforeDate')

    computed_updated_at = sgqlc.types.Field(Timestamp, graphql_name='computedUpdatedAt')

    name = sgqlc.types.Field(String, graphql_name='name')

    is_featured = sgqlc.types.Field(Boolean, graphql_name='isFeatured')

    has_banner_images = sgqlc.types.Field(Boolean, graphql_name='hasBannerImages')

    active_shops = sgqlc.types.Field(Boolean, graphql_name='activeShops')

    past = sgqlc.types.Field(Boolean, graphql_name='past')

    published = sgqlc.types.Field(Boolean, graphql_name='published')

    publicly_searchable = sgqlc.types.Field(Boolean, graphql_name='publiclySearchable')

    upcoming = sgqlc.types.Field(Boolean, graphql_name='upcoming')

    videogame_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='videogameIds')



class LeagueQuery(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('page', 'per_page', 'sort_by', 'filter', 'sort')
    page = sgqlc.types.Field(Int, graphql_name='page')

    per_page = sgqlc.types.Field(Int, graphql_name='perPage')
    '''How many nodes to return for the page. Maximum value of 512'''

    sort_by = sgqlc.types.Field(String, graphql_name='sortBy')

    filter = sgqlc.types.Field(LeaguePageFilter, graphql_name='filter')

    sort = sgqlc.types.Field(TournamentPaginationSort, graphql_name='sort')



class LocationFilterType(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('country_code', 'state', 'city')
    country_code = sgqlc.types.Field(String, graphql_name='countryCode')

    state = sgqlc.types.Field(String, graphql_name='state')

    city = sgqlc.types.Field(String, graphql_name='city')



class PaginationSearchType(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('fields_to_search', 'search_string')
    fields_to_search = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='fieldsToSearch')

    search_string = sgqlc.types.Field(String, graphql_name='searchString')



class ParticipantPageFilter(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('id', 'ids', 'event_ids', 'search', 'gamer_tag', 'unpaid', 'incomplete_team', 'missing_deck', 'checked_in', 'not_checked_in')
    id = sgqlc.types.Field(ID, graphql_name='id')

    ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='ids')

    event_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='eventIds')

    search = sgqlc.types.Field(PaginationSearchType, graphql_name='search')

    gamer_tag = sgqlc.types.Field(String, graphql_name='gamerTag')

    unpaid = sgqlc.types.Field(Boolean, graphql_name='unpaid')

    incomplete_team = sgqlc.types.Field(Boolean, graphql_name='incompleteTeam')

    missing_deck = sgqlc.types.Field(Boolean, graphql_name='missingDeck')

    checked_in = sgqlc.types.Field(Boolean, graphql_name='checkedIn')

    not_checked_in = sgqlc.types.Field(Boolean, graphql_name='notCheckedIn')



class ParticipantPaginationQuery(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('page', 'per_page', 'sort_by', 'filter')
    page = sgqlc.types.Field(Int, graphql_name='page')

    per_page = sgqlc.types.Field(Int, graphql_name='perPage')
    '''How many nodes to return for the page. Maximum value of 512'''

    sort_by = sgqlc.types.Field(String, graphql_name='sortBy')

    filter = sgqlc.types.Field(ParticipantPageFilter, graphql_name='filter')



class PhaseGroupPageQuery(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('page', 'per_page', 'sort_by', 'entrant_ids', 'filter')
    page = sgqlc.types.Field(Int, graphql_name='page')

    per_page = sgqlc.types.Field(Int, graphql_name='perPage')

    sort_by = sgqlc.types.Field(String, graphql_name='sortBy')

    entrant_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='entrantIds')

    filter = sgqlc.types.Field('PhaseGroupPageQueryFilter', graphql_name='filter')



class PhaseGroupPageQueryFilter(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('id', 'wave_id')
    id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='id')

    wave_id = sgqlc.types.Field(ID, graphql_name='waveId')



class PhaseGroupUpdateInput(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('phase_group_id', 'station_id', 'wave_id')
    phase_group_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='phaseGroupId')

    station_id = sgqlc.types.Field(ID, graphql_name='stationId')

    wave_id = sgqlc.types.Field(ID, graphql_name='waveId')



class PhaseUpsertInput(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('name', 'group_count', 'bracket_type')
    name = sgqlc.types.Field(String, graphql_name='name')
    '''The name of the Phase. For example, "Top 8" or "Pools"'''

    group_count = sgqlc.types.Field(Int, graphql_name='groupCount')
    '''The number of pools to configure for the Phase. Only applies to
    brackets that support pools
    '''

    bracket_type = sgqlc.types.Field(BracketType, graphql_name='bracketType')



class ResolveConflictsLockedSeedConfig(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('event_id', 'num_seeds')
    event_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='eventId')

    num_seeds = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='numSeeds')



class ResolveConflictsOptions(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('locked_seeds',)
    locked_seeds = sgqlc.types.Field(sgqlc.types.list_of(ResolveConflictsLockedSeedConfig), graphql_name='lockedSeeds')



class SeedPageFilter(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('id', 'entrant_name', 'check_in_state', 'phase_group_id', 'event_check_in_group_id', 'phase_id', 'event_id', 'search')
    id = sgqlc.types.Field(ID, graphql_name='id')

    entrant_name = sgqlc.types.Field(String, graphql_name='entrantName')

    check_in_state = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='checkInState')

    phase_group_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='phaseGroupId')

    event_check_in_group_id = sgqlc.types.Field(ID, graphql_name='eventCheckInGroupId')

    phase_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='phaseId')

    event_id = sgqlc.types.Field(ID, graphql_name='eventId')

    search = sgqlc.types.Field(PaginationSearchType, graphql_name='search')



class SeedPaginationQuery(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('page', 'per_page', 'sort_by', 'filter')
    page = sgqlc.types.Field(Int, graphql_name='page')

    per_page = sgqlc.types.Field(Int, graphql_name='perPage')
    '''How many nodes to return for the page. Maximum value of 512'''

    sort_by = sgqlc.types.Field(String, graphql_name='sortBy')

    filter = sgqlc.types.Field(SeedPageFilter, graphql_name='filter')



class SetFilterLocation(sgqlc.types.Input):
    '''Filter Sets by geographical constraints.'''
    __schema__ = ggschema
    __field_names__ = ('state', 'country', 'distance_from')
    state = sgqlc.types.Field(String, graphql_name='state')
    '''Only return Sets in this state. Only applicable to US states'''

    country = sgqlc.types.Field(String, graphql_name='country')
    '''Only return Sets in this country. Expects a valid two-letter
    country code
    '''

    distance_from = sgqlc.types.Field('SetFilterLocationDistanceFrom', graphql_name='distanceFrom')



class SetFilterLocationDistanceFrom(sgqlc.types.Input):
    '''Only return Sets that are a certain distance away from a specified
    point
    '''
    __schema__ = ggschema
    __field_names__ = ('point', 'radius')
    point = sgqlc.types.Field('SetFilterLocationDistanceFromPoint', graphql_name='point')
    '''Point at which to perform distance calculation'''

    radius = sgqlc.types.Field(String, graphql_name='radius')
    '''Distance from the point to include results in'''



class SetFilterLocationDistanceFromPoint(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('lat', 'lon')
    lat = sgqlc.types.Field(Float, graphql_name='lat')

    lon = sgqlc.types.Field(Float, graphql_name='lon')



class SetFilters(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('entrant_ids', 'entrant_size', 'has_vod', 'hide_empty', 'show_byes', 'is_event_online', 'location', 'participant_ids', 'phase_group_ids', 'phase_ids', 'event_ids', 'tournament_ids', 'player_ids', 'round_number', 'state', 'station_ids', 'station_numbers', 'updated_after')
    entrant_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='entrantIds')
    '''Only return Sets for these Entrants'''

    entrant_size = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='entrantSize')
    '''Only return Sets for this Entrant size. For example, to fetch 1v1
    Sets only, filter by an entrantSize of 1
    '''

    has_vod = sgqlc.types.Field(Boolean, graphql_name='hasVod')
    '''Only return Sets that have an attached VOD'''

    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    '''Do not return empty Sets. For example, set this to true to filter
    out sets that are waiting for progressions.
    '''

    show_byes = sgqlc.types.Field(Boolean, graphql_name='showByes')
    '''Return sets that contain a bye'''

    is_event_online = sgqlc.types.Field(Boolean, graphql_name='isEventOnline')
    '''Only return Sets that are in an Online event. If omitted, Sets for
    both online and offline Events are returned
    '''

    location = sgqlc.types.Field(SetFilterLocation, graphql_name='location')
    '''Only return Sets in certain geographical areas.'''

    participant_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='participantIds')
    '''Only return Sets for these Participants'''

    phase_group_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='phaseGroupIds')
    '''Only return Sets in these PhaseGroups'''

    phase_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='phaseIds')
    '''Only return Sets in these Phases'''

    event_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='eventIds')
    '''Only return Sets in these Events'''

    tournament_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tournamentIds')
    '''Only return Sets in these Tournaments'''

    player_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='playerIds')
    '''Only return Sets for these Players'''

    round_number = sgqlc.types.Field(Int, graphql_name='roundNumber')
    '''Only return Sets for these Rounds'''

    state = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='state')
    '''Only returns Sets that are in these states'''

    station_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='stationIds')
    '''Only return Sets that are assigned to these Station IDs'''

    station_numbers = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='stationNumbers')
    '''Only return Sets that are assigned to these Station numbers'''

    updated_after = sgqlc.types.Field(Timestamp, graphql_name='updatedAfter')
    '''Only return sets created or updated since this timestamp'''



class ShopLevelsQuery(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('page', 'per_page', 'sort_by')
    page = sgqlc.types.Field(Int, graphql_name='page')

    per_page = sgqlc.types.Field(Int, graphql_name='perPage')
    '''How many nodes to return for the page. Maximum value of 512'''

    sort_by = sgqlc.types.Field(String, graphql_name='sortBy')



class ShopOrderMessagesQuery(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('page', 'per_page', 'sort_by')
    page = sgqlc.types.Field(Int, graphql_name='page')

    per_page = sgqlc.types.Field(Int, graphql_name='perPage')
    '''How many nodes to return for the page. Maximum value of 512'''

    sort_by = sgqlc.types.Field(String, graphql_name='sortBy')



class StandingGroupStandingPageFilter(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('page', 'per_page', 'sort_by')
    page = sgqlc.types.Field(Int, graphql_name='page')

    per_page = sgqlc.types.Field(Int, graphql_name='perPage')

    sort_by = sgqlc.types.Field(String, graphql_name='sortBy')



class StandingPageFilter(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('id', 'ids', 'search')
    id = sgqlc.types.Field(ID, graphql_name='id')

    ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='ids')

    search = sgqlc.types.Field(PaginationSearchType, graphql_name='search')



class StandingPaginationQuery(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('page', 'per_page', 'sort_by', 'filter')
    page = sgqlc.types.Field(Int, graphql_name='page')

    per_page = sgqlc.types.Field(Int, graphql_name='perPage')
    '''How many nodes to return for the page. Maximum value of 512'''

    sort_by = sgqlc.types.Field(String, graphql_name='sortBy')

    filter = sgqlc.types.Field(StandingPageFilter, graphql_name='filter')



class StationFilter(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('page', 'per_page')
    page = sgqlc.types.Field(Int, graphql_name='page')

    per_page = sgqlc.types.Field(Int, graphql_name='perPage')



class StationUpsertInput(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('number', 'cluster_id')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')

    cluster_id = sgqlc.types.Field(ID, graphql_name='clusterId')



class TeamPaginationFilter(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('global_team_id', 'event_state', 'event_id', 'event_ids', 'min_entrant_count', 'max_entrant_count', 'search', 'type', 'tournament_id', 'member_status', 'videogame_id', 'is_league', 'upcoming', 'past', 'roster_complete', 'roster_incomplete')
    global_team_id = sgqlc.types.Field(ID, graphql_name='globalTeamId')

    event_state = sgqlc.types.Field(ActivityState, graphql_name='eventState')

    event_id = sgqlc.types.Field(ID, graphql_name='eventId')

    event_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='eventIds')

    min_entrant_count = sgqlc.types.Field(Int, graphql_name='minEntrantCount')

    max_entrant_count = sgqlc.types.Field(Int, graphql_name='maxEntrantCount')

    search = sgqlc.types.Field(PaginationSearchType, graphql_name='search')

    type = sgqlc.types.Field(Int, graphql_name='type')

    tournament_id = sgqlc.types.Field(ID, graphql_name='tournamentId')

    member_status = sgqlc.types.Field(sgqlc.types.list_of(TeamMemberStatus), graphql_name='memberStatus')

    videogame_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='videogameId')

    is_league = sgqlc.types.Field(Boolean, graphql_name='isLeague')

    upcoming = sgqlc.types.Field(Boolean, graphql_name='upcoming')

    past = sgqlc.types.Field(Boolean, graphql_name='past')

    roster_complete = sgqlc.types.Field(Boolean, graphql_name='rosterComplete')

    roster_incomplete = sgqlc.types.Field(Boolean, graphql_name='rosterIncomplete')



class TeamPaginationQuery(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('page', 'per_page', 'sort_by', 'filter')
    page = sgqlc.types.Field(Int, graphql_name='page')

    per_page = sgqlc.types.Field(Int, graphql_name='perPage')
    '''How many nodes to return for the page. Maximum value of 512'''

    sort_by = sgqlc.types.Field(String, graphql_name='sortBy')

    filter = sgqlc.types.Field(TeamPaginationFilter, graphql_name='filter')



class TopGameFilter(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('game_nums',)
    game_nums = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='gameNums')
    '''Array of which # top game you want to filter on.e.g. [2, 3] will
    filter on the 2nd and 3rd top games
    '''



class TournamentLocationFilter(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('distance_from', 'distance')
    distance_from = sgqlc.types.Field(String, graphql_name='distanceFrom')
    '''Latitude, Longitude'''

    distance = sgqlc.types.Field(String, graphql_name='distance')
    '''e.g. 50mi'''



class TournamentPageFilter(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('id', 'ids', 'owner_id', 'is_current_user_admin', 'country_code', 'addr_state', 'location', 'after_date', 'before_date', 'computed_updated_at', 'name', 'venue_name', 'is_featured', 'is_league', 'has_banner_images', 'active_shops', 'reg_open', 'past', 'published', 'publicly_searchable', 'staff_picks', 'has_online_events', 'top_games', 'upcoming', 'videogame_ids', 'sort_by_score')
    id = sgqlc.types.Field(ID, graphql_name='id')

    ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='ids')

    owner_id = sgqlc.types.Field(ID, graphql_name='ownerId')
    '''ID of the user that owns this tournament.'''

    is_current_user_admin = sgqlc.types.Field(Boolean, graphql_name='isCurrentUserAdmin')
    '''If true, filter to only tournaments the currently authed user is
    an admin of
    '''

    country_code = sgqlc.types.Field(String, graphql_name='countryCode')

    addr_state = sgqlc.types.Field(String, graphql_name='addrState')

    location = sgqlc.types.Field(TournamentLocationFilter, graphql_name='location')

    after_date = sgqlc.types.Field(Timestamp, graphql_name='afterDate')

    before_date = sgqlc.types.Field(Timestamp, graphql_name='beforeDate')

    computed_updated_at = sgqlc.types.Field(Timestamp, graphql_name='computedUpdatedAt')

    name = sgqlc.types.Field(String, graphql_name='name')

    venue_name = sgqlc.types.Field(String, graphql_name='venueName')

    is_featured = sgqlc.types.Field(Boolean, graphql_name='isFeatured')

    is_league = sgqlc.types.Field(Boolean, graphql_name='isLeague')

    has_banner_images = sgqlc.types.Field(Boolean, graphql_name='hasBannerImages')

    active_shops = sgqlc.types.Field(Boolean, graphql_name='activeShops')

    reg_open = sgqlc.types.Field(Boolean, graphql_name='regOpen')

    past = sgqlc.types.Field(Boolean, graphql_name='past')

    published = sgqlc.types.Field(Boolean, graphql_name='published')

    publicly_searchable = sgqlc.types.Field(Boolean, graphql_name='publiclySearchable')

    staff_picks = sgqlc.types.Field(Boolean, graphql_name='staffPicks')

    has_online_events = sgqlc.types.Field(Boolean, graphql_name='hasOnlineEvents')

    top_games = sgqlc.types.Field(TopGameFilter, graphql_name='topGames')

    upcoming = sgqlc.types.Field(Boolean, graphql_name='upcoming')

    videogame_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='videogameIds')

    sort_by_score = sgqlc.types.Field(Boolean, graphql_name='sortByScore')



class TournamentQuery(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('page', 'per_page', 'sort_by', 'filter', 'sort')
    page = sgqlc.types.Field(Int, graphql_name='page')

    per_page = sgqlc.types.Field(Int, graphql_name='perPage')
    '''How many nodes to return for the page. Maximum value of 512'''

    sort_by = sgqlc.types.Field(String, graphql_name='sortBy')

    filter = sgqlc.types.Field(TournamentPageFilter, graphql_name='filter')

    sort = sgqlc.types.Field(TournamentPaginationSort, graphql_name='sort')



class TournamentRegistrationInput(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('event_ids',)
    event_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='eventIds')



class UpdatePhaseSeedInfo(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('seed_id', 'seed_num', 'phase_group_id')
    seed_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='seedId')

    seed_num = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='seedNum')

    phase_group_id = sgqlc.types.Field(ID, graphql_name='phaseGroupId')



class UpdatePhaseSeedingOptions(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('strict_mode',)
    strict_mode = sgqlc.types.Field(Boolean, graphql_name='strictMode')
    '''Validate that seedMapping exactly accounts for all entrants in the
    phase
    '''



class UserEventsPaginationFilter(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('videogame_id', 'event_type', 'min_entrant_count', 'max_entrant_count', 'location', 'search')
    videogame_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='videogameId')

    event_type = sgqlc.types.Field(Int, graphql_name='eventType')

    min_entrant_count = sgqlc.types.Field(Int, graphql_name='minEntrantCount')

    max_entrant_count = sgqlc.types.Field(Int, graphql_name='maxEntrantCount')

    location = sgqlc.types.Field(LocationFilterType, graphql_name='location')

    search = sgqlc.types.Field(PaginationSearchType, graphql_name='search')



class UserEventsPaginationQuery(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('page', 'per_page', 'sort_by', 'filter')
    page = sgqlc.types.Field(Int, graphql_name='page')

    per_page = sgqlc.types.Field(Int, graphql_name='perPage')
    '''How many nodes to return for the page. Maximum value of 512'''

    sort_by = sgqlc.types.Field(String, graphql_name='sortBy')

    filter = sgqlc.types.Field(UserEventsPaginationFilter, graphql_name='filter')



class UserLeaguesPaginationFilter(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('videogame_id', 'upcoming', 'past', 'search')
    videogame_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='videogameId')

    upcoming = sgqlc.types.Field(Boolean, graphql_name='upcoming')

    past = sgqlc.types.Field(Boolean, graphql_name='past')

    search = sgqlc.types.Field(PaginationSearchType, graphql_name='search')



class UserLeaguesPaginationQuery(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('page', 'per_page', 'sort_by', 'filter')
    page = sgqlc.types.Field(Int, graphql_name='page')

    per_page = sgqlc.types.Field(Int, graphql_name='perPage')
    '''How many nodes to return for the page. Maximum value of 512'''

    sort_by = sgqlc.types.Field(String, graphql_name='sortBy')

    filter = sgqlc.types.Field(UserLeaguesPaginationFilter, graphql_name='filter')



class UserTournamentsPaginationFilter(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('past', 'upcoming', 'search', 'videogame_id', 'tournament_view', 'exclude_id')
    past = sgqlc.types.Field(Boolean, graphql_name='past')

    upcoming = sgqlc.types.Field(Boolean, graphql_name='upcoming')

    search = sgqlc.types.Field(PaginationSearchType, graphql_name='search')

    videogame_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='videogameId')

    tournament_view = sgqlc.types.Field(String, graphql_name='tournamentView')

    exclude_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeId')



class UserTournamentsPaginationQuery(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('page', 'per_page', 'sort_by', 'filter')
    page = sgqlc.types.Field(Int, graphql_name='page')

    per_page = sgqlc.types.Field(Int, graphql_name='perPage')
    '''How many nodes to return for the page. Maximum value of 512'''

    sort_by = sgqlc.types.Field(String, graphql_name='sortBy')

    filter = sgqlc.types.Field(UserTournamentsPaginationFilter, graphql_name='filter')



class VideogamePageFilter(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('id', 'name', 'for_user')
    id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='id')

    name = sgqlc.types.Field(String, graphql_name='name')

    for_user = sgqlc.types.Field(ID, graphql_name='forUser')



class VideogameQuery(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('page', 'per_page', 'sort_by', 'filter')
    page = sgqlc.types.Field(Int, graphql_name='page')

    per_page = sgqlc.types.Field(Int, graphql_name='perPage')
    '''How many nodes to return for the page. Maximum value of 512'''

    sort_by = sgqlc.types.Field(String, graphql_name='sortBy')

    filter = sgqlc.types.Field(VideogamePageFilter, graphql_name='filter')



class WaveUpsertInput(sgqlc.types.Input):
    __schema__ = ggschema
    __field_names__ = ('identifier', 'start_at', 'end_at')
    identifier = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='identifier')

    start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startAt')

    end_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endAt')




########################################################################
# Output Objects and Interfaces
########################################################################
class ActionSet(sgqlc.types.Interface):
    '''A set of actions available for an entity to take'''
    __schema__ = ggschema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(ID, graphql_name='id')



class BracketConfig(sgqlc.types.Interface):
    '''Bracket-specific configuration'''
    __schema__ = ggschema
    __field_names__ = ('id', 'bracket_type')
    id = sgqlc.types.Field(ID, graphql_name='id')

    bracket_type = sgqlc.types.Field(BracketType, graphql_name='bracketType')



class MatchConfig(sgqlc.types.Interface):
    '''Match-level configuration'''
    __schema__ = ggschema
    __field_names__ = ('id', 'bracket_type')
    id = sgqlc.types.Field(ID, graphql_name='id')

    bracket_type = sgqlc.types.Field(BracketType, graphql_name='bracketType')



class Team(sgqlc.types.Interface):
    '''A team, either at the global level or within the context of an
    event
    '''
    __schema__ = ggschema
    __field_names__ = ('id', 'discriminator', 'images', 'members', 'name')
    id = sgqlc.types.Field(ID, graphql_name='id')

    discriminator = sgqlc.types.Field(String, graphql_name='discriminator')
    '''Uniquely identifying token for team. Same as the hashed part of
    the slug
    '''

    images = sgqlc.types.Field(sgqlc.types.list_of('Image'), graphql_name='images', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    '''Arguments:

    * `type` (`String`)None
    '''

    members = sgqlc.types.Field(sgqlc.types.list_of('TeamMember'), graphql_name='members', args=sgqlc.types.ArgDict((
        ('status', sgqlc.types.Arg(sgqlc.types.list_of(TeamMemberStatus), graphql_name='status', default=None)),
))
    )
    '''Arguments:

    * `status` (`[TeamMemberStatus]`)None
    '''

    name = sgqlc.types.Field(String, graphql_name='name')



class Address(sgqlc.types.Type):
    '''A user's address'''
    __schema__ = ggschema
    __field_names__ = ('id', 'city', 'country', 'country_id', 'state', 'state_id')
    id = sgqlc.types.Field(ID, graphql_name='id')

    city = sgqlc.types.Field(String, graphql_name='city')

    country = sgqlc.types.Field(String, graphql_name='country')

    country_id = sgqlc.types.Field(Int, graphql_name='countryId')

    state = sgqlc.types.Field(String, graphql_name='state')

    state_id = sgqlc.types.Field(Int, graphql_name='stateId')



class Character(sgqlc.types.Type):
    '''A character in a videogame'''
    __schema__ = ggschema
    __field_names__ = ('id', 'images', 'name')
    id = sgqlc.types.Field(ID, graphql_name='id')

    images = sgqlc.types.Field(sgqlc.types.list_of('Image'), graphql_name='images', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    '''Arguments:

    * `type` (`String`)None
    '''

    name = sgqlc.types.Field(String, graphql_name='name')
    '''Name of Character'''



class ContactInfo(sgqlc.types.Type):
    '''Name, address, etc'''
    __schema__ = ggschema
    __field_names__ = ('id', 'city', 'country', 'country_id', 'name', 'name_first', 'name_last', 'state', 'state_id', 'zipcode')
    id = sgqlc.types.Field(ID, graphql_name='id')

    city = sgqlc.types.Field(String, graphql_name='city')
    '''Participant City Name'''

    country = sgqlc.types.Field(String, graphql_name='country')
    '''Participant Country Name'''

    country_id = sgqlc.types.Field(Int, graphql_name='countryId')
    '''Participant Country (region) id'''

    name = sgqlc.types.Field(String, graphql_name='name')

    name_first = sgqlc.types.Field(String, graphql_name='nameFirst')
    '''First Name'''

    name_last = sgqlc.types.Field(String, graphql_name='nameLast')
    '''Last Name'''

    state = sgqlc.types.Field(String, graphql_name='state')
    '''Participant State Name'''

    state_id = sgqlc.types.Field(Int, graphql_name='stateId')
    '''Participant State (region) id'''

    zipcode = sgqlc.types.Field(String, graphql_name='zipcode')
    '''Zip or Postal Code'''



class Entrant(sgqlc.types.Type):
    '''An entrant in an event'''
    __schema__ = ggschema
    __field_names__ = ('id', 'event', 'initial_seed_num', 'is_disqualified', 'name', 'paginated_sets', 'participants', 'seeds', 'skill', 'standing', 'streams', 'team')
    id = sgqlc.types.Field(ID, graphql_name='id')

    event = sgqlc.types.Field('Event', graphql_name='event')

    initial_seed_num = sgqlc.types.Field(Int, graphql_name='initialSeedNum')
    '''Entrant's seed number in the first phase of the event.'''

    is_disqualified = sgqlc.types.Field(Boolean, graphql_name='isDisqualified')

    name = sgqlc.types.Field(String, graphql_name='name')
    '''The entrant name as it appears in bracket: gamerTag of the
    participant or team name
    '''

    paginated_sets = sgqlc.types.Field('SetConnection', graphql_name='paginatedSets', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('per_page', sgqlc.types.Arg(Int, graphql_name='perPage', default=None)),
        ('sort_type', sgqlc.types.Arg(SetSortType, graphql_name='sortType', default=None)),
        ('filters', sgqlc.types.Arg(SetFilters, graphql_name='filters', default=None)),
))
    )
    '''Paginated sets for this entrant

    Arguments:

    * `page` (`Int`)None
    * `per_page` (`Int`)None
    * `sort_type` (`SetSortType`): How to sort these sets
    * `filters` (`SetFilters`): Supported filter options to filter
      down set results.
    '''

    participants = sgqlc.types.Field(sgqlc.types.list_of('Participant'), graphql_name='participants')

    seeds = sgqlc.types.Field(sgqlc.types.list_of('Seed'), graphql_name='seeds')

    skill = sgqlc.types.Field(Int, graphql_name='skill')

    standing = sgqlc.types.Field('Standing', graphql_name='standing')
    '''Standing for this entrant given an event. All entrants queried
    must be in the same event (for now).
    '''

    streams = sgqlc.types.Field(sgqlc.types.list_of('Streams'), graphql_name='streams')

    team = sgqlc.types.Field(Team, graphql_name='team')
    '''Team linked to this entrant, if one exists'''



class EntrantConnection(sgqlc.types.relay.Connection):
    __schema__ = ggschema
    __field_names__ = ('page_info', 'nodes')
    page_info = sgqlc.types.Field('PageInfo', graphql_name='pageInfo')

    nodes = sgqlc.types.Field(sgqlc.types.list_of(Entrant), graphql_name='nodes')



class Event(sgqlc.types.Type):
    '''An event in a tournament'''
    __schema__ = ggschema
    __field_names__ = ('id', 'check_in_buffer', 'check_in_duration', 'check_in_enabled', 'competition_tier', 'created_at', 'deck_submission_deadline', 'entrants', 'has_decks', 'has_tasks', 'images', 'is_online', 'league', 'match_rules_markdown', 'name', 'num_entrants', 'phase_groups', 'phases', 'prizing_info', 'publishing', 'rules_markdown', 'ruleset_id', 'sets', 'slug', 'standings', 'start_at', 'state', 'stations', 'team_management_deadline', 'team_name_allowed', 'team_roster_size', 'tournament', 'type', 'updated_at', 'use_event_seeds', 'user_entrant', 'videogame', 'waves')
    id = sgqlc.types.Field(ID, graphql_name='id')

    check_in_buffer = sgqlc.types.Field(Int, graphql_name='checkInBuffer')
    '''How long before the event start will the check-in end (in seconds)'''

    check_in_duration = sgqlc.types.Field(Int, graphql_name='checkInDuration')
    '''How long the event check-in will last (in seconds)'''

    check_in_enabled = sgqlc.types.Field(Boolean, graphql_name='checkInEnabled')
    '''Whether check-in is enabled for this event'''

    competition_tier = sgqlc.types.Field(Int, graphql_name='competitionTier')
    '''Rough categorization of event tier, denoting relative importance
    in the competitive scene
    '''

    created_at = sgqlc.types.Field(Timestamp, graphql_name='createdAt')
    '''When the event was created (unix timestamp)'''

    deck_submission_deadline = sgqlc.types.Field(Timestamp, graphql_name='deckSubmissionDeadline')
    '''Last date attendees are able to create teams for team events'''

    entrants = sgqlc.types.Field(EntrantConnection, graphql_name='entrants', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(EventEntrantPageQuery, graphql_name='query', default=None)),
))
    )
    '''The entrants that belong to an event, paginated by filter criteria

    Arguments:

    * `query` (`EventEntrantPageQuery`)None
    '''

    has_decks = sgqlc.types.Field(Boolean, graphql_name='hasDecks')
    '''Whether the event has decks'''

    has_tasks = sgqlc.types.Field(Boolean, graphql_name='hasTasks')
    '''Are player tasks enabled for this event'''

    images = sgqlc.types.Field(sgqlc.types.list_of('Image'), graphql_name='images', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    '''Arguments:

    * `type` (`String`)None
    '''

    is_online = sgqlc.types.Field(Boolean, graphql_name='isOnline')
    '''Whether the event is an online event or not'''

    league = sgqlc.types.Field('League', graphql_name='league')

    match_rules_markdown = sgqlc.types.Field(String, graphql_name='matchRulesMarkdown')
    '''Markdown field for match rules/instructions'''

    name = sgqlc.types.Field(String, graphql_name='name')
    '''Title of event set by organizer'''

    num_entrants = sgqlc.types.Field(Int, graphql_name='numEntrants')
    '''Gets the number of entrants in this event'''

    phase_groups = sgqlc.types.Field(sgqlc.types.list_of('PhaseGroup'), graphql_name='phaseGroups')
    '''The phase groups that belong to an event.'''

    phases = sgqlc.types.Field(sgqlc.types.list_of('Phase'), graphql_name='phases', args=sgqlc.types.ArgDict((
        ('state', sgqlc.types.Arg(ActivityState, graphql_name='state', default=None)),
        ('phase_id', sgqlc.types.Arg(ID, graphql_name='phaseId', default=None)),
))
    )
    '''The phases that belong to an event.

    Arguments:

    * `state` (`ActivityState`): Filter phases by state. If not
      specified will default to all phases
    * `phase_id` (`ID`): Optionally only return results for this phase
    '''

    prizing_info = sgqlc.types.Field(JSON, graphql_name='prizingInfo')
    '''TO settings for prizing'''

    publishing = sgqlc.types.Field(JSON, graphql_name='publishing')

    rules_markdown = sgqlc.types.Field(String, graphql_name='rulesMarkdown')
    '''Markdown field for event rules/instructions'''

    ruleset_id = sgqlc.types.Field(Int, graphql_name='rulesetId')
    '''Id of the event ruleset'''

    sets = sgqlc.types.Field('SetConnection', graphql_name='sets', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('per_page', sgqlc.types.Arg(Int, graphql_name='perPage', default=None)),
        ('sort_type', sgqlc.types.Arg(SetSortType, graphql_name='sortType', default=None)),
        ('filters', sgqlc.types.Arg(SetFilters, graphql_name='filters', default=None)),
))
    )
    '''Paginated sets for this Event

    Arguments:

    * `page` (`Int`)None
    * `per_page` (`Int`)None
    * `sort_type` (`SetSortType`): How to sort these sets
    * `filters` (`SetFilters`): Supported filter options to filter
      down set results.
    '''

    slug = sgqlc.types.Field(String, graphql_name='slug')

    standings = sgqlc.types.Field('StandingConnection', graphql_name='standings', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(StandingPaginationQuery), graphql_name='query', default=None)),
))
    )
    '''Paginated list of standings

    Arguments:

    * `query` (`StandingPaginationQuery!`)None
    '''

    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    '''When does this event start?'''

    state = sgqlc.types.Field(ActivityState, graphql_name='state')
    '''The state of the Event.'''

    stations = sgqlc.types.Field('StationsConnection', graphql_name='stations', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(StationFilter, graphql_name='query', default=None)),
))
    )
    '''Paginated stations on this event

    Arguments:

    * `query` (`StationFilter`)None
    '''

    team_management_deadline = sgqlc.types.Field(Timestamp, graphql_name='teamManagementDeadline')
    '''Last date attendees are able to create teams for team events'''

    team_name_allowed = sgqlc.types.Field(Boolean, graphql_name='teamNameAllowed')
    '''If this is a teams event, returns whether or not teams can set
    custom names
    '''

    team_roster_size = sgqlc.types.Field('TeamRosterSize', graphql_name='teamRosterSize')
    '''Team roster size requirements'''

    tournament = sgqlc.types.Field('Tournament', graphql_name='tournament')

    type = sgqlc.types.Field(Int, graphql_name='type')
    '''The type of the event, whether an entrant will have one
    participant or multiple
    '''

    updated_at = sgqlc.types.Field(Timestamp, graphql_name='updatedAt')
    '''When the event was last modified (unix timestamp)'''

    use_event_seeds = sgqlc.types.Field(Boolean, graphql_name='useEventSeeds')
    '''Whether the event uses the new EventSeeds for seeding'''

    user_entrant = sgqlc.types.Field(Entrant, graphql_name='userEntrant', args=sgqlc.types.ArgDict((
        ('user_id', sgqlc.types.Arg(ID, graphql_name='userId', default=None)),
))
    )
    '''The entrant (if applicable) for a given user in this event

    Arguments:

    * `user_id` (`ID`): User to get entrant for. Defaults to currently
      logged in user.
    '''

    videogame = sgqlc.types.Field('Videogame', graphql_name='videogame')

    waves = sgqlc.types.Field(sgqlc.types.list_of('Wave'), graphql_name='waves', args=sgqlc.types.ArgDict((
        ('phase_id', sgqlc.types.Arg(ID, graphql_name='phaseId', default=None)),
))
    )
    '''The waves being used by the event

    Arguments:

    * `phase_id` (`ID`): Waves filtered by phaseId, returns all if not
      set.
    '''



class EventConnection(sgqlc.types.relay.Connection):
    __schema__ = ggschema
    __field_names__ = ('page_info', 'nodes')
    page_info = sgqlc.types.Field('PageInfo', graphql_name='pageInfo')

    nodes = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='nodes')



class EventOwner(sgqlc.types.Type):
    '''Name and Gamertag of the owner of an event in a league'''
    __schema__ = ggschema
    __field_names__ = ('event_id', 'email', 'gamer_tag', 'full_name')
    event_id = sgqlc.types.Field(ID, graphql_name='eventId')

    email = sgqlc.types.Field(String, graphql_name='email')

    gamer_tag = sgqlc.types.Field(String, graphql_name='gamerTag')

    full_name = sgqlc.types.Field(String, graphql_name='fullName')



class EventOwnerConnection(sgqlc.types.relay.Connection):
    __schema__ = ggschema
    __field_names__ = ('page_info', 'nodes')
    page_info = sgqlc.types.Field('PageInfo', graphql_name='pageInfo')

    nodes = sgqlc.types.Field(sgqlc.types.list_of(EventOwner), graphql_name='nodes')



class EventTeamConnection(sgqlc.types.relay.Connection):
    __schema__ = ggschema
    __field_names__ = ('page_info', 'nodes')
    page_info = sgqlc.types.Field('PageInfo', graphql_name='pageInfo')

    nodes = sgqlc.types.Field(sgqlc.types.list_of('EventTeam'), graphql_name='nodes')



class EventTier(sgqlc.types.Type):
    '''Used for league application tiers'''
    __schema__ = ggschema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(ID, graphql_name='id')

    name = sgqlc.types.Field(String, graphql_name='name')
    '''Name of this tier'''



class Game(sgqlc.types.Type):
    '''A game represents a single game within a set.'''
    __schema__ = ggschema
    __field_names__ = ('id', 'entrant1_score', 'entrant2_score', 'images', 'order_num', 'selections', 'stage', 'state', 'winner_id')
    id = sgqlc.types.Field(ID, graphql_name='id')

    entrant1_score = sgqlc.types.Field(Int, graphql_name='entrant1Score')
    '''Score of entrant 1. For smash, this is equivalent to stocks
    remaining.
    '''

    entrant2_score = sgqlc.types.Field(Int, graphql_name='entrant2Score')
    '''Score of entrant 2. For smash, this is equivalent to stocks
    remaining.
    '''

    images = sgqlc.types.Field(sgqlc.types.list_of('Image'), graphql_name='images', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    '''Arguments:

    * `type` (`String`)None
    '''

    order_num = sgqlc.types.Field(Int, graphql_name='orderNum')

    selections = sgqlc.types.Field(sgqlc.types.list_of('GameSelection'), graphql_name='selections')
    '''Selections for this game such as character, etc.'''

    stage = sgqlc.types.Field('Stage', graphql_name='stage')
    '''The stage that this game was played on (if applicable)'''

    state = sgqlc.types.Field(Int, graphql_name='state')

    winner_id = sgqlc.types.Field(Int, graphql_name='winnerId')



class GameSelection(sgqlc.types.Type):
    '''A selection for this game. i.e. character/stage selection, etc'''
    __schema__ = ggschema
    __field_names__ = ('character', 'id', 'entrant', 'order_num', 'participant', 'selection_type', 'selection_value')
    character = sgqlc.types.Field(Character, graphql_name='character')
    '''If this is a character selection, returns the selected character.'''

    id = sgqlc.types.Field(ID, graphql_name='id')

    entrant = sgqlc.types.Field(Entrant, graphql_name='entrant')
    '''The entrant who this selection is for'''

    order_num = sgqlc.types.Field(Int, graphql_name='orderNum')

    participant = sgqlc.types.Field('Participant', graphql_name='participant')
    '''The participant who this selection is for. This is only populated
    if there are selections for multiple participants of a single
    entrant
    '''

    selection_type = sgqlc.types.Field(GameSelectionType, graphql_name='selectionType')

    selection_value = sgqlc.types.Field(Int, graphql_name='selectionValue')



class Image(sgqlc.types.Type):
    '''An image'''
    __schema__ = ggschema
    __field_names__ = ('id', 'height', 'ratio', 'type', 'url', 'width')
    id = sgqlc.types.Field(ID, graphql_name='id')

    height = sgqlc.types.Field(Float, graphql_name='height')

    ratio = sgqlc.types.Field(Float, graphql_name='ratio')

    type = sgqlc.types.Field(String, graphql_name='type')

    url = sgqlc.types.Field(String, graphql_name='url')

    width = sgqlc.types.Field(Float, graphql_name='width')



class League(sgqlc.types.Type):
    '''A league'''
    __schema__ = ggschema
    __field_names__ = ('id', 'addr_state', 'city', 'country_code', 'created_at', 'currency', 'end_at', 'entrant_count', 'event_owners', 'event_registration_closes_at', 'events', 'has_offline_events', 'has_online_events', 'hashtag', 'images', 'is_online', 'lat', 'links', 'lng', 'maps_place_id', 'name', 'num_unique_players', 'postal_code', 'primary_contact', 'primary_contact_type', 'publishing', 'registration_closes_at', 'rules', 'short_slug', 'show_standings', 'slug', 'standings', 'start_at', 'state', 'team_creation_closes_at', 'tiers', 'timezone', 'tournament_type', 'updated_at', 'url', 'venue_address', 'venue_name', 'videogames')
    id = sgqlc.types.Field(ID, graphql_name='id')

    addr_state = sgqlc.types.Field(String, graphql_name='addrState')

    city = sgqlc.types.Field(String, graphql_name='city')

    country_code = sgqlc.types.Field(String, graphql_name='countryCode')

    created_at = sgqlc.types.Field(Timestamp, graphql_name='createdAt')
    '''When the tournament was created (unix timestamp)'''

    currency = sgqlc.types.Field(String, graphql_name='currency')

    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    '''When the tournament ends'''

    entrant_count = sgqlc.types.Field(Int, graphql_name='entrantCount')

    event_owners = sgqlc.types.Field(EventOwnerConnection, graphql_name='eventOwners', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(EventOwnersQuery, graphql_name='query', default=None)),
))
    )
    '''Arguments:

    * `query` (`EventOwnersQuery`)None
    '''

    event_registration_closes_at = sgqlc.types.Field(Timestamp, graphql_name='eventRegistrationClosesAt')
    '''When does event registration close'''

    events = sgqlc.types.Field(EventConnection, graphql_name='events', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(LeagueEventsQuery, graphql_name='query', default=None)),
))
    )
    '''Paginated list of events in a league

    Arguments:

    * `query` (`LeagueEventsQuery`)None
    '''

    has_offline_events = sgqlc.types.Field(Boolean, graphql_name='hasOfflineEvents')
    '''True if tournament has at least one offline event'''

    has_online_events = sgqlc.types.Field(Boolean, graphql_name='hasOnlineEvents')

    hashtag = sgqlc.types.Field(String, graphql_name='hashtag')

    images = sgqlc.types.Field(sgqlc.types.list_of(Image), graphql_name='images', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    '''Arguments:

    * `type` (`String`)None
    '''

    is_online = sgqlc.types.Field(Boolean, graphql_name='isOnline')
    '''True if tournament has at least one online event'''

    lat = sgqlc.types.Field(Float, graphql_name='lat')

    links = sgqlc.types.Field('TournamentLinks', graphql_name='links')

    lng = sgqlc.types.Field(Float, graphql_name='lng')

    maps_place_id = sgqlc.types.Field(String, graphql_name='mapsPlaceId')

    name = sgqlc.types.Field(String, graphql_name='name')
    '''The tournament name'''

    num_unique_players = sgqlc.types.Field(Int, graphql_name='numUniquePlayers')

    postal_code = sgqlc.types.Field(String, graphql_name='postalCode')

    primary_contact = sgqlc.types.Field(String, graphql_name='primaryContact')

    primary_contact_type = sgqlc.types.Field(String, graphql_name='primaryContactType')

    publishing = sgqlc.types.Field(JSON, graphql_name='publishing')
    '''Publishing settings for this tournament'''

    registration_closes_at = sgqlc.types.Field(Timestamp, graphql_name='registrationClosesAt')
    '''When does registration for the tournament end'''

    rules = sgqlc.types.Field(String, graphql_name='rules')

    short_slug = sgqlc.types.Field(String, graphql_name='shortSlug')
    '''The short slug used to form the url'''

    show_standings = sgqlc.types.Field(Boolean, graphql_name='showStandings')
    '''Whether standings for this league should be visible'''

    slug = sgqlc.types.Field(String, graphql_name='slug')

    standings = sgqlc.types.Field('StandingConnection', graphql_name='standings', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(StandingGroupStandingPageFilter, graphql_name='query', default=None)),
))
    )
    '''Paginated list of standings

    Arguments:

    * `query` (`StandingGroupStandingPageFilter`)None
    '''

    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    '''When the tournament Starts'''

    state = sgqlc.types.Field(Int, graphql_name='state')
    '''State of the tournament, can be ActivityState::CREATED,
    ActivityState::ACTIVE, or ActivityState::COMPLETED
    '''

    team_creation_closes_at = sgqlc.types.Field(Timestamp, graphql_name='teamCreationClosesAt')
    '''When is the team creation deadline'''

    tiers = sgqlc.types.Field(sgqlc.types.list_of(EventTier), graphql_name='tiers')

    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    '''The timezone of the tournament'''

    tournament_type = sgqlc.types.Field(Int, graphql_name='tournamentType')
    '''The type of tournament from TournamentType'''

    updated_at = sgqlc.types.Field(Timestamp, graphql_name='updatedAt')
    '''When the tournament was last modified (unix timestamp)'''

    url = sgqlc.types.Field(String, graphql_name='url', args=sgqlc.types.ArgDict((
        ('tab', sgqlc.types.Arg(String, graphql_name='tab', default=None)),
        ('relative', sgqlc.types.Arg(Boolean, graphql_name='relative', default=True)),
))
    )
    '''Build Tournament URL

    Arguments:

    * `tab` (`String`): Tournament tab to add to URL
    * `relative` (`Boolean`): Generate a relative URL. Defaults to
      true. Setting to false will generate an absolute URL (default:
      `true`)
    '''

    venue_address = sgqlc.types.Field(String, graphql_name='venueAddress')

    venue_name = sgqlc.types.Field(String, graphql_name='venueName')

    videogames = sgqlc.types.Field(sgqlc.types.list_of('Videogame'), graphql_name='videogames')



class LeagueConnection(sgqlc.types.relay.Connection):
    __schema__ = ggschema
    __field_names__ = ('page_info', 'nodes')
    page_info = sgqlc.types.Field('PageInfo', graphql_name='pageInfo')

    nodes = sgqlc.types.Field(sgqlc.types.list_of(League), graphql_name='nodes')



class Mutation(sgqlc.types.Type):
    __schema__ = ggschema
    __field_names__ = ('assign_station', 'assign_stream', 'delete_phase', 'delete_station', 'delete_wave', 'generate_registration_token', 'mark_set_called', 'mark_set_in_progress', 'register_for_tournament', 'report_bracket_set', 'reset_set', 'resolve_schedule_conflicts', 'swap_seeds', 'update_bracket_set', 'update_phase_groups', 'update_phase_seeding', 'update_vod_url', 'upsert_phase', 'upsert_station', 'upsert_wave')
    assign_station = sgqlc.types.Field('Set', graphql_name='assignStation', args=sgqlc.types.ArgDict((
        ('set_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='setId', default=None)),
        ('station_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='stationId', default=None)),
))
    )
    '''Assign a station to a set. If there is a stream attached to the
    station, the set will be assigned to the stream as well.

    Arguments:

    * `set_id` (`ID!`)None
    * `station_id` (`ID!`)None
    '''

    assign_stream = sgqlc.types.Field('Set', graphql_name='assignStream', args=sgqlc.types.ArgDict((
        ('set_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='setId', default=None)),
        ('stream_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='streamId', default=None)),
))
    )
    '''Assign a stream to a set

    Arguments:

    * `set_id` (`ID!`)None
    * `stream_id` (`ID!`)None
    '''

    delete_phase = sgqlc.types.Field(Boolean, graphql_name='deletePhase', args=sgqlc.types.ArgDict((
        ('phase_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='phaseId', default=None)),
))
    )
    '''Delete a phase by id

    Arguments:

    * `phase_id` (`ID!`)None
    '''

    delete_station = sgqlc.types.Field(Boolean, graphql_name='deleteStation', args=sgqlc.types.ArgDict((
        ('station_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='stationId', default=None)),
))
    )
    '''Delete a station by id

    Arguments:

    * `station_id` (`ID!`)None
    '''

    delete_wave = sgqlc.types.Field(Boolean, graphql_name='deleteWave', args=sgqlc.types.ArgDict((
        ('wave_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='waveId', default=None)),
))
    )
    '''Delete a wave by id

    Arguments:

    * `wave_id` (`ID!`)None
    '''

    generate_registration_token = sgqlc.types.Field(String, graphql_name='generateRegistrationToken', args=sgqlc.types.ArgDict((
        ('registration', sgqlc.types.Arg(sgqlc.types.non_null(TournamentRegistrationInput), graphql_name='registration', default=None)),
        ('user_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='userId', default=None)),
))
    )
    '''Generate tournament registration Token on behalf of user

    Arguments:

    * `registration` (`TournamentRegistrationInput!`)None
    * `user_id` (`ID!`)None
    '''

    mark_set_called = sgqlc.types.Field('Set', graphql_name='markSetCalled', args=sgqlc.types.ArgDict((
        ('set_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='setId', default=None)),
))
    )
    '''Update a set to called state

    Arguments:

    * `set_id` (`ID!`)None
    '''

    mark_set_in_progress = sgqlc.types.Field('Set', graphql_name='markSetInProgress', args=sgqlc.types.ArgDict((
        ('set_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='setId', default=None)),
))
    )
    '''Update a set to called state

    Arguments:

    * `set_id` (`ID!`)None
    '''

    register_for_tournament = sgqlc.types.Field('Participant', graphql_name='registerForTournament', args=sgqlc.types.ArgDict((
        ('registration', sgqlc.types.Arg(TournamentRegistrationInput, graphql_name='registration', default=None)),
        ('registration_token', sgqlc.types.Arg(String, graphql_name='registrationToken', default=None)),
))
    )
    '''Register for tournament

    Arguments:

    * `registration` (`TournamentRegistrationInput`)None
    * `registration_token` (`String`)None
    '''

    report_bracket_set = sgqlc.types.Field(sgqlc.types.list_of('Set'), graphql_name='reportBracketSet', args=sgqlc.types.ArgDict((
        ('set_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='setId', default=None)),
        ('winner_id', sgqlc.types.Arg(ID, graphql_name='winnerId', default=None)),
        ('is_dq', sgqlc.types.Arg(Boolean, graphql_name='isDQ', default=None)),
        ('game_data', sgqlc.types.Arg(sgqlc.types.list_of(BracketSetGameDataInput), graphql_name='gameData', default=None)),
))
    )
    '''Report set winner or game stats for a H2H bracket set. If winnerId
    is supplied, mark set as complete. gameData parameter will
    overwrite any existing reported game data.

    Arguments:

    * `set_id` (`ID!`)None
    * `winner_id` (`ID`)None
    * `is_dq` (`Boolean`)None
    * `game_data` (`[BracketSetGameDataInput]`)None
    '''

    reset_set = sgqlc.types.Field('Set', graphql_name='resetSet', args=sgqlc.types.ArgDict((
        ('set_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='setId', default=None)),
        ('reset_dependent_sets', sgqlc.types.Arg(Boolean, graphql_name='resetDependentSets', default=None)),
))
    )
    '''Resets set to initial state, can affect other sets and phase
    groups

    Arguments:

    * `set_id` (`ID!`)None
    * `reset_dependent_sets` (`Boolean`)None
    '''

    resolve_schedule_conflicts = sgqlc.types.Field(sgqlc.types.list_of('Seed'), graphql_name='resolveScheduleConflicts', args=sgqlc.types.ArgDict((
        ('tournament_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='tournamentId', default=None)),
        ('options', sgqlc.types.Arg(ResolveConflictsOptions, graphql_name='options', default=None)),
))
    )
    '''Automatically attempt to resolve all schedule conflicts. Returns a
    list of changed seeds

    Arguments:

    * `tournament_id` (`ID!`)None
    * `options` (`ResolveConflictsOptions`)None
    '''

    swap_seeds = sgqlc.types.Field(sgqlc.types.list_of('Seed'), graphql_name='swapSeeds', args=sgqlc.types.ArgDict((
        ('phase_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='phaseId', default=None)),
        ('seed1_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='seed1Id', default=None)),
        ('seed2_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='seed2Id', default=None)),
))
    )
    '''Swap two seed ids in a phase

    Arguments:

    * `phase_id` (`ID!`)None
    * `seed1_id` (`ID!`)None
    * `seed2_id` (`ID!`)None
    '''

    update_bracket_set = sgqlc.types.Field('Set', graphql_name='updateBracketSet', args=sgqlc.types.ArgDict((
        ('set_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='setId', default=None)),
        ('winner_id', sgqlc.types.Arg(ID, graphql_name='winnerId', default=None)),
        ('is_dq', sgqlc.types.Arg(Boolean, graphql_name='isDQ', default=None)),
        ('game_data', sgqlc.types.Arg(sgqlc.types.list_of(BracketSetGameDataInput), graphql_name='gameData', default=None)),
))
    )
    '''Update game stats for a H2H bracket set. Set winner cannot be
    changed with this function, use the resetSet mutation instead.

    Arguments:

    * `set_id` (`ID!`)None
    * `winner_id` (`ID`)None
    * `is_dq` (`Boolean`)None
    * `game_data` (`[BracketSetGameDataInput]`)None
    '''

    update_phase_groups = sgqlc.types.Field(sgqlc.types.list_of('PhaseGroup'), graphql_name='updatePhaseGroups', args=sgqlc.types.ArgDict((
        ('group_configs', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(PhaseGroupUpdateInput)), graphql_name='groupConfigs', default=None)),
))
    )
    '''Update set of phase groups in a phase

    Arguments:

    * `group_configs` (`[PhaseGroupUpdateInput]!`)None
    '''

    update_phase_seeding = sgqlc.types.Field('Phase', graphql_name='updatePhaseSeeding', args=sgqlc.types.ArgDict((
        ('phase_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='phaseId', default=None)),
        ('seed_mapping', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(UpdatePhaseSeedInfo)), graphql_name='seedMapping', default=None)),
        ('options', sgqlc.types.Arg(UpdatePhaseSeedingOptions, graphql_name='options', default=None)),
))
    )
    '''Update the seeding for a phase

    Arguments:

    * `phase_id` (`ID!`)None
    * `seed_mapping` (`[UpdatePhaseSeedInfo]!`)None
    * `options` (`UpdatePhaseSeedingOptions`)None
    '''

    update_vod_url = sgqlc.types.Field('Set', graphql_name='updateVodUrl', args=sgqlc.types.ArgDict((
        ('set_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='setId', default=None)),
        ('vod_url', sgqlc.types.Arg(String, graphql_name='vodUrl', default=None)),
))
    )
    '''Update a set's vodUrl

    Arguments:

    * `set_id` (`ID!`)None
    * `vod_url` (`String`)None
    '''

    upsert_phase = sgqlc.types.Field('Phase', graphql_name='upsertPhase', args=sgqlc.types.ArgDict((
        ('phase_id', sgqlc.types.Arg(ID, graphql_name='phaseId', default=None)),
        ('event_id', sgqlc.types.Arg(ID, graphql_name='eventId', default=None)),
        ('payload', sgqlc.types.Arg(sgqlc.types.non_null(PhaseUpsertInput), graphql_name='payload', default=None)),
))
    )
    '''Create or update a Phase

    Arguments:

    * `phase_id` (`ID`)None
    * `event_id` (`ID`)None
    * `payload` (`PhaseUpsertInput!`)None
    '''

    upsert_station = sgqlc.types.Field('Stations', graphql_name='upsertStation', args=sgqlc.types.ArgDict((
        ('station_id', sgqlc.types.Arg(ID, graphql_name='stationId', default=None)),
        ('tournament_id', sgqlc.types.Arg(ID, graphql_name='tournamentId', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.non_null(StationUpsertInput), graphql_name='fields', default=None)),
))
    )
    '''Add or update a station by id

    Arguments:

    * `station_id` (`ID`)None
    * `tournament_id` (`ID`)None
    * `fields` (`StationUpsertInput!`)None
    '''

    upsert_wave = sgqlc.types.Field('Wave', graphql_name='upsertWave', args=sgqlc.types.ArgDict((
        ('wave_id', sgqlc.types.Arg(ID, graphql_name='waveId', default=None)),
        ('tournament_id', sgqlc.types.Arg(ID, graphql_name='tournamentId', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.non_null(WaveUpsertInput), graphql_name='fields', default=None)),
))
    )
    '''Add or update a wave by id

    Arguments:

    * `wave_id` (`ID`)None
    * `tournament_id` (`ID`)None
    * `fields` (`WaveUpsertInput!`)None
    '''



class PageInfo(sgqlc.types.Type):
    __schema__ = ggschema
    __field_names__ = ('total', 'total_pages', 'page', 'per_page', 'sort_by', 'filter')
    total = sgqlc.types.Field(Int, graphql_name='total')

    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')

    page = sgqlc.types.Field(Int, graphql_name='page')

    per_page = sgqlc.types.Field(Int, graphql_name='perPage')

    sort_by = sgqlc.types.Field(String, graphql_name='sortBy')

    filter = sgqlc.types.Field(JSON, graphql_name='filter')



class Participant(sgqlc.types.Type):
    '''A participant of a tournament; either a spectator or competitor'''
    __schema__ = ggschema
    __field_names__ = ('id', 'checked_in', 'checked_in_at', 'connected_accounts', 'contact_info', 'email', 'entrants', 'events', 'gamer_tag', 'images', 'player', 'prefix', 'required_connections', 'user', 'verified')
    id = sgqlc.types.Field(ID, graphql_name='id')

    checked_in = sgqlc.types.Field(Boolean, graphql_name='checkedIn')
    '''If this participant was checked-in by admin'''

    checked_in_at = sgqlc.types.Field(Timestamp, graphql_name='checkedInAt')
    '''The time this participant was checked-in by admin'''

    connected_accounts = sgqlc.types.Field(JSON, graphql_name='connectedAccounts')
    '''Info for connected accounts to external services.'''

    contact_info = sgqlc.types.Field(ContactInfo, graphql_name='contactInfo')
    '''Contact Info selected during registration. Falls back to
    User.location and/or User.name if necessary. These fields are for
    admin use only. If you are not a tournament admin or the
    participant being queried, these fields will be null. Do not
    display this information publicly.
    '''

    email = sgqlc.types.Field(String, graphql_name='email')
    '''Email of the user, only available to admins within 18 months of
    tournament completion for tournament administrators.
    '''

    entrants = sgqlc.types.Field(sgqlc.types.list_of(Entrant), graphql_name='entrants')
    '''Entrants associated with this Participant, if applicable'''

    events = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='events')
    '''The events this participant registered for within a Tournament.'''

    gamer_tag = sgqlc.types.Field(String, graphql_name='gamerTag')
    '''The tag that was used when the participant registered, e.g. Mang0'''

    images = sgqlc.types.Field(sgqlc.types.list_of(Image), graphql_name='images', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    '''Arguments:

    * `type` (`String`)None
    '''

    player = sgqlc.types.Field('Player', graphql_name='player')

    prefix = sgqlc.types.Field(String, graphql_name='prefix')
    '''The prefix that the user set for this Tournament, e.g. C9'''

    required_connections = sgqlc.types.Field(sgqlc.types.list_of('ProfileAuthorization'), graphql_name='requiredConnections')
    '''Tournament Admin viewable field. Shows details for required social
    connections
    '''

    user = sgqlc.types.Field('User', graphql_name='user')
    '''The user this participant is associated to.'''

    verified = sgqlc.types.Field(Boolean, graphql_name='verified')
    '''If this participant is verified as actually being in the
    tournament
    '''



class ParticipantConnection(sgqlc.types.relay.Connection):
    __schema__ = ggschema
    __field_names__ = ('page_info', 'nodes')
    page_info = sgqlc.types.Field(PageInfo, graphql_name='pageInfo')

    nodes = sgqlc.types.Field(sgqlc.types.list_of(Participant), graphql_name='nodes')



class Phase(sgqlc.types.Type):
    '''A phase in an event'''
    __schema__ = ggschema
    __field_names__ = ('id', 'bracket_type', 'event', 'group_count', 'is_exhibition', 'name', 'num_seeds', 'phase_groups', 'phase_order', 'progressing_in_data', 'progressions', 'seeds', 'sets', 'state', 'waves')
    id = sgqlc.types.Field(ID, graphql_name='id')

    bracket_type = sgqlc.types.Field(BracketType, graphql_name='bracketType')
    '''The bracket type of this phase.'''

    event = sgqlc.types.Field(Event, graphql_name='event')
    '''The Event that this phase belongs to'''

    group_count = sgqlc.types.Field(Int, graphql_name='groupCount')
    '''Number of phase groups in this phase'''

    is_exhibition = sgqlc.types.Field(Boolean, graphql_name='isExhibition')
    '''Is the phase an exhibition or not.'''

    name = sgqlc.types.Field(String, graphql_name='name')
    '''Name of phase e.g. Round 1 Pools'''

    num_seeds = sgqlc.types.Field(Int, graphql_name='numSeeds')
    '''The number of seeds this phase contains.'''

    phase_groups = sgqlc.types.Field('PhaseGroupConnection', graphql_name='phaseGroups', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(PhaseGroupPageQuery, graphql_name='query', default=None)),
))
    )
    '''Phase groups under this phase, paginated

    Arguments:

    * `query` (`PhaseGroupPageQuery`)None
    '''

    phase_order = sgqlc.types.Field(Int, graphql_name='phaseOrder')
    '''The relative order of this phase within an event'''

    progressing_in_data = sgqlc.types.Field(sgqlc.types.list_of('ProgressionData'), graphql_name='progressingInData')
    '''Information about the progressions into this phase'''

    progressions = sgqlc.types.Field(sgqlc.types.list_of('Progression'), graphql_name='progressions')
    '''Information about the progressions out of this phase'''

    seeds = sgqlc.types.Field('SeedConnection', graphql_name='seeds', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(SeedPaginationQuery), graphql_name='query', default=None)),
        ('event_id', sgqlc.types.Arg(ID, graphql_name='eventId', default=None)),
))
    )
    '''Paginated seeds for this phase

    Arguments:

    * `query` (`SeedPaginationQuery!`)None
    * `event_id` (`ID`)None
    '''

    sets = sgqlc.types.Field('SetConnection', graphql_name='sets', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('per_page', sgqlc.types.Arg(Int, graphql_name='perPage', default=None)),
        ('sort_type', sgqlc.types.Arg(SetSortType, graphql_name='sortType', default=None)),
        ('filters', sgqlc.types.Arg(SetFilters, graphql_name='filters', default=None)),
))
    )
    '''Paginated sets for this Phase

    Arguments:

    * `page` (`Int`)None
    * `per_page` (`Int`)None
    * `sort_type` (`SetSortType`): How to sort these sets
    * `filters` (`SetFilters`): Supported filter options to filter
      down set results.
    '''

    state = sgqlc.types.Field(ActivityState, graphql_name='state')
    '''State of the phase'''

    waves = sgqlc.types.Field(sgqlc.types.list_of('Wave'), graphql_name='waves')



class PhaseGroup(sgqlc.types.Type):
    '''A group within a phase'''
    __schema__ = ggschema
    __field_names__ = ('id', 'bracket_type', 'bracket_url', 'display_identifier', 'first_round_time', 'num_rounds', 'phase', 'progressions_out', 'rounds', 'seed_map', 'seeds', 'sets', 'standings', 'start_at', 'state', 'tiebreak_order', 'wave')
    id = sgqlc.types.Field(ID, graphql_name='id')

    bracket_type = sgqlc.types.Field(BracketType, graphql_name='bracketType')
    '''The bracket type of this group's phase.'''

    bracket_url = sgqlc.types.Field(String, graphql_name='bracketUrl')
    '''URL for this phase groups's bracket.'''

    display_identifier = sgqlc.types.Field(String, graphql_name='displayIdentifier')
    '''Unique identifier for this group within the context of its phase'''

    first_round_time = sgqlc.types.Field(Timestamp, graphql_name='firstRoundTime')
    '''For the given phase group, this is the start time of the first
    round that occurs in the group.
    '''

    num_rounds = sgqlc.types.Field(Int, graphql_name='numRounds')

    phase = sgqlc.types.Field(Phase, graphql_name='phase')
    '''The phase associated with this phase group'''

    progressions_out = sgqlc.types.Field(sgqlc.types.list_of('Progression'), graphql_name='progressionsOut')
    '''The progressions out of this phase group'''

    rounds = sgqlc.types.Field(sgqlc.types.list_of('Round'), graphql_name='rounds')

    seed_map = sgqlc.types.Field(JSON, graphql_name='seedMap')

    seeds = sgqlc.types.Field('SeedConnection', graphql_name='seeds', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(SeedPaginationQuery), graphql_name='query', default=None)),
        ('event_id', sgqlc.types.Arg(ID, graphql_name='eventId', default=None)),
))
    )
    '''Paginated seeds for this phase group

    Arguments:

    * `query` (`SeedPaginationQuery!`)None
    * `event_id` (`ID`)None
    '''

    sets = sgqlc.types.Field('SetConnection', graphql_name='sets', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('per_page', sgqlc.types.Arg(Int, graphql_name='perPage', default=None)),
        ('sort_type', sgqlc.types.Arg(SetSortType, graphql_name='sortType', default=None)),
        ('filters', sgqlc.types.Arg(SetFilters, graphql_name='filters', default=None)),
))
    )
    '''Paginated sets on this phaseGroup

    Arguments:

    * `page` (`Int`)None
    * `per_page` (`Int`)None
    * `sort_type` (`SetSortType`): How to sort these sets
    * `filters` (`SetFilters`): Supported filter options to filter
      down set results.
    '''

    standings = sgqlc.types.Field('StandingConnection', graphql_name='standings', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(StandingGroupStandingPageFilter, graphql_name='query', default=None)),
))
    )
    '''Paginated list of standings

    Arguments:

    * `query` (`StandingGroupStandingPageFilter`)None
    '''

    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    '''Unix time the group is scheduled to start. This info could also be
    on the wave instead.
    '''

    state = sgqlc.types.Field(Int, graphql_name='state')

    tiebreak_order = sgqlc.types.Field(JSON, graphql_name='tiebreakOrder')

    wave = sgqlc.types.Field('Wave', graphql_name='wave')



class PhaseGroupConnection(sgqlc.types.relay.Connection):
    __schema__ = ggschema
    __field_names__ = ('page_info', 'nodes')
    page_info = sgqlc.types.Field(PageInfo, graphql_name='pageInfo')

    nodes = sgqlc.types.Field(sgqlc.types.list_of(PhaseGroup), graphql_name='nodes')



class Player(sgqlc.types.Type):
    '''A player'''
    __schema__ = ggschema
    __field_names__ = ('id', 'gamer_tag', 'prefix', 'rankings', 'recent_standings', 'sets', 'user')
    id = sgqlc.types.Field(ID, graphql_name='id')

    gamer_tag = sgqlc.types.Field(String, graphql_name='gamerTag')

    prefix = sgqlc.types.Field(String, graphql_name='prefix')

    rankings = sgqlc.types.Field(sgqlc.types.list_of('PlayerRank'), graphql_name='rankings', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('videogame_id', sgqlc.types.Arg(ID, graphql_name='videogameId', default=None)),
))
    )
    '''Most recent active & published rankings

    Arguments:

    * `limit` (`Int`)None
    * `videogame_id` (`ID`)None
    '''

    recent_standings = sgqlc.types.Field(sgqlc.types.list_of('Standing'), graphql_name='recentStandings', args=sgqlc.types.ArgDict((
        ('videogame_id', sgqlc.types.Arg(ID, graphql_name='videogameId', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Recent standings

    Arguments:

    * `videogame_id` (`ID`)None
    * `limit` (`Int`): Number of recent standings to fetch. Default
      value is 3. Maximum value is 20.
    '''

    sets = sgqlc.types.Field('SetConnection', graphql_name='sets', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('per_page', sgqlc.types.Arg(Int, graphql_name='perPage', default=None)),
        ('filters', sgqlc.types.Arg(SetFilters, graphql_name='filters', default=None)),
))
    )
    '''Set history for this player.

    Arguments:

    * `page` (`Int`)None
    * `per_page` (`Int`)None
    * `filters` (`SetFilters`): Supported filter options to filter
      down set results.
    '''

    user = sgqlc.types.Field('User', graphql_name='user')



class PlayerRank(sgqlc.types.Type):
    '''A player's ranks'''
    __schema__ = ggschema
    __field_names__ = ('id', 'rank', 'title')
    id = sgqlc.types.Field(ID, graphql_name='id')

    rank = sgqlc.types.Field(Int, graphql_name='rank')
    '''The player's placement on the ranking'''

    title = sgqlc.types.Field(String, graphql_name='title')



class ProfileAuthorization(sgqlc.types.Type):
    '''An OAuth ProfileAuthorization object'''
    __schema__ = ggschema
    __field_names__ = ('id', 'external_id', 'external_username', 'stream', 'type', 'url')
    id = sgqlc.types.Field(ID, graphql_name='id')

    external_id = sgqlc.types.Field(String, graphql_name='externalId')
    '''The id given by the external service'''

    external_username = sgqlc.types.Field(String, graphql_name='externalUsername')
    '''The username given by the external service (including
    discriminator if discord)
    '''

    stream = sgqlc.types.Field('Stream', graphql_name='stream')

    type = sgqlc.types.Field(AuthorizationType, graphql_name='type')
    '''The name of the external service providing this auth i.e. "twitch"'''

    url = sgqlc.types.Field(String, graphql_name='url')



class Progression(sgqlc.types.Type):
    '''A connection between a placement in an origin phase group to a
    destination seed.
    '''
    __schema__ = ggschema
    __field_names__ = ('id', 'origin_order', 'origin_phase', 'origin_phase_group', 'origin_placement', 'placeholder_name')
    id = sgqlc.types.Field(ID, graphql_name='id')

    origin_order = sgqlc.types.Field(Int, graphql_name='originOrder')

    origin_phase = sgqlc.types.Field(Phase, graphql_name='originPhase')

    origin_phase_group = sgqlc.types.Field(PhaseGroup, graphql_name='originPhaseGroup')

    origin_placement = sgqlc.types.Field(Int, graphql_name='originPlacement')

    placeholder_name = sgqlc.types.Field(String, graphql_name='placeholderName')



class ProgressionData(sgqlc.types.Type):
    '''Data on phase progression, keyed on destination PhaseId'''
    __schema__ = ggschema
    __field_names__ = ('origin', 'num_progressing')
    origin = sgqlc.types.Field(Int, graphql_name='origin')
    '''Origin phase ID that is the source of this progression.'''

    num_progressing = sgqlc.types.Field(Int, graphql_name='numProgressing')
    '''Amount of seeds per phase group that are progressing.'''



class Query(sgqlc.types.Type):
    __schema__ = ggschema
    __field_names__ = ('current_user', 'entrant', 'event', 'league', 'leagues', 'participant', 'phase', 'phase_group', 'player', 'seed', 'set', 'shop', 'stream', 'stream_queue', 'team', 'tournament', 'tournaments', 'user', 'videogame', 'videogames')
    current_user = sgqlc.types.Field('User', graphql_name='currentUser')
    '''Returns the authenticated user'''

    entrant = sgqlc.types.Field(Entrant, graphql_name='entrant', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Returns an entrant given its id

    Arguments:

    * `id` (`ID!`)None
    '''

    event = sgqlc.types.Field(Event, graphql_name='event', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('slug', sgqlc.types.Arg(String, graphql_name='slug', default=None)),
))
    )
    '''Returns an event given its id or slug

    Arguments:

    * `id` (`ID`)None
    * `slug` (`String`)None
    '''

    league = sgqlc.types.Field(League, graphql_name='league', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('slug', sgqlc.types.Arg(String, graphql_name='slug', default=None)),
))
    )
    '''Returns a league given its id or slug

    Arguments:

    * `id` (`ID`)None
    * `slug` (`String`)None
    '''

    leagues = sgqlc.types.Field(LeagueConnection, graphql_name='leagues', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(LeagueQuery), graphql_name='query', default=None)),
))
    )
    '''Paginated, filterable list of leagues

    Arguments:

    * `query` (`LeagueQuery!`)None
    '''

    participant = sgqlc.types.Field(Participant, graphql_name='participant', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('is_admin', sgqlc.types.Arg(Boolean, graphql_name='isAdmin', default=None)),
))
    )
    '''Returns a participant given its id

    Arguments:

    * `id` (`ID!`)None
    * `is_admin` (`Boolean`)None
    '''

    phase = sgqlc.types.Field(Phase, graphql_name='phase', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    '''Returns a phase given its id

    Arguments:

    * `id` (`ID`)None
    '''

    phase_group = sgqlc.types.Field(PhaseGroup, graphql_name='phaseGroup', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    '''Returns a phase group given its id

    Arguments:

    * `id` (`ID`)None
    '''

    player = sgqlc.types.Field(Player, graphql_name='player', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Returns a player given an id

    Arguments:

    * `id` (`ID!`)None
    '''

    seed = sgqlc.types.Field('Seed', graphql_name='seed', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    '''Returns a phase seed given its id

    Arguments:

    * `id` (`ID`)None
    '''

    set = sgqlc.types.Field('Set', graphql_name='set', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Returns a set given its id

    Arguments:

    * `id` (`ID!`)None
    '''

    shop = sgqlc.types.Field('Shop', graphql_name='shop', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('slug', sgqlc.types.Arg(String, graphql_name='slug', default=None)),
))
    )
    '''A shop entity

    Arguments:

    * `id` (`ID`)None
    * `slug` (`String`)None
    '''

    stream = sgqlc.types.Field('Streams', graphql_name='stream', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Returns an stream given its id

    Arguments:

    * `id` (`ID!`)None
    '''

    stream_queue = sgqlc.types.Field(sgqlc.types.list_of('StreamQueue'), graphql_name='streamQueue', args=sgqlc.types.ArgDict((
        ('tournament_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='tournamentId', default=None)),
        ('include_player_streams', sgqlc.types.Arg(Boolean, graphql_name='includePlayerStreams', default=None)),
))
    )
    '''Returns all the stream queues for a given tournament

    Arguments:

    * `tournament_id` (`ID!`)None
    * `include_player_streams` (`Boolean`)None
    '''

    team = sgqlc.types.Field(Team, graphql_name='team', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('slug', sgqlc.types.Arg(String, graphql_name='slug', default=None)),
        ('invite_code', sgqlc.types.Arg(String, graphql_name='inviteCode', default=None)),
))
    )
    '''Returns a team given its id

    Arguments:

    * `id` (`ID`)None
    * `slug` (`String`)None
    * `invite_code` (`String`)None
    '''

    tournament = sgqlc.types.Field('Tournament', graphql_name='tournament', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('slug', sgqlc.types.Arg(String, graphql_name='slug', default=None)),
))
    )
    '''Returns a tournament given its id or slug

    Arguments:

    * `id` (`ID`)None
    * `slug` (`String`)None
    '''

    tournaments = sgqlc.types.Field('TournamentConnection', graphql_name='tournaments', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(TournamentQuery), graphql_name='query', default=None)),
))
    )
    '''Paginated, filterable list of tournaments

    Arguments:

    * `query` (`TournamentQuery!`)None
    '''

    user = sgqlc.types.Field('User', graphql_name='user', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('slug', sgqlc.types.Arg(String, graphql_name='slug', default=None)),
))
    )
    '''Returns a user given a user slug of the form user/abc123, or id

    Arguments:

    * `id` (`ID`)None
    * `slug` (`String`)None
    '''

    videogame = sgqlc.types.Field('Videogame', graphql_name='videogame', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('slug', sgqlc.types.Arg(String, graphql_name='slug', default=None)),
))
    )
    '''Returns a videogame given its id

    Arguments:

    * `id` (`ID`)None
    * `slug` (`String`)None
    '''

    videogames = sgqlc.types.Field('VideogameConnection', graphql_name='videogames', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(VideogameQuery), graphql_name='query', default=None)),
))
    )
    '''Returns paginated list of videogames matching the search criteria.

    Arguments:

    * `query` (`VideogameQuery!`)None
    '''



class ResetAffectedData(sgqlc.types.Type):
    __schema__ = ggschema
    __field_names__ = ('affected_set_count', 'affected_sets', 'affected_phase_group_count')
    affected_set_count = sgqlc.types.Field(Int, graphql_name='affectedSetCount')

    affected_sets = sgqlc.types.Field(sgqlc.types.list_of('Set'), graphql_name='affectedSets')

    affected_phase_group_count = sgqlc.types.Field(Int, graphql_name='affectedPhaseGroupCount')



class Round(sgqlc.types.Type):
    '''A round within a phase group'''
    __schema__ = ggschema
    __field_names__ = ('id', 'best_of', 'number', 'start_at')
    id = sgqlc.types.Field(ID, graphql_name='id')

    best_of = sgqlc.types.Field(Int, graphql_name='bestOf')
    '''If applicable, bestOf is the number of games
    one must win a majority out of to win a set in this round
    '''

    number = sgqlc.types.Field(Int, graphql_name='number')
    '''Indicates this round's order in the phase group'''

    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    '''The time that this round is scheduled to start at'''



class Score(sgqlc.types.Type):
    '''The score that led to this standing being awarded. The meaning of
    this field can vary by standing type and is not used for some
    standing types.
    '''
    __schema__ = ggschema
    __field_names__ = ('label', 'value', 'display_value')
    label = sgqlc.types.Field(String, graphql_name='label')
    '''The name of this score. e.g. "Kills" or "Stocks"'''

    value = sgqlc.types.Field(Float, graphql_name='value')
    '''The raw score value'''

    display_value = sgqlc.types.Field(String, graphql_name='displayValue')
    '''Like value, but formatted for race format events. Formatted
    according to the race config for the front end to use.
    '''



class Seed(sgqlc.types.Type):
    '''A seed for an entrant'''
    __schema__ = ggschema
    __field_names__ = ('id', 'checked_in_participants', 'entrant', 'group_seed_num', 'is_bye', 'phase', 'phase_group', 'placeholder_name', 'placement', 'players', 'progression_seed_id', 'progression_source', 'seed_num', 'set_record_without_byes', 'standings')
    id = sgqlc.types.Field(ID, graphql_name='id')

    checked_in_participants = sgqlc.types.Field(JSON, graphql_name='checkedInParticipants')
    '''Map of Participant ID to checked in boolean'''

    entrant = sgqlc.types.Field(Entrant, graphql_name='entrant')

    group_seed_num = sgqlc.types.Field(Int, graphql_name='groupSeedNum')

    is_bye = sgqlc.types.Field(Boolean, graphql_name='isBye')

    phase = sgqlc.types.Field(Phase, graphql_name='phase')

    phase_group = sgqlc.types.Field(PhaseGroup, graphql_name='phaseGroup')

    placeholder_name = sgqlc.types.Field(String, graphql_name='placeholderName')

    placement = sgqlc.types.Field(Int, graphql_name='placement')

    players = sgqlc.types.Field(sgqlc.types.list_of(Player), graphql_name='players')
    '''The player(s) associated with this seed's entrant'''

    progression_seed_id = sgqlc.types.Field(Int, graphql_name='progressionSeedId')

    progression_source = sgqlc.types.Field(Progression, graphql_name='progressionSource')
    '''Source progression information'''

    seed_num = sgqlc.types.Field(Int, graphql_name='seedNum')

    set_record_without_byes = sgqlc.types.Field(JSON, graphql_name='setRecordWithoutByes', args=sgqlc.types.ArgDict((
        ('phase_group_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='phaseGroupId', default=None)),
))
    )
    '''Entrant's win/loss record for this standing. Scores do not include
    byes.

    Arguments:

    * `phase_group_id` (`ID!`)None
    '''

    standings = sgqlc.types.Field(sgqlc.types.list_of('Standing'), graphql_name='standings', args=sgqlc.types.ArgDict((
        ('container_type', sgqlc.types.Arg(String, graphql_name='containerType', default=None)),
))
    )
    '''Arguments:

    * `container_type` (`String`): The container of the standing
      groups to get standings for. If null, will return all standings.
    '''



class SeedConnection(sgqlc.types.relay.Connection):
    __schema__ = ggschema
    __field_names__ = ('page_info', 'nodes')
    page_info = sgqlc.types.Field(PageInfo, graphql_name='pageInfo')

    nodes = sgqlc.types.Field(sgqlc.types.list_of(Seed), graphql_name='nodes')



class Set(sgqlc.types.Type):
    '''A set'''
    __schema__ = ggschema
    __field_names__ = ('id', 'completed_at', 'created_at', 'display_score', 'entrant1_source', 'entrant2_source', 'event', 'full_round_text', 'game', 'games', 'has_placeholder', 'identifier', 'images', 'l_placement', 'loser_progression_seed', 'phase_group', 'reset_affected_data', 'round', 'set_games_type', 'slots', 'start_at', 'started_at', 'state', 'station', 'stream', 'total_games', 'updated_at', 'vod_url', 'w_placement', 'winner_id', 'winner_progression_seed')
    id = sgqlc.types.Field(ID, graphql_name='id')

    completed_at = sgqlc.types.Field(Timestamp, graphql_name='completedAt')
    '''The time this set was marked as completed'''

    created_at = sgqlc.types.Field(Timestamp, graphql_name='createdAt')
    '''The time this set was created'''

    display_score = sgqlc.types.Field(String, graphql_name='displayScore', args=sgqlc.types.ArgDict((
        ('main_entrant_id', sgqlc.types.Arg(ID, graphql_name='mainEntrantId', default=None)),
))
    )
    '''Arguments:

    * `main_entrant_id` (`ID`)None
    '''

    entrant1_source = sgqlc.types.Field('SetEntrantSource', graphql_name='entrant1Source')
    '''The source of the first entrant in this set'''

    entrant2_source = sgqlc.types.Field('SetEntrantSource', graphql_name='entrant2Source')
    '''The source of the second entrant in this set'''

    event = sgqlc.types.Field(Event, graphql_name='event')
    '''Event that this set belongs to.'''

    full_round_text = sgqlc.types.Field(String, graphql_name='fullRoundText')
    '''Full round text of this set.'''

    game = sgqlc.types.Field(Game, graphql_name='game', args=sgqlc.types.ArgDict((
        ('order_num', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='orderNum', default=None)),
))
    )
    '''Arguments:

    * `order_num` (`Int!`)None
    '''

    games = sgqlc.types.Field(sgqlc.types.list_of(Game), graphql_name='games')

    has_placeholder = sgqlc.types.Field(Boolean, graphql_name='hasPlaceholder')
    '''Whether this set contains a placeholder entrant'''

    identifier = sgqlc.types.Field(String, graphql_name='identifier')
    '''The letters that describe a unique identifier within the pool. Eg.
    F, AT
    '''

    images = sgqlc.types.Field(sgqlc.types.list_of(Image), graphql_name='images', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    '''Arguments:

    * `type` (`String`)None
    '''

    l_placement = sgqlc.types.Field(Int, graphql_name='lPlacement')

    loser_progression_seed = sgqlc.types.Field(Seed, graphql_name='loserProgressionSeed')
    '''The progression seed that the loser of this set will be placed
    into (if applicable)
    '''

    phase_group = sgqlc.types.Field(PhaseGroup, graphql_name='phaseGroup')
    '''Phase group that this Set belongs to.'''

    reset_affected_data = sgqlc.types.Field(ResetAffectedData, graphql_name='resetAffectedData')
    '''The sets that are affected from resetting this set'''

    round = sgqlc.types.Field(Int, graphql_name='round')
    '''The round number of the set. Negative numbers are losers bracket'''

    set_games_type = sgqlc.types.Field(Int, graphql_name='setGamesType')
    '''Indicates whether the set is in best of or total games mode. This
    instructs which field is used to figure out how many games are in
    this set.
    '''

    slots = sgqlc.types.Field(sgqlc.types.list_of('SetSlot'), graphql_name='slots', args=sgqlc.types.ArgDict((
        ('include_byes', sgqlc.types.Arg(Boolean, graphql_name='includeByes', default=False)),
))
    )
    '''A possible spot in a set. Use this to get all entrants in a set.
    Use this for all bracket types (FFA, elimination, etc)

    Arguments:

    * `include_byes` (`Boolean`)None (default: `false`)
    '''

    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    '''The start time of the Set. If there is no startAt time on the Set,
    will pull it from phaseGroup rounds configuration.
    '''

    started_at = sgqlc.types.Field(Timestamp, graphql_name='startedAt')

    state = sgqlc.types.Field(Int, graphql_name='state')

    station = sgqlc.types.Field('Stations', graphql_name='station')
    '''Tournament event station for a set'''

    stream = sgqlc.types.Field('Streams', graphql_name='stream')
    '''Tournament event stream for a set'''

    total_games = sgqlc.types.Field(Int, graphql_name='totalGames')
    '''If setGamesType is in total games mode, this defined the number of
    games in the set.
    '''

    updated_at = sgqlc.types.Field(Timestamp, graphql_name='updatedAt')
    '''The time this set was last updated'''

    vod_url = sgqlc.types.Field(String, graphql_name='vodUrl')
    '''Url of a VOD for this set'''

    w_placement = sgqlc.types.Field(Int, graphql_name='wPlacement')

    winner_id = sgqlc.types.Field(Int, graphql_name='winnerId')

    winner_progression_seed = sgqlc.types.Field(Seed, graphql_name='winnerProgressionSeed')
    '''The progression seed that the winner of this set will be placed
    into (if applicable)
    '''



class SetConnection(sgqlc.types.relay.Connection):
    __schema__ = ggschema
    __field_names__ = ('page_info', 'nodes')
    page_info = sgqlc.types.Field(PageInfo, graphql_name='pageInfo')

    nodes = sgqlc.types.Field(sgqlc.types.list_of(Set), graphql_name='nodes')



class SetEntrantSource(sgqlc.types.Type):
    '''Describes a source for an entrant in a set. Generally the source
    is either from a winner/loser of a set in this phase group, or a
    seed if this is a progression
    '''
    __schema__ = ggschema
    __field_names__ = ('type', 'type_id', 'condition', 'condition_string')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    '''The type of this source. e.g. set, seed'''

    type_id = sgqlc.types.Field(ID, graphql_name='typeId')
    '''The ID of the type of this source. e.g. set ID, seed ID, etc.'''

    condition = sgqlc.types.Field(String, graphql_name='condition')
    '''The condition of this source. e.g. winner, loser, etc.'''

    condition_string = sgqlc.types.Field(String, graphql_name='conditionString')
    '''Human readable string for the condition. e.g. "Winner of Set
    #1234" or "Seed #1"
    '''



class SetSlot(sgqlc.types.Type):
    '''A slot in a set where a seed currently or will eventually exist in
    order to participate in the set.
    '''
    __schema__ = ggschema
    __field_names__ = ('id', 'entrant', 'prereq_id', 'prereq_placement', 'prereq_type', 'seed', 'slot_index', 'standing')
    id = sgqlc.types.Field(ID, graphql_name='id')

    entrant = sgqlc.types.Field(Entrant, graphql_name='entrant')

    prereq_id = sgqlc.types.Field(String, graphql_name='prereqId')
    '''Pairs with prereqType, is the ID of the prereq.'''

    prereq_placement = sgqlc.types.Field(Int, graphql_name='prereqPlacement')
    '''Given a set prereq type, defines the placement required in the
    origin set to end up in this slot.
    '''

    prereq_type = sgqlc.types.Field(String, graphql_name='prereqType')
    '''Describes where the entity in this slot comes from.'''

    seed = sgqlc.types.Field(Seed, graphql_name='seed')

    slot_index = sgqlc.types.Field(Int, graphql_name='slotIndex')
    '''The index of the slot. Unique per set.'''

    standing = sgqlc.types.Field('Standing', graphql_name='standing')
    '''The standing within this set for the seed currently assigned to
    this slot.
    '''



class Shop(sgqlc.types.Type):
    '''A shop'''
    __schema__ = ggschema
    __field_names__ = ('id', 'levels', 'messages', 'name', 'slug', 'url')
    id = sgqlc.types.Field(ID, graphql_name='id')

    levels = sgqlc.types.Field('ShopLevelConnection', graphql_name='levels', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(ShopLevelsQuery, graphql_name='query', default=None)),
))
    )
    '''Arguments:

    * `query` (`ShopLevelsQuery`)None
    '''

    messages = sgqlc.types.Field('ShopOrderMessageConnection', graphql_name='messages', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(ShopOrderMessagesQuery, graphql_name='query', default=None)),
))
    )
    '''Arguments:

    * `query` (`ShopOrderMessagesQuery`)None
    '''

    name = sgqlc.types.Field(String, graphql_name='name')

    slug = sgqlc.types.Field(String, graphql_name='slug')

    url = sgqlc.types.Field(String, graphql_name='url')



class ShopLevel(sgqlc.types.Type):
    '''A shop level'''
    __schema__ = ggschema
    __field_names__ = ('id', 'curr_amount', 'description', 'goal_amount', 'images', 'name')
    id = sgqlc.types.Field(ID, graphql_name='id')

    curr_amount = sgqlc.types.Field(Float, graphql_name='currAmount')

    description = sgqlc.types.Field(String, graphql_name='description')

    goal_amount = sgqlc.types.Field(Float, graphql_name='goalAmount')

    images = sgqlc.types.Field(sgqlc.types.list_of(Image), graphql_name='images', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    '''Arguments:

    * `type` (`String`)None
    '''

    name = sgqlc.types.Field(String, graphql_name='name')



class ShopLevelConnection(sgqlc.types.relay.Connection):
    __schema__ = ggschema
    __field_names__ = ('page_info', 'nodes')
    page_info = sgqlc.types.Field(PageInfo, graphql_name='pageInfo')

    nodes = sgqlc.types.Field(sgqlc.types.list_of(ShopLevel), graphql_name='nodes')



class ShopOrderMessage(sgqlc.types.Type):
    '''The message and player info for a shop order'''
    __schema__ = ggschema
    __field_names__ = ('id', 'gamertag', 'message', 'name', 'player', 'total')
    id = sgqlc.types.Field(ID, graphql_name='id')

    gamertag = sgqlc.types.Field(String, graphql_name='gamertag')
    '''The player's gamertag. Returns null if anonymous message type'''

    message = sgqlc.types.Field(String, graphql_name='message')
    '''The order message'''

    name = sgqlc.types.Field(String, graphql_name='name')
    '''The player's name. Returns null unless name & tag display is
    selected
    '''

    player = sgqlc.types.Field(Player, graphql_name='player')
    '''The player who left the comment'''

    total = sgqlc.types.Field(Float, graphql_name='total')
    '''The total order amount'''



class ShopOrderMessageConnection(sgqlc.types.relay.Connection):
    __schema__ = ggschema
    __field_names__ = ('page_info', 'nodes')
    page_info = sgqlc.types.Field(PageInfo, graphql_name='pageInfo')

    nodes = sgqlc.types.Field(sgqlc.types.list_of(ShopOrderMessage), graphql_name='nodes')



class Stage(sgqlc.types.Type):
    '''Video Stage'''
    __schema__ = ggschema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(ID, graphql_name='id')

    name = sgqlc.types.Field(String, graphql_name='name')
    '''Stage name'''



class Standing(sgqlc.types.Type):
    '''A standing indicates the placement of something within a
    container.
    '''
    __schema__ = ggschema
    __field_names__ = ('id', 'container', 'entrant', 'is_final', 'metadata', 'placement', 'player', 'stats', 'total_points')
    id = sgqlc.types.Field(ID, graphql_name='id')

    container = sgqlc.types.Field('StandingContainer', graphql_name='container')
    '''The containing entity that contextualizes this standing. Event
    standings, for example, represent an entrant's standing in the
    entire event vs. Set standings which is an entrant's standing in
    only a single set within an event.
    '''

    entrant = sgqlc.types.Field(Entrant, graphql_name='entrant')
    '''If the entity this standing is assigned to can be resolved into an
    entrant, this will provide the entrant.
    '''

    is_final = sgqlc.types.Field(Boolean, graphql_name='isFinal')

    metadata = sgqlc.types.Field(JSON, graphql_name='metadata')
    '''Metadata that goes along with this standing. Can take on different
    forms based on standing group type and settings.
    '''

    placement = sgqlc.types.Field(Int, graphql_name='placement')

    player = sgqlc.types.Field(Player, graphql_name='player')
    '''The player(s) tied to this standing's entity'''

    stats = sgqlc.types.Field('StandingStats', graphql_name='stats')

    total_points = sgqlc.types.Field(Float, graphql_name='totalPoints')



class StandingConnection(sgqlc.types.relay.Connection):
    __schema__ = ggschema
    __field_names__ = ('page_info', 'nodes')
    page_info = sgqlc.types.Field(PageInfo, graphql_name='pageInfo')

    nodes = sgqlc.types.Field(sgqlc.types.list_of(Standing), graphql_name='nodes')



class StandingStats(sgqlc.types.Type):
    '''Any stats related to this standing. This type is experimental and
    very likely to change in the future.
    '''
    __schema__ = ggschema
    __field_names__ = ('score',)
    score = sgqlc.types.Field(Score, graphql_name='score')



class Stations(sgqlc.types.Type):
    '''Stations, such as a stream setup, at an event'''
    __schema__ = ggschema
    __field_names__ = ('id', 'can_auto_assign', 'cluster_number', 'cluster_prefix', 'enabled', 'identifier', 'num_setups', 'number', 'prefix', 'queue', 'queue_depth', 'state', 'updated_at')
    id = sgqlc.types.Field(ID, graphql_name='id')

    can_auto_assign = sgqlc.types.Field(Boolean, graphql_name='canAutoAssign')

    cluster_number = sgqlc.types.Field(String, graphql_name='clusterNumber')

    cluster_prefix = sgqlc.types.Field(Int, graphql_name='clusterPrefix')

    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')

    identifier = sgqlc.types.Field(Int, graphql_name='identifier')

    num_setups = sgqlc.types.Field(Int, graphql_name='numSetups')

    number = sgqlc.types.Field(Int, graphql_name='number')

    prefix = sgqlc.types.Field(String, graphql_name='prefix')

    queue = sgqlc.types.Field(JSON, graphql_name='queue')

    queue_depth = sgqlc.types.Field(Int, graphql_name='queueDepth')

    state = sgqlc.types.Field(Int, graphql_name='state')

    updated_at = sgqlc.types.Field(Timestamp, graphql_name='updatedAt')



class StationsConnection(sgqlc.types.relay.Connection):
    __schema__ = ggschema
    __field_names__ = ('page_info', 'nodes')
    page_info = sgqlc.types.Field(PageInfo, graphql_name='pageInfo')

    nodes = sgqlc.types.Field(sgqlc.types.list_of(Stations), graphql_name='nodes')



class Stream(sgqlc.types.Type):
    '''A Stream object'''
    __schema__ = ggschema
    __field_names__ = ('id', 'is_online', 'name', 'type')
    id = sgqlc.types.Field(ID, graphql_name='id')

    is_online = sgqlc.types.Field(Boolean, graphql_name='isOnline')
    '''Whether the stream is currently live. May be slightly delayed.'''

    name = sgqlc.types.Field(String, graphql_name='name')
    '''The name of the stream'''

    type = sgqlc.types.Field(StreamType, graphql_name='type')
    '''The name of the external service providing this auth i.e. "twitch"'''



class StreamQueue(sgqlc.types.Type):
    '''A Stream queue object'''
    __schema__ = ggschema
    __field_names__ = ('id', 'sets', 'stream')
    id = sgqlc.types.Field(String, graphql_name='id')

    sets = sgqlc.types.Field(sgqlc.types.list_of(Set), graphql_name='sets')
    '''The sets on the stream'''

    stream = sgqlc.types.Field('Streams', graphql_name='stream')
    '''The stream on the queue'''



class Streams(sgqlc.types.Type):
    '''Tournament Stream'''
    __schema__ = ggschema
    __field_names__ = ('enabled', 'id', 'follower_count', 'is_online', 'num_setups', 'parent_stream_id', 'short_name', 'stream_game', 'stream_id', 'stream_logo', 'stream_name', 'stream_source', 'stream_status', 'stream_type', 'stream_type_id')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')

    id = sgqlc.types.Field(ID, graphql_name='id')

    follower_count = sgqlc.types.Field(Int, graphql_name='followerCount')

    is_online = sgqlc.types.Field(Boolean, graphql_name='isOnline')

    num_setups = sgqlc.types.Field(Int, graphql_name='numSetups')

    parent_stream_id = sgqlc.types.Field(Int, graphql_name='parentStreamId')

    short_name = sgqlc.types.Field(String, graphql_name='shortName')

    stream_game = sgqlc.types.Field(String, graphql_name='streamGame')

    stream_id = sgqlc.types.Field(String, graphql_name='streamId')

    stream_logo = sgqlc.types.Field(String, graphql_name='streamLogo')

    stream_name = sgqlc.types.Field(String, graphql_name='streamName')

    stream_source = sgqlc.types.Field(StreamSource, graphql_name='streamSource')

    stream_status = sgqlc.types.Field(String, graphql_name='streamStatus')

    stream_type = sgqlc.types.Field(Int, graphql_name='streamType')

    stream_type_id = sgqlc.types.Field(Int, graphql_name='streamTypeId')



class TeamConnection(sgqlc.types.relay.Connection):
    __schema__ = ggschema
    __field_names__ = ('page_info', 'nodes')
    page_info = sgqlc.types.Field(PageInfo, graphql_name='pageInfo')

    nodes = sgqlc.types.Field(sgqlc.types.list_of(Team), graphql_name='nodes')



class TeamMember(sgqlc.types.Type):
    '''A member of a team'''
    __schema__ = ggschema
    __field_names__ = ('id', 'is_alternate', 'is_captain', 'member_type', 'participant', 'player', 'status')
    id = sgqlc.types.Field(ID, graphql_name='id')

    is_alternate = sgqlc.types.Field(Boolean, graphql_name='isAlternate')

    is_captain = sgqlc.types.Field(Boolean, graphql_name='isCaptain')

    member_type = sgqlc.types.Field(TeamMemberType, graphql_name='memberType')
    '''The type of the team member'''

    participant = sgqlc.types.Field(Participant, graphql_name='participant')

    player = sgqlc.types.Field(Player, graphql_name='player')

    status = sgqlc.types.Field(TeamMemberStatus, graphql_name='status')
    '''The status of the team member'''



class TeamRosterSize(sgqlc.types.Type):
    '''Team roster size requirements'''
    __schema__ = ggschema
    __field_names__ = ('max_alternates', 'max_players', 'min_alternates', 'min_players')
    max_alternates = sgqlc.types.Field(Int, graphql_name='maxAlternates')

    max_players = sgqlc.types.Field(Int, graphql_name='maxPlayers')

    min_alternates = sgqlc.types.Field(Int, graphql_name='minAlternates')

    min_players = sgqlc.types.Field(Int, graphql_name='minPlayers')



class Tournament(sgqlc.types.Type):
    '''A tournament'''
    __schema__ = ggschema
    __field_names__ = ('id', 'addr_state', 'admins', 'city', 'country_code', 'created_at', 'currency', 'end_at', 'event_registration_closes_at', 'events', 'has_offline_events', 'has_online_events', 'hashtag', 'images', 'is_online', 'is_registration_open', 'lat', 'links', 'lng', 'maps_place_id', 'name', 'num_attendees', 'owner', 'participants', 'postal_code', 'primary_contact', 'primary_contact_type', 'publishing', 'registration_closes_at', 'rules', 'short_slug', 'slug', 'start_at', 'state', 'stations', 'stream_queue', 'streams', 'team_creation_closes_at', 'teams', 'timezone', 'tournament_type', 'updated_at', 'url', 'venue_address', 'venue_name', 'waves')
    id = sgqlc.types.Field(ID, graphql_name='id')

    addr_state = sgqlc.types.Field(String, graphql_name='addrState')

    admins = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='admins', args=sgqlc.types.ArgDict((
        ('roles', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='roles', default=None)),
))
    )
    '''Admin-only view of admins for this tournament

    Arguments:

    * `roles` (`[String]`): Which roles to show
    '''

    city = sgqlc.types.Field(String, graphql_name='city')

    country_code = sgqlc.types.Field(String, graphql_name='countryCode')

    created_at = sgqlc.types.Field(Timestamp, graphql_name='createdAt')
    '''When the tournament was created (unix timestamp)'''

    currency = sgqlc.types.Field(String, graphql_name='currency')

    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    '''When the tournament ends'''

    event_registration_closes_at = sgqlc.types.Field(Timestamp, graphql_name='eventRegistrationClosesAt')
    '''When does event registration close'''

    events = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='events', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(EventFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    * `filter` (`EventFilter`)None
    '''

    has_offline_events = sgqlc.types.Field(Boolean, graphql_name='hasOfflineEvents')
    '''True if tournament has at least one offline event'''

    has_online_events = sgqlc.types.Field(Boolean, graphql_name='hasOnlineEvents')

    hashtag = sgqlc.types.Field(String, graphql_name='hashtag')

    images = sgqlc.types.Field(sgqlc.types.list_of(Image), graphql_name='images', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    '''Arguments:

    * `type` (`String`)None
    '''

    is_online = sgqlc.types.Field(Boolean, graphql_name='isOnline')
    '''True if tournament has at least one online event'''

    is_registration_open = sgqlc.types.Field(Boolean, graphql_name='isRegistrationOpen')
    '''Is tournament registration open'''

    lat = sgqlc.types.Field(Float, graphql_name='lat')

    links = sgqlc.types.Field('TournamentLinks', graphql_name='links')

    lng = sgqlc.types.Field(Float, graphql_name='lng')

    maps_place_id = sgqlc.types.Field(String, graphql_name='mapsPlaceId')

    name = sgqlc.types.Field(String, graphql_name='name')
    '''The tournament name'''

    num_attendees = sgqlc.types.Field(Int, graphql_name='numAttendees')
    '''Number of attendees including spectators, if public'''

    owner = sgqlc.types.Field('User', graphql_name='owner')
    '''The user who created the tournament'''

    participants = sgqlc.types.Field(ParticipantConnection, graphql_name='participants', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(ParticipantPaginationQuery), graphql_name='query', default=None)),
        ('is_admin', sgqlc.types.Arg(Boolean, graphql_name='isAdmin', default=None)),
))
    )
    '''Paginated, queryable list of participants

    Arguments:

    * `query` (`ParticipantPaginationQuery!`)None
    * `is_admin` (`Boolean`)None
    '''

    postal_code = sgqlc.types.Field(String, graphql_name='postalCode')

    primary_contact = sgqlc.types.Field(String, graphql_name='primaryContact')

    primary_contact_type = sgqlc.types.Field(String, graphql_name='primaryContactType')

    publishing = sgqlc.types.Field(JSON, graphql_name='publishing')
    '''Publishing settings for this tournament'''

    registration_closes_at = sgqlc.types.Field(Timestamp, graphql_name='registrationClosesAt')
    '''When does registration for the tournament end'''

    rules = sgqlc.types.Field(String, graphql_name='rules')

    short_slug = sgqlc.types.Field(String, graphql_name='shortSlug')
    '''The short slug used to form the url'''

    slug = sgqlc.types.Field(String, graphql_name='slug')
    '''The slug used to form the url'''

    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    '''When the tournament Starts'''

    state = sgqlc.types.Field(Int, graphql_name='state')
    '''State of the tournament, can be ActivityState::CREATED,
    ActivityState::ACTIVE, or ActivityState::COMPLETED
    '''

    stations = sgqlc.types.Field(StationsConnection, graphql_name='stations', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('per_page', sgqlc.types.Arg(Int, graphql_name='perPage', default=None)),
))
    )
    '''Arguments:

    * `page` (`Int`)None
    * `per_page` (`Int`)None
    '''

    stream_queue = sgqlc.types.Field(sgqlc.types.list_of(StreamQueue), graphql_name='streamQueue')

    streams = sgqlc.types.Field(sgqlc.types.list_of(Streams), graphql_name='streams')

    team_creation_closes_at = sgqlc.types.Field(Timestamp, graphql_name='teamCreationClosesAt')
    '''When is the team creation deadline'''

    teams = sgqlc.types.Field(TeamConnection, graphql_name='teams', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(TeamPaginationQuery), graphql_name='query', default=None)),
))
    )
    '''Paginated, queryable list of teams

    Arguments:

    * `query` (`TeamPaginationQuery!`)None
    '''

    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    '''The timezone of the tournament'''

    tournament_type = sgqlc.types.Field(Int, graphql_name='tournamentType')
    '''The type of tournament from TournamentType'''

    updated_at = sgqlc.types.Field(Timestamp, graphql_name='updatedAt')
    '''When the tournament was last modified (unix timestamp)'''

    url = sgqlc.types.Field(String, graphql_name='url', args=sgqlc.types.ArgDict((
        ('tab', sgqlc.types.Arg(String, graphql_name='tab', default=None)),
        ('relative', sgqlc.types.Arg(Boolean, graphql_name='relative', default=True)),
))
    )
    '''Build Tournament URL

    Arguments:

    * `tab` (`String`): Tournament tab to add to URL
    * `relative` (`Boolean`): Generate a relative URL. Defaults to
      true. Setting to false will generate an absolute URL (default:
      `true`)
    '''

    venue_address = sgqlc.types.Field(String, graphql_name='venueAddress')

    venue_name = sgqlc.types.Field(String, graphql_name='venueName')

    waves = sgqlc.types.Field(sgqlc.types.list_of('Wave'), graphql_name='waves')
    '''List of all waves in this tournament'''



class TournamentConnection(sgqlc.types.relay.Connection):
    __schema__ = ggschema
    __field_names__ = ('page_info', 'nodes')
    page_info = sgqlc.types.Field(PageInfo, graphql_name='pageInfo')

    nodes = sgqlc.types.Field(sgqlc.types.list_of(Tournament), graphql_name='nodes')



class TournamentLinks(sgqlc.types.Type):
    __schema__ = ggschema
    __field_names__ = ('facebook', 'discord')
    facebook = sgqlc.types.Field(String, graphql_name='facebook')

    discord = sgqlc.types.Field(String, graphql_name='discord')



class User(sgqlc.types.Type):
    '''A user'''
    __schema__ = ggschema
    __field_names__ = ('authorizations', 'id', 'bio', 'birthday', 'discriminator', 'email', 'events', 'gender_pronoun', 'images', 'leagues', 'location', 'name', 'player', 'slug', 'tournaments')
    authorizations = sgqlc.types.Field(sgqlc.types.list_of(ProfileAuthorization), graphql_name='authorizations', args=sgqlc.types.ArgDict((
        ('types', sgqlc.types.Arg(sgqlc.types.list_of(SocialConnectionType), graphql_name='types', default=None)),
))
    )
    '''Authorizations to external services (i.e. Twitch, Twitter)

    Arguments:

    * `types` (`[SocialConnectionType]`)None
    '''

    id = sgqlc.types.Field(ID, graphql_name='id')

    bio = sgqlc.types.Field(String, graphql_name='bio')

    birthday = sgqlc.types.Field(String, graphql_name='birthday')
    '''Public facing user birthday that respects user publishing settings'''

    discriminator = sgqlc.types.Field(String, graphql_name='discriminator')
    '''Uniquely identifying token for user. Same as the hashed part of
    the slug
    '''

    email = sgqlc.types.Field(String, graphql_name='email')

    events = sgqlc.types.Field(EventConnection, graphql_name='events', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(UserEventsPaginationQuery, graphql_name='query', default=None)),
))
    )
    '''Events this user has competed in

    Arguments:

    * `query` (`UserEventsPaginationQuery`)None
    '''

    gender_pronoun = sgqlc.types.Field(String, graphql_name='genderPronoun')

    images = sgqlc.types.Field(sgqlc.types.list_of(Image), graphql_name='images', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    '''Arguments:

    * `type` (`String`)None
    '''

    leagues = sgqlc.types.Field(LeagueConnection, graphql_name='leagues', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(UserLeaguesPaginationQuery, graphql_name='query', default=None)),
))
    )
    '''Leagues this user has competed in

    Arguments:

    * `query` (`UserLeaguesPaginationQuery`)None
    '''

    location = sgqlc.types.Field(Address, graphql_name='location')
    '''Public location info for this user'''

    name = sgqlc.types.Field(String, graphql_name='name')
    '''Public facing user name that respects user publishing settings'''

    player = sgqlc.types.Field(Player, graphql_name='player')
    '''player for user'''

    slug = sgqlc.types.Field(String, graphql_name='slug')

    tournaments = sgqlc.types.Field(TournamentConnection, graphql_name='tournaments', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(UserTournamentsPaginationQuery, graphql_name='query', default=None)),
))
    )
    '''Tournaments this user is organizing or competing in

    Arguments:

    * `query` (`UserTournamentsPaginationQuery`)None
    '''



class Videogame(sgqlc.types.Type):
    '''A videogame'''
    __schema__ = ggschema
    __field_names__ = ('id', 'characters', 'display_name', 'images', 'name', 'slug', 'stages')
    id = sgqlc.types.Field(ID, graphql_name='id')

    characters = sgqlc.types.Field(sgqlc.types.list_of(Character), graphql_name='characters')
    '''All characters for this videogame'''

    display_name = sgqlc.types.Field(String, graphql_name='displayName')

    images = sgqlc.types.Field(sgqlc.types.list_of(Image), graphql_name='images', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    '''Arguments:

    * `type` (`String`)None
    '''

    name = sgqlc.types.Field(String, graphql_name='name')

    slug = sgqlc.types.Field(String, graphql_name='slug')

    stages = sgqlc.types.Field(sgqlc.types.list_of(Stage), graphql_name='stages')
    '''All stages for this videogame'''



class VideogameConnection(sgqlc.types.relay.Connection):
    __schema__ = ggschema
    __field_names__ = ('page_info', 'nodes')
    page_info = sgqlc.types.Field(PageInfo, graphql_name='pageInfo')

    nodes = sgqlc.types.Field(sgqlc.types.list_of(Videogame), graphql_name='nodes')



class Wave(sgqlc.types.Type):
    '''A wave in a tournament'''
    __schema__ = ggschema
    __field_names__ = ('id', 'identifier', 'start_at')
    id = sgqlc.types.Field(ID, graphql_name='id')

    identifier = sgqlc.types.Field(String, graphql_name='identifier')
    '''The Wave Identifier'''

    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    '''Unix time the wave is scheduled to start.'''



class EventTeam(sgqlc.types.Type, Team):
    '''An event-level Team, in the context of some competition'''
    __schema__ = ggschema
    __field_names__ = ('global_team',)
    global_team = sgqlc.types.Field('GlobalTeam', graphql_name='globalTeam')



class GlobalTeam(sgqlc.types.Type, Team):
    '''Global Team'''
    __schema__ = ggschema
    __field_names__ = ('event_teams', 'league_teams')
    event_teams = sgqlc.types.Field(EventTeamConnection, graphql_name='eventTeams', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(TeamPaginationQuery, graphql_name='query', default=None)),
))
    )
    '''Arguments:

    * `query` (`TeamPaginationQuery`)None
    '''

    league_teams = sgqlc.types.Field(EventTeamConnection, graphql_name='leagueTeams', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(TeamPaginationQuery, graphql_name='query', default=None)),
))
    )
    '''Leagues-level teams for leagues this team is competing in

    Arguments:

    * `query` (`TeamPaginationQuery`)None
    '''



class RaceBracketConfig(sgqlc.types.Type, BracketConfig):
    '''Race specific bracket configuration'''
    __schema__ = ggschema
    __field_names__ = ('automatic_end_time', 'automatic_start_time', 'goal_target_comparator', 'goal_target_value', 'limit_mode', 'limit_value', 'race_type')
    automatic_end_time = sgqlc.types.Field(Timestamp, graphql_name='automaticEndTime')

    automatic_start_time = sgqlc.types.Field(Timestamp, graphql_name='automaticStartTime')

    goal_target_comparator = sgqlc.types.Field(Comparator, graphql_name='goalTargetComparator')

    goal_target_value = sgqlc.types.Field(String, graphql_name='goalTargetValue')

    limit_mode = sgqlc.types.Field(RaceLimitMode, graphql_name='limitMode')

    limit_value = sgqlc.types.Field(Int, graphql_name='limitValue')

    race_type = sgqlc.types.Field(RaceType, graphql_name='raceType')



class RaceMatchConfig(sgqlc.types.Type, MatchConfig):
    '''Race specific match configuration'''
    __schema__ = ggschema
    __field_names__ = ('player_reporting_enabled', 'verification_methods', 'verification_required')
    player_reporting_enabled = sgqlc.types.Field(Boolean, graphql_name='playerReportingEnabled')
    '''Can players report results?'''

    verification_methods = sgqlc.types.Field(sgqlc.types.list_of(MatchConfigVerificationMethod), graphql_name='verificationMethods')
    '''Accepted methods of verification that players can use'''

    verification_required = sgqlc.types.Field(Boolean, graphql_name='verificationRequired')
    '''Are players required to submit verification of their reported
    results?
    '''



class TeamActionSet(sgqlc.types.Type, ActionSet):
    '''A set of actions available for a team to take'''
    __schema__ = ggschema
    __field_names__ = ()



########################################################################
# Unions
########################################################################
class StandingContainer(sgqlc.types.Union):
    '''The containing entity that this standing is for'''
    __schema__ = ggschema
    __types__ = (Tournament, Event, PhaseGroup, Set)



########################################################################
# Schema Entry Points
########################################################################
ggschema.query_type = Query
ggschema.mutation_type = Mutation
ggschema.subscription_type = None

