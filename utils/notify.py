import requests
from slack_sdk import WebClient


class SlackNotifier:
    """
    Slackへの通知を行うクラス

    Attributes:
        webhook_url (str): SlackのWebhook URL
        client (WebClient): Slack SDKのWebClientオブジェクト
    """

    def __init__(self, webhook_url: str):
        """
        SlackNotifierクラスのコンストラクタ

        Args:
            webhook_url (str): SlackのWebhook URL
        """
        self.webhook_url = webhook_url
        self.client = WebClient()

    def send_message(self, message: str) -> bool:
        """
        メッセージをSlackに送信する

        Args:
            message (str): 送信するメッセージ

        Returns:
            bool: 送信成功の場合はTrue、失敗の場合はFalse
        """
        try:
            response = requests.post(self.webhook_url, json={"text": message})
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Slackへの通知に失敗しました: {e}")
            return False
        except Exception as e:
            print(f"予期しないエラーが発生しました: {e}")
            return False