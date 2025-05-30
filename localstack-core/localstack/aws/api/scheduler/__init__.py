from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

CapacityProvider = str
CapacityProviderStrategyItemBase = int
CapacityProviderStrategyItemWeight = int
ClientToken = str
DeadLetterConfigArnString = str
Description = str
DetailType = str
EnableECSManagedTags = bool
EnableExecuteCommand = bool
Group = str
KmsKeyArn = str
MaxResults = int
MaximumEventAgeInSeconds = int
MaximumRetryAttempts = int
MaximumWindowInMinutes = int
MessageGroupId = str
Name = str
NamePrefix = str
NextToken = str
PlacementConstraintExpression = str
PlacementStrategyField = str
PlatformVersion = str
ReferenceId = str
RoleArn = str
SageMakerPipelineParameterName = str
SageMakerPipelineParameterValue = str
ScheduleArn = str
ScheduleExpression = str
ScheduleExpressionTimezone = str
ScheduleGroupArn = str
ScheduleGroupName = str
ScheduleGroupNamePrefix = str
SecurityGroup = str
Source = str
String = str
Subnet = str
TagKey = str
TagResourceArn = str
TagValue = str
TargetArn = str
TargetInput = str
TargetPartitionKey = str
TaskCount = int
TaskDefinitionArn = str


class ActionAfterCompletion(StrEnum):
    NONE = "NONE"
    DELETE = "DELETE"


