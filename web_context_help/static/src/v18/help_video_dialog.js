/* Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
 * License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
 *
 * VERSION-DEPENDENT: Odoo 18 adapter.
 * Dialog listing the videos of the directory set by the system parameter
 * web_help_video_path: a click on a video inserts it in the help page.
 */
import {Component, onWillStart, useState} from "@odoo/owl";
import {Dialog} from "@web/core/dialog/dialog";
import {rpc} from "@web/core/network/rpc";

export class HelpVideoDialog extends Component {
    static template = "web_context_help.HelpVideoDialog";
    static components = {Dialog};
    static props = {
        close: Function,
        onSelect: Function,
    };

    setup() {
        this.state = useState({path: "", exists: true, videos: [], filter: ""});
        onWillStart(async () => {
            Object.assign(this.state, await rpc("/web_context_help/videos"));
        });
    }

    get videos() {
        const filter = this.state.filter.trim().toLowerCase();
        return this.state.videos.filter(
            (video) => !filter || video.name.toLowerCase().includes(filter)
        );
    }

    formatSize(size) {
        return size >= 1048576
            ? `${(size / 1048576).toFixed(1)} MB`
            : `${Math.ceil(size / 1024)} KB`;
    }

    select(video) {
        this.props.onSelect(video);
        this.props.close();
    }
}
