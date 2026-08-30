from PyQt6.QtWidgets import QWidget, QHBoxLayout

def init_widget_details(widget: QWidget, name: str, tooltip: str):
	widget.setObjectName(name)
	widget.setToolTip(tooltip)

def embed_into_hbox_layout(widget: QWidget, margin=5) -> QWidget:
	result = QWidget()
	layout = QHBoxLayout(result)
	layout.setContentsMargins(margin, margin, margin, margin)
	layout.addWidget(widget)
	return result