class AssignPublicIp(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class FlexibleTimeWindowMode(StrEnum):
    OFF = "OFF"
    FLEXIBLE = "FLEXIBLE"


class LaunchType(StrEnum):
    EC2 = "EC2"
    FARGATE = "FARGATE"
    EXTERNAL = "EXTERNAL"


class PlacementConstraintType(StrEnum):
    distinctInstance = "distinctInstance"
    memberOf = "memberOf"


class PlacementStrategyType(StrEnum):
    random = "random"
    spread = "spread"
    binpack = "binpack"


class PropagateTags(StrEnum):
    TASK_DEFINITION = "TASK_DEFINITION"


class ScheduleGroupState(StrEnum):
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


class ScheduleState(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ConflictException(ServiceException):
    code: str = "ConflictException"
    sender_fault: bool = True
    status_code: int = 409


class InternalServerException(ServiceException):
    code: str = "InternalServerException"
    sender_fault: bool = False
    status_code: int = 500


class ResourceNotFoundException(ServiceException):
    code: str = "ResourceNotFoundException"
    sender_fault: bool = True
    status_code: int = 404


class ServiceQuotaExceededException(ServiceException):
    code: str = "ServiceQuotaExceededException"
    sender_fault: bool = True
    status_code: int = 402


class ThrottlingException(ServiceException):
    code: str = "ThrottlingException"
    sender_fault: bool = True
    status_code: int = 429


class ValidationException(ServiceException):
    code: str = "ValidationException"
    sender_fault: bool = True
    status_code: int = 400


Subnets = List[Subnet]
SecurityGroups = List[SecurityGroup]


class AwsVpcConfiguration(TypedDict, total=False):
    AssignPublicIp: Optional[AssignPublicIp]
    SecurityGroups: Optional[SecurityGroups]
    Subnets: Subnets


class CapacityProviderStrategyItem(TypedDict, total=False):
    base: Optional[CapacityProviderStrategyItemBase]
    capacityProvider: CapacityProvider
    weight: Optional[CapacityProviderStrategyItemWeight]


CapacityProviderStrategy = List[CapacityProviderStrategyItem]


class Tag(TypedDict, total=False):
    Key: TagKey
    Value: TagValue


TagList = List[Tag]


class CreateScheduleGroupInput(ServiceRequest):
    ClientToken: Optional[ClientToken]
    Name: ScheduleGroupName
    Tags: Optional[TagList]


class CreateScheduleGroupOutput(TypedDict, total=False):
    ScheduleGroupArn: ScheduleGroupArn


class SqsParameters(TypedDict, total=False):
    MessageGroupId: Optional[MessageGroupId]


class SageMakerPipelineParameter(TypedDict, total=False):
    Name: SageMakerPipelineParameterName
    Value: SageMakerPipelineParameterValue


SageMakerPipelineParameterList = List[SageMakerPipelineParameter]


class SageMakerPipelineParameters(TypedDict, total=False):
    PipelineParameterList: Optional[SageMakerPipelineParameterList]


class RetryPolicy(TypedDict, total=False):
    MaximumEventAgeInSeconds: Optional[MaximumEventAgeInSeconds]
    MaximumRetryAttempts: Optional[MaximumRetryAttempts]


class KinesisParameters(TypedDict, total=False):
    PartitionKey: TargetPartitionKey


class EventBridgeParameters(TypedDict, total=False):
    DetailType: DetailType
    Source: Source


TagMap = Dict[TagKey, TagValue]
Tags = List[TagMap]
PlacementStrategy = TypedDict(
    "PlacementStrategy",
    {
        "field": Optional[PlacementStrategyField],
        "type": Optional[PlacementStrategyType],
    },
    total=False,
)
PlacementStrategies = List[PlacementStrategy]
PlacementConstraint = TypedDict(
    "PlacementConstraint",
    {
        "expression": Optional[PlacementConstraintExpression],
        "type": Optional[PlacementConstraintType],
    },
    total=False,
)
PlacementConstraints = List[PlacementConstraint]


class NetworkConfiguration(TypedDict, total=False):
    awsvpcConfiguration: Optional[AwsVpcConfiguration]


class EcsParameters(TypedDict, total=False):
    CapacityProviderStrategy: Optional[CapacityProviderStrategy]
    EnableECSManagedTags: Optional[EnableECSManagedTags]
    EnableExecuteCommand: Optional[EnableExecuteCommand]
    Group: Optional[Group]
    LaunchType: Optional[LaunchType]
    NetworkConfiguration: Optional[NetworkConfiguration]
    PlacementConstraints: Optional[PlacementConstraints]
    PlacementStrategy: Optional[PlacementStrategies]
    PlatformVersion: Optional[PlatformVersion]
    PropagateTags: Optional[PropagateTags]
    ReferenceId: Optional[ReferenceId]
    Tags: Optional[Tags]
    TaskCount: Optional[TaskCount]
    TaskDefinitionArn: TaskDefinitionArn


class DeadLetterConfig(TypedDict, total=False):
    Arn: Optional[DeadLetterConfigArnString]


class Target(TypedDict, total=False):
    Arn: TargetArn
    DeadLetterConfig: Optional[DeadLetterConfig]
    EcsParameters: Optional[EcsParameters]
    EventBridgeParameters: Optional[EventBridgeParameters]
    Input: Optional[TargetInput]
    KinesisParameters: Optional[KinesisParameters]
    RetryPolicy: Optional[RetryPolicy]
    RoleArn: RoleArn
    SageMakerPipelineParameters: Optional[SageMakerPipelineParameters]
    SqsParameters: Optional[SqsParameters]


StartDate = datetime


class FlexibleTimeWindow(TypedDict, total=False):
    MaximumWindowInMinutes: Optional[MaximumWindowInMinutes]
    Mode: FlexibleTimeWindowMode


EndDate = datetime


class CreateScheduleInput(ServiceRequest):
    ActionAfterCompletion: Optional[ActionAfterCompletion]
    ClientToken: Optional[ClientToken]
    Description: Optional[Description]
    EndDate: Optional[EndDate]
    FlexibleTimeWindow: FlexibleTimeWindow
    GroupName: Optional[ScheduleGroupName]
    KmsKeyArn: Optional[KmsKeyArn]
    Name: Name
    ScheduleExpression: ScheduleExpression
    ScheduleExpressionTimezone: Optional[ScheduleExpressionTimezone]
    StartDate: Optional[StartDate]
    State: Optional[ScheduleState]
    Target: Target


class CreateScheduleOutput(TypedDict, total=False):
    ScheduleArn: ScheduleArn


CreationDate = datetime


class DeleteScheduleGroupInput(ServiceRequest):
    ClientToken: Optional[ClientToken]
    Name: ScheduleGroupName


class DeleteScheduleGroupOutput(TypedDict, total=False):
    pass


class DeleteScheduleInput(ServiceRequest):
    ClientToken: Optional[ClientToken]
    GroupName: Optional[ScheduleGroupName]
    Name: Name


class DeleteScheduleOutput(TypedDict, total=False):
    pass


class GetScheduleGroupInput(ServiceRequest):
    Name: ScheduleGroupName


LastModificationDate = datetime


class GetScheduleGroupOutput(TypedDict, total=False):
    Arn: Optional[ScheduleGroupArn]
    CreationDate: Optional[CreationDate]
    LastModificationDate: Optional[LastModificationDate]
    Name: Optional[ScheduleGroupName]
    State: Optional[ScheduleGroupState]


class GetScheduleInput(ServiceRequest):
    GroupName: Optional[ScheduleGroupName]
    Name: Name


class GetScheduleOutput(TypedDict, total=False):
    ActionAfterCompletion: Optional[ActionAfterCompletion]
    Arn: Optional[ScheduleArn]
    CreationDate: Optional[CreationDate]
    Description: Optional[Description]
    EndDate: Optional[EndDate]
    FlexibleTimeWindow: Optional[FlexibleTimeWindow]
    GroupName: Optional[ScheduleGroupName]
    KmsKeyArn: Optional[KmsKeyArn]
    LastModificationDate: Optional[LastModificationDate]
    Name: Optional[Name]
    ScheduleExpression: Optional[ScheduleExpression]
    ScheduleExpressionTimezone: Optional[ScheduleExpressionTimezone]
    StartDate: Optional[StartDate]
    State: Optional[ScheduleState]
    Target: Optional[Target]


class ListScheduleGroupsInput(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NamePrefix: Optional[ScheduleGroupNamePrefix]
    NextToken: Optional[NextToken]


class ScheduleGroupSummary(TypedDict, total=False):
    Arn: Optional[ScheduleGroupArn]
    CreationDate: Optional[CreationDate]
    LastModificationDate: Optional[LastModificationDate]
    Name: Optional[ScheduleGroupName]
    State: Optional[ScheduleGroupState]


ScheduleGroupList = List[ScheduleGroupSummary]


class ListScheduleGroupsOutput(TypedDict, total=False):
    NextToken: Optional[NextToken]
    ScheduleGroups: ScheduleGroupList


class ListSchedulesInput(ServiceRequest):
    GroupName: Optional[ScheduleGroupName]
    MaxResults: Optional[MaxResults]
    NamePrefix: Optional[NamePrefix]
    NextToken: Optional[NextToken]
    State: Optional[ScheduleState]


class TargetSummary(TypedDict, total=False):
    Arn: TargetArn


class ScheduleSummary(TypedDict, total=False):
    Arn: Optional[ScheduleArn]
    CreationDate: Optional[CreationDate]
    GroupName: Optional[ScheduleGroupName]
    LastModificationDate: Optional[LastModificationDate]
    Name: Optional[Name]
    State: Optional[ScheduleState]
    Target: Optional[TargetSummary]


ScheduleList = List[ScheduleSummary]


class ListSchedulesOutput(TypedDict, total=False):
    NextToken: Optional[NextToken]
    Schedules: ScheduleList


class ListTagsForResourceInput(ServiceRequest):
    ResourceArn: TagResourceArn


class ListTagsForResourceOutput(TypedDict, total=False):
    Tags: Optional[TagList]


TagKeyList = List[TagKey]


class TagResourceInput(ServiceRequest):
    ResourceArn: TagResourceArn
    Tags: TagList


class TagResourceOutput(TypedDict, total=False):
    pass


class UntagResourceInput(ServiceRequest):
    ResourceArn: TagResourceArn
    TagKeys: TagKeyList


class UntagResourceOutput(TypedDict, total=False):
    pass


class UpdateScheduleInput(ServiceRequest):
    ActionAfterCompletion: Optional[ActionAfterCompletion]
    ClientToken: Optional[ClientToken]
    Description: Optional[Description]
    EndDate: Optional[EndDate]
    FlexibleTimeWindow: FlexibleTimeWindow
    GroupName: Optional[ScheduleGroupName]
    KmsKeyArn: Optional[KmsKeyArn]
    Name: Name
    ScheduleExpression: ScheduleExpression
    ScheduleExpressionTimezone: Optional[ScheduleExpressionTimezone]
    StartDate: Optional[StartDate]
    State: Optional[ScheduleState]
    Target: Target


class UpdateScheduleOutput(TypedDict, total=False):
    ScheduleArn: ScheduleArn


class SchedulerApi:
    service = "scheduler"
    version = "2021-06-30"

    @handler("CreateSchedule")
    def create_schedule(
        self,
        context: RequestContext,
        flexible_time_window: FlexibleTimeWindow,
        name: Name,
        schedule_expression: ScheduleExpression,
        target: Target,
        action_after_completion: ActionAfterCompletion | None = None,
        client_token: ClientToken | None = None,
        description: Description | None = None,
        end_date: EndDate | None = None,
        group_name: ScheduleGroupName | None = None,
        kms_key_arn: KmsKeyArn | None = None,
        schedule_expression_timezone: ScheduleExpressionTimezone | None = None,
        start_date: StartDate | None = None,
        state: ScheduleState | None = None,
        **kwargs,
    ) -> CreateScheduleOutput:
        raise NotImplementedError

    @handler("CreateScheduleGroup")
    def create_schedule_group(
        self,
        context: RequestContext,
        name: ScheduleGroupName,
        client_token: ClientToken | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateScheduleGroupOutput:
        raise NotImplementedError

    @handler("DeleteSchedule")
    def delete_schedule(
        self,
        context: RequestContext,
        name: Name,
        client_token: ClientToken | None = None,
        group_name: ScheduleGroupName | None = None,
        **kwargs,
    ) -> DeleteScheduleOutput:
        raise NotImplementedError

    @handler("DeleteScheduleGroup")
    def delete_schedule_group(
        self,
        context: RequestContext,
        name: ScheduleGroupName,
        client_token: ClientToken | None = None,
        **kwargs,
    ) -> DeleteScheduleGroupOutput:
        raise NotImplementedError

    @handler("GetSchedule")
    def get_schedule(
        self,
        context: RequestContext,
        name: Name,
        group_name: ScheduleGroupName | None = None,
        **kwargs,
    ) -> GetScheduleOutput:
        raise NotImplementedError

    @handler("GetScheduleGroup")
    def get_schedule_group(
        self, context: RequestContext, name: ScheduleGroupName, **kwargs
    ) -> GetScheduleGroupOutput:
        raise NotImplementedError

    @handler("ListScheduleGroups")
    def list_schedule_groups(
        self,
        context: RequestContext,
        max_results: MaxResults | None = None,
        name_prefix: ScheduleGroupNamePrefix | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListScheduleGroupsOutput:
        raise NotImplementedError

    @handler("ListSchedules")
    def list_schedules(
        self,
        context: RequestContext,
        group_name: ScheduleGroupName | None = None,
        max_results: MaxResults | None = None,
        name_prefix: NamePrefix | None = None,
        next_token: NextToken | None = None,
        state: ScheduleState | None = None,
        **kwargs,
    ) -> ListSchedulesOutput:
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self, context: RequestContext, resource_arn: TagResourceArn, **kwargs
    ) -> ListTagsForResourceOutput:
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: TagResourceArn, tags: TagList, **kwargs
    ) -> TagResourceOutput:
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self, context: RequestContext, resource_arn: TagResourceArn, tag_keys: TagKeyList, **kwargs
    ) -> UntagResourceOutput:
        raise NotImplementedError

    @handler("UpdateSchedule")
    def update_schedule(
        self,
        context: RequestContext,
        flexible_time_window: FlexibleTimeWindow,
        name: Name,
        schedule_expression: ScheduleExpression,
        target: Target,
        action_after_completion: ActionAfterCompletion | None = None,
        client_token: ClientToken | None = None,
        description: Description | None = None,
        end_date: EndDate | None = None,
        group_name: ScheduleGroupName | None = None,
        kms_key_arn: KmsKeyArn | None = None,
        schedule_expression_timezone: ScheduleExpressionTimezone | None = None,
        start_date: StartDate | None = None,
        state: ScheduleState | None = None,
        **kwargs,
    ) -> UpdateScheduleOutput:
        raise NotImplementedError
