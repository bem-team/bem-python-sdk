# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "FunctionCompareMetricsResponse",
    "AggregateComparison",
    "AggregateComparisonAccuracy",
    "AggregateComparisonF1Score",
    "AggregateComparisonPrecision",
    "AggregateComparisonRecall",
    "BaselineMetrics",
    "BaselineMetricsAggregateMetrics",
    "BaselineMetricsFieldMetric",
    "BaselineMetricsFieldMetricMetrics",
    "ComparisonMetrics",
    "ComparisonMetricsAggregateMetrics",
    "ComparisonMetricsFieldMetric",
    "ComparisonMetricsFieldMetricMetrics",
    "FieldMetricsChange",
    "FieldMetricsChangeComparison",
    "FieldMetricsChangeComparisonAccuracy",
    "FieldMetricsChangeComparisonF1Score",
    "FieldMetricsChangeComparisonPrecision",
    "FieldMetricsChangeComparisonRecall",
]


class AggregateComparisonAccuracy(BaseModel):
    """Comparison of a single metric between two versions"""

    baseline_value: Optional[float] = FieldInfo(alias="baselineValue", default=None)
    """Value in baseline version (null if not available)"""

    comparison_value: Optional[float] = FieldInfo(alias="comparisonValue", default=None)
    """Value in comparison version (null if not available)"""

    difference: Optional[float] = None
    """Absolute difference (comparisonValue - baselineValue)"""

    lift_percent: Optional[float] = FieldInfo(alias="liftPercent", default=None)
    """**Percentage change from baseline to comparison**

    Formula: ((comparisonValue - baselineValue) / baselineValue) \\** 100

    - Positive values indicate improvement
    - Negative values indicate regression
    """


class AggregateComparisonF1Score(BaseModel):
    """Comparison of a single metric between two versions"""

    baseline_value: Optional[float] = FieldInfo(alias="baselineValue", default=None)
    """Value in baseline version (null if not available)"""

    comparison_value: Optional[float] = FieldInfo(alias="comparisonValue", default=None)
    """Value in comparison version (null if not available)"""

    difference: Optional[float] = None
    """Absolute difference (comparisonValue - baselineValue)"""

    lift_percent: Optional[float] = FieldInfo(alias="liftPercent", default=None)
    """**Percentage change from baseline to comparison**

    Formula: ((comparisonValue - baselineValue) / baselineValue) \\** 100

    - Positive values indicate improvement
    - Negative values indicate regression
    """


class AggregateComparisonPrecision(BaseModel):
    """Comparison of a single metric between two versions"""

    baseline_value: Optional[float] = FieldInfo(alias="baselineValue", default=None)
    """Value in baseline version (null if not available)"""

    comparison_value: Optional[float] = FieldInfo(alias="comparisonValue", default=None)
    """Value in comparison version (null if not available)"""

    difference: Optional[float] = None
    """Absolute difference (comparisonValue - baselineValue)"""

    lift_percent: Optional[float] = FieldInfo(alias="liftPercent", default=None)
    """**Percentage change from baseline to comparison**

    Formula: ((comparisonValue - baselineValue) / baselineValue) \\** 100

    - Positive values indicate improvement
    - Negative values indicate regression
    """


class AggregateComparisonRecall(BaseModel):
    """Comparison of a single metric between two versions"""

    baseline_value: Optional[float] = FieldInfo(alias="baselineValue", default=None)
    """Value in baseline version (null if not available)"""

    comparison_value: Optional[float] = FieldInfo(alias="comparisonValue", default=None)
    """Value in comparison version (null if not available)"""

    difference: Optional[float] = None
    """Absolute difference (comparisonValue - baselineValue)"""

    lift_percent: Optional[float] = FieldInfo(alias="liftPercent", default=None)
    """**Percentage change from baseline to comparison**

    Formula: ((comparisonValue - baselineValue) / baselineValue) \\** 100

    - Positive values indicate improvement
    - Negative values indicate regression
    """


