# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .metrics_details import MetricsDetails
from .rate_confidence_interval import RateConfidenceInterval

__all__ = [
    "FunctionEstimateReviewRequirementsResponse",
    "Estimate",
    "EstimateConfidenceDistribution",
    "EstimateThresholdMatrix",
    "EstimateThresholdMatrixAccuracyAboveThreshold",
    "EstimateThresholdMatrixFalseDiscoveryRate",
    "EstimateThresholdMatrixFalsePositiveRate",
    "EstimateThresholdMatrixPrecision",
    "EstimateThresholdMatrixRecall",
]


class EstimateConfidenceDistribution(BaseModel):
    """Distribution of confidence levels"""

    high: Optional[int] = None

    low: Optional[int] = None

    medium: Optional[int] = None


class EstimateThresholdMatrixAccuracyAboveThreshold(BaseModel):
    """
    Accuracy confidence intervals for samples above threshold, by confidence level.
    Keys are confidence levels as strings ("90", "95", "99").
    Values contain statistical confidence intervals.
    """

    api_95: Optional[RateConfidenceInterval] = FieldInfo(alias="95", default=None)
    """
    Confidence interval for a rate/proportion using Wald (normal approximation)
    method by default.

    Wald confidence intervals use the normal approximation to the binomial
    distribution. For extreme rates or small sample sizes, Wilson confidence
    intervals may be more appropriate.
    """


class EstimateThresholdMatrixFalseDiscoveryRate(BaseModel):
    """
    False Discovery Rate confidence intervals by confidence level.
    Keys are confidence levels as strings ("90", "95", "99").
    Values contain statistical confidence intervals.
    """

    api_95: Optional[RateConfidenceInterval] = FieldInfo(alias="95", default=None)
    """
    Confidence interval for a rate/proportion using Wald (normal approximation)
    method by default.

    Wald confidence intervals use the normal approximation to the binomial
    distribution. For extreme rates or small sample sizes, Wilson confidence
    intervals may be more appropriate.
    """


class EstimateThresholdMatrixFalsePositiveRate(BaseModel):
    """
    False Positive Rate confidence intervals by confidence level.
    Keys are confidence levels as strings ("90", "95", "99").
    Values contain statistical confidence intervals.
    """

    api_95: Optional[RateConfidenceInterval] = FieldInfo(alias="95", default=None)
    """
    Confidence interval for a rate/proportion using Wald (normal approximation)
    method by default.

    Wald confidence intervals use the normal approximation to the binomial
    distribution. For extreme rates or small sample sizes, Wilson confidence
    intervals may be more appropriate.
    """


class EstimateThresholdMatrixPrecision(BaseModel):
    """
    Precision confidence intervals by confidence level.
    Keys are confidence levels as strings ("90", "95", "99").
    Values contain statistical confidence intervals.
    """

    api_95: Optional[RateConfidenceInterval] = FieldInfo(alias="95", default=None)
    """
    Confidence interval for a rate/proportion using Wald (normal approximation)
    method by default.

    Wald confidence intervals use the normal approximation to the binomial
    distribution. For extreme rates or small sample sizes, Wilson confidence
    intervals may be more appropriate.
    """


class EstimateThresholdMatrixRecall(BaseModel):
    """
    Recall confidence intervals by confidence level.
    Keys are confidence levels as strings ("90", "95", "99").
    Values contain statistical confidence intervals.
    """

    api_95: Optional[RateConfidenceInterval] = FieldInfo(alias="95", default=None)
    """
    Confidence interval for a rate/proportion using Wald (normal approximation)
    method by default.

    Wald confidence intervals use the normal approximation to the binomial
    distribution. For extreme rates or small sample sizes, Wilson confidence
    intervals may be more appropriate.
    """


class EstimateThresholdMatrix(BaseModel):
    """Results for a specific confidence threshold analysis"""

    fn: int
    """False Negatives"""

    fp: int
    """False Positives"""

    threshold: float
    """Confidence threshold value"""

    tn: int
    """True Negatives"""

    tp: int
    """True Positives"""

    accuracy_above_threshold: Optional[EstimateThresholdMatrixAccuracyAboveThreshold] = FieldInfo(
        alias="accuracyAboveThreshold", default=None
    )
    """
    Accuracy confidence intervals for samples above threshold, by confidence level.
    Keys are confidence levels as strings ("90", "95", "99"). Values contain
    statistical confidence intervals.
    """

    false_discovery_rate: Optional[EstimateThresholdMatrixFalseDiscoveryRate] = FieldInfo(
        alias="falseDiscoveryRate", default=None
    )
    """
    False Discovery Rate confidence intervals by confidence level. Keys are
    confidence levels as strings ("90", "95", "99"). Values contain statistical
    confidence intervals.
    """

    false_positive_rate: Optional[EstimateThresholdMatrixFalsePositiveRate] = FieldInfo(
        alias="falsePositiveRate", default=None
    )
    """
    False Positive Rate confidence intervals by confidence level. Keys are
    confidence levels as strings ("90", "95", "99"). Values contain statistical
    confidence intervals.
    """

    precision: Optional[EstimateThresholdMatrixPrecision] = None
    """
    Precision confidence intervals by confidence level. Keys are confidence levels
    as strings ("90", "95", "99"). Values contain statistical confidence intervals.
    """

    recall: Optional[EstimateThresholdMatrixRecall] = None
    """
    Recall confidence intervals by confidence level. Keys are confidence levels as
    strings ("90", "95", "99"). Values contain statistical confidence intervals.
    """


class Estimate(BaseModel):
    """Detailed review requirements estimate"""

    confidence_distribution: EstimateConfidenceDistribution = FieldInfo(alias="confidenceDistribution")
    """Distribution of confidence levels"""

    labeled_transformations: int = FieldInfo(alias="labeledTransformations")
    """Number of transformations already labeled"""

    missing_evaluations: int = FieldInfo(alias="missingEvaluations")
    """Number of transformations without evaluation data"""

    threshold_matrix: List[EstimateThresholdMatrix] = FieldInfo(alias="thresholdMatrix")
    """Statistical analysis across confidence thresholds"""

    total_transformations: int = FieldInfo(alias="totalTransformations")
    """Total number of transformations analyzed"""

    unlabeled_transformations: int = FieldInfo(alias="unlabeledTransformations")
    """Number of transformations not yet labeled"""


class FunctionEstimateReviewRequirementsResponse(BaseModel):
    """Response containing review requirements estimate"""

    estimate: Estimate
    """Detailed review requirements estimate"""

    function_name: str = FieldInfo(alias="functionName")
    """Name of the analyzed function"""

    function_version_num: int = FieldInfo(alias="functionVersionNum")
    """Version number of the function that was analyzed"""

    metrics: Optional[MetricsDetails] = None
    """Detailed performance metrics and analysis"""
