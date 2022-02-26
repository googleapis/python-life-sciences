# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.lifesciences_v2beta.types import workflows
from .transports.base import WorkflowsServiceV2BetaTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import WorkflowsServiceV2BetaGrpcAsyncIOTransport
from .client import WorkflowsServiceV2BetaClient


class WorkflowsServiceV2BetaAsyncClient:
    """A service for running workflows, such as pipelines consisting
    of Docker containers.
    """

    _client: WorkflowsServiceV2BetaClient

    DEFAULT_ENDPOINT = WorkflowsServiceV2BetaClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = WorkflowsServiceV2BetaClient.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(
        WorkflowsServiceV2BetaClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        WorkflowsServiceV2BetaClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(WorkflowsServiceV2BetaClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        WorkflowsServiceV2BetaClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        WorkflowsServiceV2BetaClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        WorkflowsServiceV2BetaClient.parse_common_organization_path
    )
    common_project_path = staticmethod(WorkflowsServiceV2BetaClient.common_project_path)
    parse_common_project_path = staticmethod(
        WorkflowsServiceV2BetaClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        WorkflowsServiceV2BetaClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        WorkflowsServiceV2BetaClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            WorkflowsServiceV2BetaAsyncClient: The constructed client.
        """
        return WorkflowsServiceV2BetaClient.from_service_account_info.__func__(WorkflowsServiceV2BetaAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            WorkflowsServiceV2BetaAsyncClient: The constructed client.
        """
        return WorkflowsServiceV2BetaClient.from_service_account_file.__func__(WorkflowsServiceV2BetaAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return WorkflowsServiceV2BetaClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> WorkflowsServiceV2BetaTransport:
        """Returns the transport used by the client instance.

        Returns:
            WorkflowsServiceV2BetaTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(WorkflowsServiceV2BetaClient).get_transport_class,
        type(WorkflowsServiceV2BetaClient),
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, WorkflowsServiceV2BetaTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the workflows service v2 beta client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.WorkflowsServiceV2BetaTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = WorkflowsServiceV2BetaClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def run_pipeline(
        self,
        request: Union[workflows.RunPipelineRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Runs a pipeline. The returned Operation's [metadata]
        [google.longrunning.Operation.metadata] field will contain a
        [google.cloud.lifesciences.v2beta.Metadata][google.cloud.lifesciences.v2beta.Metadata]
        object describing the status of the pipeline execution. The
        [response][google.longrunning.Operation.response] field will
        contain a
        [google.cloud.lifesciences.v2beta.RunPipelineResponse][google.cloud.lifesciences.v2beta.RunPipelineResponse]
        object if the pipeline completes successfully.

        **Note:** Before you can use this method, the *Life Sciences
        Service Agent* must have access to your project. This is done
        automatically when the Cloud Life Sciences API is first enabled,
        but if you delete this permission you must disable and re-enable
        the API to grant the Life Sciences Service Agent the required
        permissions. Authorization requires the following `Google
        IAM <https://cloud.google.com/iam/>`__ permission:

        -  ``lifesciences.workflows.run``


        .. code-block:: python

            from google.cloud import lifesciences_v2beta

            def sample_run_pipeline():
                # Create a client
                client = lifesciences_v2beta.WorkflowsServiceV2BetaClient()

                # Initialize request argument(s)
                request = lifesciences_v2beta.RunPipelineRequest(
                )

                # Make the request
                operation = client.run_pipeline(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.lifesciences_v2beta.types.RunPipelineRequest, dict]):
                The request object. The arguments to the `RunPipeline`
                method. The requesting user must have the
                `iam.serviceAccounts.actAs` permission for the Cloud
                Life Sciences service account or the request will fail.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.lifesciences_v2beta.types.RunPipelineResponse` The response to the RunPipeline method, returned in the operation's result
                   field on success.

        """
        # Create or coerce a protobuf request object.
        request = workflows.RunPipelineRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.run_pipeline,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            workflows.RunPipelineResponse,
            metadata_type=workflows.Metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-life-sciences",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("WorkflowsServiceV2BetaAsyncClient",)