class AggregateComparison(BaseModel):
    """Comparison of metrics between two versions"""

    accuracy: Optional[AggregateComparisonAccuracy] = None
    """Comparison of a single metric between two versions"""

    f1_score: Optional[AggregateComparisonF1Score] = FieldInfo(alias="f1Score", default=None)
    """Comparison of a single metric between two versions"""

    precision: Optional[AggregateComparisonPrecision] = None
    """Comparison of a single metric between two versions"""

    recall: Optional[AggregateComparisonRecall] = None
    """Comparison of a single metric between two versions"""


class BaselineMetricsAggregateMetrics(BaseModel):
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


class BaselineMetricsFieldMetricMetrics(BaseModel):
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


class BaselineMetricsFieldMetric(BaseModel):
    """Enhanced field metrics with comprehensive analytics"""

    field_path: str = FieldInfo(alias="fieldPath")
    """JSON path to the field"""

    metrics: Optional[BaselineMetricsFieldMetricMetrics] = None
    """Comprehensive performance metrics"""


class BaselineMetrics(BaseModel):
    """Detailed performance metrics and analysis"""

    aggregate_metrics: Optional[BaselineMetricsAggregateMetrics] = FieldInfo(alias="aggregateMetrics", default=None)
    """Comprehensive performance metrics"""

    field_metrics: Optional[List[BaselineMetricsFieldMetric]] = FieldInfo(alias="fieldMetrics", default=None)
    """Enhanced field metrics with comprehensive analytics"""

    precision_recall_auc: Optional[float] = FieldInfo(alias="precisionRecallAuc", default=None)
    """Area Under the Precision-Recall Curve"""


class ComparisonMetricsAggregateMetrics(BaseModel):
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


class ComparisonMetricsFieldMetricMetrics(BaseModel):
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


class ComparisonMetricsFieldMetric(BaseModel):
    """Enhanced field metrics with comprehensive analytics"""

    field_path: str = FieldInfo(alias="fieldPath")
    """JSON path to the field"""

    metrics: Optional[ComparisonMetricsFieldMetricMetrics] = None
    """Comprehensive performance metrics"""


class ComparisonMetrics(BaseModel):
    """Detailed performance metrics and analysis"""

    aggregate_metrics: Optional[ComparisonMetricsAggregateMetrics] = FieldInfo(alias="aggregateMetrics", default=None)
    """Comprehensive performance metrics"""

    field_metrics: Optional[List[ComparisonMetricsFieldMetric]] = FieldInfo(alias="fieldMetrics", default=None)
    """Enhanced field metrics with comprehensive analytics"""

    precision_recall_auc: Optional[float] = FieldInfo(alias="precisionRecallAuc", default=None)
    """Area Under the Precision-Recall Curve"""


class FieldMetricsChangeComparisonAccuracy(BaseModel):
    """Comparison of a single metric between two versions"""

    baseline_value: Optional[float] = FieldInfo(alias="baselineValue", default=None)
    """Value in baseline version (null if not available)"""

    comparison_value: Optional[float] = FieldInfo(alias="comparisonValue", default=None)
    """Value in comparison version (null if not available)"""

    difference: Optional[float] = None
    """Absolute difference (comparisonValue - baselineValue)"""

    lift_percent: Optional[float] = FieldInfo(alias="liftPercent", default=None)
    """**Percentage change from baseline to comparison**

    Formula: ((comparisonValue - baselineValue) / baselineValue) \\** 100

    - Positive values indicate improvement
    - Negative values indicate regression
    """


class FieldMetricsChangeComparisonF1Score(BaseModel):
    """Comparison of a single metric between two versions"""

    baseline_value: Optional[float] = FieldInfo(alias="baselineValue", default=None)
    """Value in baseline version (null if not available)"""

    comparison_value: Optional[float] = FieldInfo(alias="comparisonValue", default=None)
    """Value in comparison version (null if not available)"""

    difference: Optional[float] = None
    """Absolute difference (comparisonValue - baselineValue)"""

    lift_percent: Optional[float] = FieldInfo(alias="liftPercent", default=None)
    """**Percentage change from baseline to comparison**

    Formula: ((comparisonValue - baselineValue) / baselineValue) \\** 100

    - Positive values indicate improvement
    - Negative values indicate regression
    """


