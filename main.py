import qrcode
import io
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.image import Image as CoreImage


class UpiQRApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # Input for UPI ID
        self.upi_input = TextInput(
            hint_text="Enter UPI ID (e.g. antick@upi)",
            multiline=False,
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.upi_input)

        # Input for Amount
        self.amount_input = TextInput(
            hint_text="Enter Amount (e.g. 150)",
            multiline=False,
            input_filter="float",
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.amount_input)

        # Generate Button
        self.generate_button = Button(
            text="Generate QR",
            size_hint=(1, 0.2)
        )
        self.generate_button.bind(on_press=self.generate_qr)
        self.layout.add_widget(self.generate_button)

        # Image placeholder
        self.qr_image = Image(size_hint=(1, 0.6))
        self.layout.add_widget(self.qr_image)

        return self.layout

    def generate_qr(self, instance):
        upi_id = self.upi_input.text.strip()
        amount = self.amount_input.text.strip()

        if not upi_id or not amount:
            return  # No input

        # Create UPI payment URI
        upi_uri = f"upi://pay?pa={upi_id}&pn=Receiver&am={amount}&cu=INR"

        # Generate QR code
        qr = qrcode.make(upi_uri)
        buf = io.BytesIO()
        qr.save(buf, format="PNG")
        buf.seek(0)

        # Load into Kivy Image widget
        im = CoreImage(buf, ext="png")
        self.qr_image.texture = im.texture


if __name__ == "__main__":
    UpiQRApp().run()
