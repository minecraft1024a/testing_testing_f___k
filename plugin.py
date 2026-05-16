"""
testing_testing_f___k 插件主类
"""

from src.app.plugin_system.api.log_api import get_logger
from src.core.components.base import BasePlugin
from src.core.components.loader import register_plugin

from .components.configs.config import Config

logger = get_logger("testing_testing_f___k")


@register_plugin
class TestingTestingFKPlugin(BasePlugin):
    """
    testing_testing_f___k 插件
    """

    plugin_name = "testing_testing_f___k"
    plugin_version = "1.0.0"
    plugin_author = "Your Name"
    plugin_description = "testing_testing_f___k 插件"
    configs = [Config]

    def get_components(self) -> list[type]:
        """获取插件内所有组件类

        Returns:
            list[type]: 插件内所有组件类的列表
        """
        return []