class FieldMetricsChangeComparisonPrecision(BaseModel):
    """Comparison of a single metric between two versions"""

    baseline_value: Optional[float] = FieldInfo(alias="baselineValue", default=None)
    """Value in baseline version (null if not available)"""

    comparison_value: Optional[float] = FieldInfo(alias="comparisonValue", default=None)
    """Value in comparison version (null if not available)"""

    difference: Optional[float] = None
    """Absolute difference (comparisonValue - baselineValue)"""

    lift_percent: Optional[float] = FieldInfo(alias="liftPercent", default=None)
    """**Percentage change from baseline to comparison**

    Formula: ((comparisonValue - baselineValue) / baselineValue) \\** 100

    - Positive values indicate improvement
    - Negative values indicate regression
    """


class FieldMetricsChangeComparisonRecall(BaseModel):
    """Comparison of a single metric between two versions"""

    baseline_value: Optional[float] = FieldInfo(alias="baselineValue", default=None)
    """Value in baseline version (null if not available)"""

    comparison_value: Optional[float] = FieldInfo(alias="comparisonValue", default=None)
    """Value in comparison version (null if not available)"""

    difference: Optional[float] = None
    """Absolute difference (comparisonValue - baselineValue)"""

    lift_percent: Optional[float] = FieldInfo(alias="liftPercent", default=None)
    """**Percentage change from baseline to comparison**

    Formula: ((comparisonValue - baselineValue) / baselineValue) \\** 100

    - Positive values indicate improvement
    - Negative values indicate regression
    """


class FieldMetricsChangeComparison(BaseModel):
    """Comparison of metrics between two versions"""

    accuracy: Optional[FieldMetricsChangeComparisonAccuracy] = None
    """Comparison of a single metric between two versions"""

    f1_score: Optional[FieldMetricsChangeComparisonF1Score] = FieldInfo(alias="f1Score", default=None)
    """Comparison of a single metric between two versions"""

    precision: Optional[FieldMetricsChangeComparisonPrecision] = None
    """Comparison of a single metric between two versions"""

    recall: Optional[FieldMetricsChangeComparisonRecall] = None
    """Comparison of a single metric between two versions"""


class FieldMetricsChange(BaseModel):
    """Comparison of field-level metrics"""

    comparison: FieldMetricsChangeComparison
    """Comparison of metrics between two versions"""

    field_path: str = FieldInfo(alias="fieldPath")
    """JSON pointer path to the field"""


class FunctionCompareMetricsResponse(BaseModel):
    """**Response containing metrics comparison between two function versions**

    Shows absolute differences, lift percentages, and field-level changes.
    """

    baseline_version_num: int = FieldInfo(alias="baselineVersionNum")
    """Baseline version number used for comparison"""

    comparison_version_num: int = FieldInfo(alias="comparisonVersionNum")
    """Comparison version number"""

    function_name: str = FieldInfo(alias="functionName")
    """Name of the compared function"""

    aggregate_comparison: Optional[AggregateComparison] = FieldInfo(alias="aggregateComparison", default=None)
    """Comparison of metrics between two versions"""

    baseline_metrics: Optional[BaselineMetrics] = FieldInfo(alias="baselineMetrics", default=None)
    """Detailed performance metrics and analysis"""

    baseline_transformation_count: Optional[int] = FieldInfo(alias="baselineTransformationCount", default=None)
    """Number of transformations used to calculate baseline metrics"""

    comparison_metrics: Optional[ComparisonMetrics] = FieldInfo(alias="comparisonMetrics", default=None)
    """Detailed performance metrics and analysis"""

    comparison_transformation_count: Optional[int] = FieldInfo(alias="comparisonTransformationCount", default=None)
    """Number of transformations used to calculate comparison metrics"""

    field_metrics_changes: Optional[List[FieldMetricsChange]] = FieldInfo(alias="fieldMetricsChanges", default=None)
    """**Field-level metrics that changed significantly**

    Only includes fields where metrics changed by more than 1%.
    """

    message: Optional[str] = None
    """Optional message with additional details"""
