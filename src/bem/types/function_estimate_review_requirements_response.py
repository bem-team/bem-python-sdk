# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "FunctionEstimateReviewRequirementsResponse",
    "Estimate",
    "EstimateConfidenceDistribution",
    "EstimateThresholdMatrix",
    "EstimateThresholdMatrixAccuracyAboveThreshold",
    "EstimateThresholdMatrixAccuracyAboveThreshold_95",
    "EstimateThresholdMatrixFalseDiscoveryRate",
    "EstimateThresholdMatrixFalseDiscoveryRate_95",
    "EstimateThresholdMatrixFalsePositiveRate",
    "EstimateThresholdMatrixFalsePositiveRate_95",
    "EstimateThresholdMatrixPrecision",
    "EstimateThresholdMatrixPrecision_95",
    "EstimateThresholdMatrixRecall",
    "EstimateThresholdMatrixRecall_95",
    "Metrics",
    "MetricsAggregateMetrics",
    "MetricsFieldMetric",
    "MetricsFieldMetricMetrics",
]


class EstimateConfidenceDistribution(BaseModel):
    """Distribution of confidence levels"""

    high: Optional[int] = None

    low: Optional[int] = None

    medium: Optional[int] = None


class EstimateThresholdMatrixAccuracyAboveThreshold_95(BaseModel):
    """
    Confidence interval for a rate/proportion using Wald (normal approximation) method by default.

    Wald confidence intervals use the normal approximation to the binomial distribution.
    For extreme rates or small sample sizes, Wilson confidence intervals may be more appropriate.
    """

    current_sample: int = FieldInfo(alias="currentSample")
    """Current number of samples/observations available"""

    sample_needed: int = FieldInfo(alias="sampleNeeded")
    """Minimum number of samples needed for reliable confidence interval calculation"""

    ci_lower: Optional[float] = FieldInfo(alias="ciLower", default=None)
    """Lower bound of the confidence interval (null if insufficient sample size)"""

    ci_upper: Optional[float] = FieldInfo(alias="ciUpper", default=None)
    """Upper bound of the confidence interval (null if insufficient sample size)"""

    mid: Optional[float] = None
    """
    Point estimate (observed rate) at the center of the interval (null if
    insufficient sample size)
    """


class EstimateThresholdMatrixAccuracyAboveThreshold(BaseModel):
    """
    Accuracy confidence intervals for samples above threshold, by confidence level.
    Keys are confidence levels as strings ("90", "95", "99").
    Values contain statistical confidence intervals.
    """

    api_95: Optional[EstimateThresholdMatrixAccuracyAboveThreshold_95] = FieldInfo(alias="95", default=None)
    """
    Confidence interval for a rate/proportion using Wald (normal approximation)
    method by default.

    Wald confidence intervals use the normal approximation to the binomial
    distribution. For extreme rates or small sample sizes, Wilson confidence
    intervals may be more appropriate.
    """


class EstimateThresholdMatrixFalseDiscoveryRate_95(BaseModel):
    """
    Confidence interval for a rate/proportion using Wald (normal approximation) method by default.

    Wald confidence intervals use the normal approximation to the binomial distribution.
    For extreme rates or small sample sizes, Wilson confidence intervals may be more appropriate.
    """

    current_sample: int = FieldInfo(alias="currentSample")
    """Current number of samples/observations available"""

    sample_needed: int = FieldInfo(alias="sampleNeeded")
    """Minimum number of samples needed for reliable confidence interval calculation"""

    ci_lower: Optional[float] = FieldInfo(alias="ciLower", default=None)
    """Lower bound of the confidence interval (null if insufficient sample size)"""

    ci_upper: Optional[float] = FieldInfo(alias="ciUpper", default=None)
    """Upper bound of the confidence interval (null if insufficient sample size)"""

    mid: Optional[float] = None
    """
    Point estimate (observed rate) at the center of the interval (null if
    insufficient sample size)
    """


