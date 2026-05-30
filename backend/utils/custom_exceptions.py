class InvalidFileError(Exception):
    """Exception raised when an invalid file is encountered."""
    pass
class NotFoundError(Exception):
    """Exception raised when an item is not found."""
    pass
class AuthenticationError(Exception):
    """Exception raised for authentication failures."""
    pass
class PipelineError(Exception):
    """Exception raised when a pipeline execution fails."""
    pass

