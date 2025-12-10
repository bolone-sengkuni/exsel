import io

import qrcode

from rich.console import Console


# Import only Console here to avoid circular imports caused by
# `from app.config.imports import *` which re-exports modules that
# in turn import this file.
console = Console()


def generate_qr_ascii(data: str) -> str:
    qr = qrcode.QRCode(border=1)
    qr.add_data(data)
    qr.make(fit=True)
    output = io.StringIO()
    qr.print_ascii(out=output, invert=True)
    return output.getvalue()


