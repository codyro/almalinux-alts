import os
import typing
from abc import abstractmethod


__all__ = ['BaseUploader', 'BaseLogsUploader', 'UploadError']


class UploadError(Exception):
    pass


class BaseUploader(object):

    def get_artifacts_list(self, artifacts_dir: str) -> typing.List[str]:
        """
        Returns the list of the files in artifacts directory
        that need to be uploaded.

        Parameters
        ----------
        artifacts_dir : str
            Path to artifacts directory.

        Returns
        -------
        list
            List of files.

        """
        return [
            os.path.join(artifacts_dir, file)
            for file in os.listdir(artifacts_dir)
            if not os.path.isdir(file)
        ]

    @abstractmethod
    def upload(self, artifacts_dir: str, **kwargs) -> \
            typing.Tuple[typing.Dict[str, str], bool]:
        raise NotImplementedError()

    @abstractmethod
    def upload_single_file(self, *args, **kwargs) -> typing.Any:
        raise NotImplementedError()


class BaseLogsUploader(BaseUploader):

    def get_artifacts_list(self, artifacts_dir: str) -> typing.List[str]:
        all_files = super().get_artifacts_list(artifacts_dir)
        return [file_ for file_ in all_files if file_.endswith('.log')]
