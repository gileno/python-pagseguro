# -*- coding: utf-8 -*-
import pytest

from pagseguro.config import Config
from pagseguro.parsers import (
    PagSeguroNotificationResponse, PagSeguroPreApprovalNotificationResponse,
    PagSeguroPreApprovalCancel, PagSeguroCheckoutSession,
    PagSeguroPreApprovalPayment, PagSeguroCheckoutResponse,
    PagSeguroTransactionSearchResult, PagSeguroPreApproval,
    PagSeguroPreApprovalSearch
)


@pytest.fixture
def config():
    return Config(sandbox=True)


@pytest.fixture
def xml_sandbox():
    return """
<transactionSearchResult>
    <date>2011-02-16T20:14:35.000-02:00</date>
    <currentPage>1</currentPage>
    <resultsInThisPage>2</resultsInThisPage>
    <totalPages>1</totalPages>
    <transactions>
        <transaction>
            <date>2011-02-05T15:46:12.000-02:00</date>
            <lastEventDate>2011-02-15T17:39:14.000-03:00</lastEventDate>
            <code>9E884542-81B3-4419-9A75-BCC6FB495EF1</code>
            <reference>REF1234</reference>
            <type>1</type>
            <status>3</status>
            <paymentMethod>
                <type>1</type>
            </paymentMethod>
            <grossAmount>49900.00</grossAmount>
            <discountAmount>0.00</discountAmount>
            <feeAmount>0.00</feeAmount>
            <netAmount>49900.00</netAmount>
            <extraAmount>0.00</extraAmount>
        </transaction>
        <transaction>
            <date>2011-02-07T18:57:52.000-02:00</date>
            <lastEventDate>2011-02-14T21:37:24.000-03:00</lastEventDate>
            <code>2FB07A22-68FF-4F83-A356-24153A0C05E1</code>
            <reference>REF5678</reference>
            <type>3</type>
            <status>4</status>
            <paymentMethod>
                <type>3</type>
            </paymentMethod>
            <grossAmount>26900.00</grossAmount>
            <discountAmount>0.00</discountAmount>
            <feeAmount>0.00</feeAmount>
            <netAmount>26900.00</netAmount>
            <extraAmount>0.00</extraAmount>
        </transaction>
    </transactions>
</transactionSearchResult>"""


def test_xml_parsers_config(config, xml_sandbox):
    notification_response = PagSeguroNotificationResponse(
        xml_sandbox, config=config
    )
    assert notification_response.config is config
    pre_approval_notification = PagSeguroPreApprovalNotificationResponse(
        xml_sandbox, config=config
    )
    assert pre_approval_notification.config is config
    pre_approval_cancel = PagSeguroPreApprovalCancel(
        xml_sandbox, config=config
    )
    assert pre_approval_cancel.config is config
    checkout_session = PagSeguroCheckoutSession(xml_sandbox, config=config)
    assert checkout_session.config is config
    pre_approval_payment = PagSeguroPreApprovalPayment(
        xml_sandbox, config=config
    )
    assert pre_approval_payment.config is config
    checkout_response = PagSeguroCheckoutResponse(xml_sandbox, config=config)
    assert checkout_response.config is config
    transaction_result = PagSeguroTransactionSearchResult(
        xml_sandbox, config=config
    )
    assert transaction_result.config is config
    pre_approval = PagSeguroPreApproval(xml_sandbox, config=config)
    assert pre_approval.config is config
    pre_approval_search = PagSeguroPreApprovalSearch(
        xml_sandbox, config=config
    )
    assert pre_approval_search.config is config