class EstimateThresholdMatrixFalseDiscoveryRate(BaseModel):
    """
    False Discovery Rate confidence intervals by confidence level.
    Keys are confidence levels as strings ("90", "95", "99").
    Values contain statistical confidence intervals.
    """

    api_95: Optional[EstimateThresholdMatrixFalseDiscoveryRate_95] = FieldInfo(alias="95", default=None)
    """
    Confidence interval for a rate/proportion using Wald (normal approximation)
    method by default.

    Wald confidence intervals use the normal approximation to the binomial
    distribution. For extreme rates or small sample sizes, Wilson confidence
    intervals may be more appropriate.
    """


class EstimateThresholdMatrixFalsePositiveRate_95(BaseModel):
    """
    Confidence interval for a rate/proportion using Wald (normal approximation) method by default.

    Wald confidence intervals use the normal approximation to the binomial distribution.
    For extreme rates or small sample sizes, Wilson confidence intervals may be more appropriate.
    """

    current_sample: int = FieldInfo(alias="currentSample")
    """Current number of samples/observations available"""

    sample_needed: int = FieldInfo(alias="sampleNeeded")
    """Minimum number of samples needed for reliable confidence interval calculation"""

    ci_lower: Optional[float] = FieldInfo(alias="ciLower", default=None)
    """Lower bound of the confidence interval (null if insufficient sample size)"""

    ci_upper: Optional[float] = FieldInfo(alias="ciUpper", default=None)
    """Upper bound of the confidence interval (null if insufficient sample size)"""

    mid: Optional[float] = None
    """
    Point estimate (observed rate) at the center of the interval (null if
    insufficient sample size)
    """


class EstimateThresholdMatrixFalsePositiveRate(BaseModel):
    """
    False Positive Rate confidence intervals by confidence level.
    Keys are confidence levels as strings ("90", "95", "99").
    Values contain statistical confidence intervals.
    """

    api_95: Optional[EstimateThresholdMatrixFalsePositiveRate_95] = FieldInfo(alias="95", default=None)
    """
    Confidence interval for a rate/proportion using Wald (normal approximation)
    method by default.

    Wald confidence intervals use the normal approximation to the binomial
    distribution. For extreme rates or small sample sizes, Wilson confidence
    intervals may be more appropriate.
    """


class EstimateThresholdMatrixPrecision_95(BaseModel):
    """
    Confidence interval for a rate/proportion using Wald (normal approximation) method by default.

    Wald confidence intervals use the normal approximation to the binomial distribution.
    For extreme rates or small sample sizes, Wilson confidence intervals may be more appropriate.
    """

    current_sample: int = FieldInfo(alias="currentSample")
    """Current number of samples/observations available"""

    sample_needed: int = FieldInfo(alias="sampleNeeded")
    """Minimum number of samples needed for reliable confidence interval calculation"""

    ci_lower: Optional[float] = FieldInfo(alias="ciLower", default=None)
    """Lower bound of the confidence interval (null if insufficient sample size)"""

    ci_upper: Optional[float] = FieldInfo(alias="ciUpper", default=None)
    """Upper bound of the confidence interval (null if insufficient sample size)"""

    mid: Optional[float] = None
    """
    Point estimate (observed rate) at the center of the interval (null if
    insufficient sample size)
    """


class EstimateThresholdMatrixPrecision(BaseModel):
    """
    Precision confidence intervals by confidence level.
    Keys are confidence levels as strings ("90", "95", "99").
    Values contain statistical confidence intervals.
    """

    api_95: Optional[EstimateThresholdMatrixPrecision_95] = FieldInfo(alias="95", default=None)
    """
    Confidence interval for a rate/proportion using Wald (normal approximation)
    method by default.

    Wald confidence intervals use the normal approximation to the binomial
    distribution. For extreme rates or small sample sizes, Wilson confidence
    intervals may be more appropriate.
    """


