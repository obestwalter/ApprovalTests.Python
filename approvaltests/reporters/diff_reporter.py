from .first_working_reporter import FirstWorkingReporter
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory
from .python_native_reporter import PythonNativeReporter


class DiffReporter(FirstWorkingReporter):
    """
    The DiffReporter class goes through a chain of possible diffing tools,
    to find the first option installed on your system.

    If none are found, it falls back to writing the diffs on
    the console.

    At present, the default Reporter is the DiffReporter.
    """

    def __init__(self, reporter_factory=None):
        factory = reporter_factory or GenericDiffReporterFactory()
        
        reporters = list(factory.get_all_reporters())
        reporters.append(PythonNativeReporter())
        super(DiffReporter, self).__init__(*reporters)