class EstimateThresholdMatrixRecall_95(BaseModel):
    """
    Confidence interval for a rate/proportion using Wald (normal approximation) method by default.

    Wald confidence intervals use the normal approximation to the binomial distribution.
    For extreme rates or small sample sizes, Wilson confidence intervals may be more appropriate.
    """

    current_sample: int = FieldInfo(alias="currentSample")
    """Current number of samples/observations available"""

    sample_needed: int = FieldInfo(alias="sampleNeeded")
    """Minimum number of samples needed for reliable confidence interval calculation"""

    ci_lower: Optional[float] = FieldInfo(alias="ciLower", default=None)
    """Lower bound of the confidence interval (null if insufficient sample size)"""

    ci_upper: Optional[float] = FieldInfo(alias="ciUpper", default=None)
    """Upper bound of the confidence interval (null if insufficient sample size)"""

    mid: Optional[float] = None
    """
    Point estimate (observed rate) at the center of the interval (null if
    insufficient sample size)
    """


class EstimateThresholdMatrixRecall(BaseModel):
    """
    Recall confidence intervals by confidence level.
    Keys are confidence levels as strings ("90", "95", "99").
    Values contain statistical confidence intervals.
    """

    api_95: Optional[EstimateThresholdMatrixRecall_95] = FieldInfo(alias="95", default=None)
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


class MetricsAggregateMetrics(BaseModel):
    """Comprehensive performance metrics"""

    accuracy: Optional[float] = None
    """Overall accuracy"""

    f1_score: Optional[float] = FieldInfo(alias="f1Score", default=None)
    """F1 Score (harmonic mean of precision and recall)"""

    fn: Optional[int] = None
    """False Negatives"""

    fp: Optional[int] = None
    """False Positives"""

    precision: Optional[float] = None
    """Precision (TP / (TP + FP))"""

    recall: Optional[float] = None
    """Recall (TP / (TP + FN))"""

    tn: Optional[int] = None
    """True Negatives"""

    tp: Optional[int] = None
    """True Positives"""


class MetricsFieldMetricMetrics(BaseModel):
    """Comprehensive performance metrics"""

    accuracy: Optional[float] = None
    """Overall accuracy"""

    f1_score: Optional[float] = FieldInfo(alias="f1Score", default=None)
    """F1 Score (harmonic mean of precision and recall)"""

    fn: Optional[int] = None
    """False Negatives"""

    fp: Optional[int] = None
    """False Positives"""

    precision: Optional[float] = None
    """Precision (TP / (TP + FP))"""

    recall: Optional[float] = None
    """Recall (TP / (TP + FN))"""

    tn: Optional[int] = None
    """True Negatives"""

    tp: Optional[int] = None
    """True Positives"""


class MetricsFieldMetric(BaseModel):
    """Enhanced field metrics with comprehensive analytics"""

    field_path: str = FieldInfo(alias="fieldPath")
    """JSON path to the field"""

    metrics: Optional[MetricsFieldMetricMetrics] = None
    """Comprehensive performance metrics"""


class Metrics(BaseModel):
    """Detailed performance metrics and analysis"""

    aggregate_metrics: Optional[MetricsAggregateMetrics] = FieldInfo(alias="aggregateMetrics", default=None)
    """Comprehensive performance metrics"""

    field_metrics: Optional[List[MetricsFieldMetric]] = FieldInfo(alias="fieldMetrics", default=None)
    """Enhanced field metrics with comprehensive analytics"""

    precision_recall_auc: Optional[float] = FieldInfo(alias="precisionRecallAuc", default=None)
    """Area Under the Precision-Recall Curve"""


class FunctionEstimateReviewRequirementsResponse(BaseModel):
    """Response containing review requirements estimate"""

    estimate: Estimate
    """Detailed review requirements estimate"""

    function_name: str = FieldInfo(alias="functionName")
    """Name of the analyzed function"""

    function_version_num: int = FieldInfo(alias="functionVersionNum")
    """Version number of the function that was analyzed"""

    metrics: Optional[Metrics] = None
    """Detailed performance metrics and analysis"""
